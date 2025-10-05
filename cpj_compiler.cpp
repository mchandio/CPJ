// Improved cpj_compiler.cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <sys/stat.h>
#include <sys/types.h>

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

static void ensure_dir(const std::string &d)
{
    if (d.empty())
        return;
    std::string cmd = "mkdir -p '" + d + "'";
    std::system(cmd.c_str());
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
