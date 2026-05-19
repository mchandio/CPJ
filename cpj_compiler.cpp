// Cross-platform CPJ compiler
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <filesystem>

#include <map>
#include <set>
#include <memory>
#include <system_error>

// Optimization levels
enum class OptLevel
{
    None,    // No optimization
    Basic,   // Basic optimizations (constant folding, dead code elimination)
    Advanced // Advanced optimizations (loop unrolling, inlining)
};

// Code optimization context
struct OptimizationContext
{
    OptLevel level;
    bool enableInlining;
    bool enableConstFolding;
    bool enableDeadCodeElim;
    std::set<std::string> inlinedFunctions;
    std::map<std::string, std::string> constValues;

    OptimizationContext(OptLevel l = OptLevel::Basic) : level(l),
                                                        enableInlining(l >= OptLevel::Advanced),
                                                        enableConstFolding(l >= OptLevel::Basic),
                                                        enableDeadCodeElim(l >= OptLevel::Basic) {}
};

#ifdef _WIN32
#include <direct.h>
#include <windows.h>
#define PATH_SEPARATOR "\\"
#else
#include <sys/stat.h>
#include <sys/types.h>
#define PATH_SEPARATOR "/"
#endif

static inline std::string trim(const std::string &s)
{
    size_t a = 0;
    while (a < s.size() && std::isspace((unsigned char)s[a]))
        ++a;
    size_t b = s.size();
    while (b > a && std::isspace((unsigned char)s[b - 1]))
        --b;
    return s.substr(a, b - a);
}

// Constant folding optimization
static std::string optimize_constants(const std::string &code, OptimizationContext &ctx)
{
    if (!ctx.enableConstFolding)
        return code;

    std::stringstream result;
    std::istringstream stream(code);
    std::string line;

    while (std::getline(stream, line))
    {
        // Detect constant assignments
        if (line.find("const ") != std::string::npos)
        {
            size_t equals = line.find('=');
            if (equals != std::string::npos)
            {
                std::string name = trim(line.substr(line.find("const ") + 6, equals - line.find("const ") - 6));
                std::string value = trim(line.substr(equals + 1));
                if (value.back() == ';')
                    value.pop_back();
                ctx.constValues[name] = value;
            }
        }

        // Replace constant uses with their values
        for (const auto &[name, value] : ctx.constValues)
        {
            size_t pos = 0;
            while ((pos = line.find(name, pos)) != std::string::npos)
            {
                line.replace(pos, name.length(), value);
                pos += value.length();
            }
        }

        result << line << '\n';
    }

    return result.str();
}

// Function inlining optimization
static std::string optimize_inlining(const std::string &code, OptimizationContext &ctx)
{
    if (!ctx.enableInlining)
        return code;

    std::stringstream result;
    std::istringstream stream(code);
    std::string line;
    std::map<std::string, std::string> functions;

    // First pass: collect function definitions
    while (std::getline(stream, line))
    {
        if (line.find("def ") != std::string::npos && line.find("{") != std::string::npos)
        {
            std::string funcName = line.substr(line.find("def ") + 4);
            funcName = funcName.substr(0, funcName.find('('));

            // Collect function body
            std::string funcBody = line + "\n";
            int braceCount = 1;
            while (braceCount > 0 && std::getline(stream, line))
            {
                funcBody += line + "\n";
                braceCount += std::count(line.begin(), line.end(), '{');
                braceCount -= std::count(line.begin(), line.end(), '}');
            }

            functions[funcName] = funcBody;
        }
    }

    // Second pass: inline function calls
    stream.clear();
    stream.seekg(0);
    while (std::getline(stream, line))
    {
        bool isInlined = false;
        for (const auto &[funcName, funcBody] : functions)
        {
            if (line.find(funcName + "(") != std::string::npos)
            {
                // Only inline if function isn't too large
                if (std::count(funcBody.begin(), funcBody.end(), '\n') < 10)
                {
                    ctx.inlinedFunctions.insert(funcName);
                    result << "/* Inlined function " << funcName << " */\n";
                    result << funcBody;
                    isInlined = true;
                    break;
                }
            }
        }
        if (!isInlined)
        {
            result << line << '\n';
        }
    }

    return result.str();
}

// Dead code elimination
static std::string eliminate_dead_code(const std::string &code, OptimizationContext &ctx)
{
    if (!ctx.enableDeadCodeElim)
        return code;

    std::stringstream result;
    std::istringstream stream(code);
    std::string line;
    bool inDeadBlock = false;

    while (std::getline(stream, line))
    {
        // Simple dead code detection based on if(false) blocks
        if (line.find("if") != std::string::npos &&
            line.find("false") != std::string::npos)
        {
            inDeadBlock = true;
            continue;
        }

        if (inDeadBlock)
        {
            if (line.find("}") != std::string::npos)
            {
                inDeadBlock = false;
            }
            continue;
        }

        // Skip unused functions
        bool isUnusedFunc = false;
        for (const auto &func : ctx.inlinedFunctions)
        {
            if (line.find("def " + func) != std::string::npos)
            {
                isUnusedFunc = true;
                break;
            }
        }

        if (!isUnusedFunc)
        {
            result << line << '\n';
        }
    }

    return result.str();
}

static void ensure_dir(const std::string &d)
{
    if (d.empty())
        return;
    std::filesystem::create_directories(d);
}

static int run_cmd(const std::string &cmd, bool verbose)
{
    if (verbose)
        std::cerr << "Running: " << cmd << std::endl;
    return std::system(cmd.c_str());
}

static std::filesystem::path safe_absolute(const std::filesystem::path &path)
{
    std::error_code ec;
    std::filesystem::path absolute = std::filesystem::absolute(path, ec);
    if (ec)
        return path;

    std::filesystem::path canonical = std::filesystem::weakly_canonical(absolute, ec);
    if (ec)
        return absolute;
    return canonical;
}

static bool has_cpj_runtime(const std::filesystem::path &root)
{
    std::error_code ec;
    return std::filesystem::exists(root / "tools" / "cpj_emitter.py", ec) &&
           std::filesystem::exists(root / "tools" / "cpj_web_emitter.py", ec);
}

static void add_candidate_chain(std::vector<std::filesystem::path> &candidates, const std::filesystem::path &start)
{
    std::filesystem::path dir = safe_absolute(start);
    while (!dir.empty())
    {
        candidates.push_back(dir);
        std::filesystem::path parent = dir.parent_path();
        if (parent == dir)
            break;
        dir = parent;
    }
}

static std::filesystem::path executable_path(const char *argv0)
{
#ifdef _WIN32
    std::vector<char> buffer(32768);
    DWORD len = GetModuleFileNameA(nullptr, buffer.data(), static_cast<DWORD>(buffer.size()));
    if (len > 0 && len < buffer.size())
    {
        return safe_absolute(std::filesystem::path(std::string(buffer.data(), len)));
    }
#endif
    std::error_code ec;
    std::filesystem::path cwd = std::filesystem::current_path(ec);
    if (argv0 && *argv0)
    {
        std::filesystem::path path(argv0);
        if (path.is_relative() && !ec)
            path = cwd / path;
        return safe_absolute(path);
    }
    if (!ec)
        return cwd;
    return ".";
}

static std::string find_runtime_root(const char *argv0)
{
    std::vector<std::filesystem::path> candidates;
    std::error_code ec;

    std::filesystem::path exe = executable_path(argv0);
    if (!exe.empty())
        add_candidate_chain(candidates, exe.parent_path());

    if (const char *cpj_home = std::getenv("CPJ_HOME"))
        add_candidate_chain(candidates, cpj_home);

#ifdef _WIN32
    if (const char *local_app_data = std::getenv("LOCALAPPDATA"))
        add_candidate_chain(candidates, std::filesystem::path(local_app_data) / "CPJ");
#endif

    std::filesystem::path cwd = std::filesystem::current_path(ec);
    if (!ec)
        add_candidate_chain(candidates, cwd);

    for (const auto &candidate : candidates)
        if (has_cpj_runtime(candidate))
            return candidate.string();

    if (!ec)
        return cwd.string();
    return ".";
}

static void print_usage(const std::string &runtime_root)
{
    std::cout << "Usage: cpj [options] <source.cpj>\n";
    std::cout << "  --no-java        disable Java emission\n";
    std::cout << "  --no-python      disable Python emission\n";
    std::cout << "  --no-web         disable standalone web emission\n";
    std::cout << "  --web-only       emit only standalone HTML\n";
    std::cout << "  --no-compile     skip compilation steps (javac)\n";
    std::cout << "  --no-run         do not run generated artifacts\n";
    std::cout << "  -o, --out <dir>  output directory (default: generated)\n";
    std::cout << "  -v, --verbose    verbose logging\n";
    if (!runtime_root.empty())
        std::cout << "  Runtime root:    " << runtime_root << "\n";
}

static std::string shell_quote(const std::string &value)
{
#ifdef _WIN32
    std::string quoted = "\"";
    for (char c : value)
    {
        if (c == '"')
            quoted += "\\\"";
        else
            quoted += c;
    }
    quoted += "\"";
    return quoted;
#else
    std::string quoted = "'";
    for (char c : value)
    {
        if (c == '\'')
            quoted += "'\\''";
        else
            quoted += c;
    }
    quoted += "'";
    return quoted;
#endif
}

static std::string python_module_command(const std::string &module, const std::vector<std::string> &args, const std::string &runtime_root)
{
#ifdef _WIN32
    std::string cmd = "set \"PYTHONPATH=" + runtime_root + "\" && python -m " + module;
#else
    std::string cmd = "PYTHONPATH=" + shell_quote(runtime_root) + " python3 -m " + module;
#endif
    for (const auto &arg : args)
        cmd += " " + shell_quote(arg);
    return cmd;
}

int main(int argc, char **argv)
{
    const std::string runtime_root = find_runtime_root(argc > 0 ? argv[0] : nullptr);

    // CLI flags
    bool emit_java = true;
    bool emit_python = true;
    bool emit_web = true;
    bool do_compile = true;
    bool do_run = true;
    bool verbose = false;
    std::string out_dir = "generated";
    std::string path;

    // Parse args (simple style)
    for (int i = 1; i < argc; ++i)
    {
        std::string a = argv[i];
        if (a == "--no-java")
            emit_java = false;
        else if (a == "--no-python")
            emit_python = false;
        else if (a == "--no-web")
            emit_web = false;
        else if (a == "--web-only")
        {
            emit_java = false;
            emit_python = false;
            emit_web = true;
            do_run = false;
        }
        else if (a == "--no-compile")
            do_compile = false;
        else if (a == "--no-run")
            do_run = false;
        else if (a == "-v" || a == "--verbose")
            verbose = true;
        else if (a == "-o" || a == "--out")
        {
            if (i + 1 < argc)
                out_dir = argv[++i];
        }
        else if (a == "-h" || a == "--help")
        {
            print_usage(runtime_root);
            return 0;
        }
        else if (path.empty())
            path = a;
    }

    if (path.empty())
    {
        print_usage(runtime_root);
        std::cout << "\n[CPJ] Native Windows CPJ is installed and ready.\n";
        std::cout << "[CPJ] Compile a file, for example:\n";
        std::cout << "      cpj --web-only -o generated " << shell_quote((std::filesystem::path(runtime_root) / "samples" / "web_app.cpj").string()) << "\n";
        return 0;
    }

    std::ifstream in(path);
    if (!in)
    {
        std::cerr << "Error: cannot open input file '" << path << "'\n";
        return 2;
    }

    std::ostringstream ss;
    ss << in.rdbuf();
    std::string content = ss.str();

    // Always emit backend code. If main() is present, run it.
    bool has_main = content.find("def main(") != std::string::npos || content.find("def main ") != std::string::npos;
    std::cout << "[CPJ] Code generation complete for '" << path << "'.\n";
    std::string input_name = path.substr(path.find_last_of("/\\") + 1);
    std::string py_out_dir = out_dir + "/python";
    std::string py_out_file = py_out_dir + "/" + input_name + ".py";
    if (emit_python)
    {
        ensure_dir(py_out_dir);
        // Call the Python emitter to generate backend code
        // Ensure Python can import the tools package when invoked from the repo root
        std::string emit_cmd = python_module_command("tools.cpj_emitter", {path, "-o", py_out_file}, runtime_root);
        int emit_rc = run_cmd(emit_cmd, verbose);
        if (emit_rc != 0)
        {
            std::cerr << "[CPJ] Error: Python emitter failed.\n";
            return 3;
        }
        std::cout << "[CPJ] Python backend emitted: " << py_out_file << "\n";
    }
    if (emit_web)
    {
        std::string web_out_dir = out_dir + "/web";
        std::string web_out_file = web_out_dir + "/" + input_name + ".html";
        std::string web_project_dir = web_out_dir + "/" + input_name + "_project";
        ensure_dir(web_out_dir);
        std::string web_cmd = python_module_command("tools.cpj_web_emitter", {path, "-o", web_out_file, "--project-dir", web_project_dir}, runtime_root);
        int web_rc = run_cmd(web_cmd, verbose);
        if (web_rc != 0)
        {
            std::cerr << "[CPJ] Error: standalone web emitter failed.\n";
            return 5;
        }
        std::cout << "[CPJ] Standalone web backend emitted: " << web_out_file << "\n";
        std::cout << "[CPJ] Standalone web project emitted: " << web_project_dir << "\n";
    }
    if (has_main && emit_python)
    {
        std::cout << "[CPJ] Detected main() entry point. Running generated Python code...\n";
#ifdef _WIN32
        int rc = run_cmd("python " + shell_quote(py_out_file), true);
#else
        int rc = run_cmd("python3 " + shell_quote(py_out_file), true);
#endif
        if (rc != 0)
        {
            std::cerr << "[CPJ] Error running generated Python code.\n";
            return 4;
        }
    }
    else if (has_main)
    {
        std::cout << "[CPJ] Detected main() entry point, but Python emission is disabled.\n";
    }
    else
    {
        std::cout << "[CPJ] No main() entry point found.\n";
    }
    return 0;
}
