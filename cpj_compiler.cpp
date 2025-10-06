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

int main(int argc, char **argv)
{
    const std::string defaultPath = "samples/farmflow.cpj";

    // CLI flags
    bool emit_java = true;
    bool emit_python = true;
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
            std::cout << "Usage: cpj_compiler [options] <source.cpj>\n";
            std::cout << "  --no-java        disable Java emission\n";
            std::cout << "  --no-python      disable Python emission\n";
            std::cout << "  --no-compile     skip compilation steps (javac)\n";
            std::cout << "  --no-run         do not run generated artifacts\n";
            std::cout << "  -o, --out <dir>  output directory (default: generated)\n";
            std::cout << "  -v, --verbose    verbose logging\n";
            return 0;
        }
        else if (path.empty())
            path = a;
    }

    if (path.empty())
        path = defaultPath;

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
    std::string py_out_dir = out_dir + "/python";
    std::string py_out_file = py_out_dir + "/" + path.substr(path.find_last_of("/\\") + 1) + ".py";
    if (emit_python)
    {
        ensure_dir(py_out_dir);
        // Call the Python emitter to generate backend code
        // Ensure Python can import the tools package when invoked from the repo root
        std::string emit_cmd = "PYTHONPATH=. python3 -m tools.cpj_emitter '" + path + "' -o '" + py_out_file + "'";
        int emit_rc = run_cmd(emit_cmd, verbose);
        if (emit_rc != 0)
        {
            std::cerr << "[CPJ] Error: Python emitter failed.\n";
            return 3;
        }
        std::cout << "[CPJ] Python backend emitted: " << py_out_file << "\n";
    }
    if (has_main && emit_python)
    {
        std::cout << "[CPJ] Detected main() entry point. Running generated Python code...\n";
        int rc = run_cmd("python3 '" + py_out_file + "'", true);
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
