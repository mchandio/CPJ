// cpj_cpp_utils.cpp
// Utility functions for CPJ C++ compiler module
#include "cpj_cpp.h"
#include <cstdlib>
#include <iostream>

bool compile_cpp(const std::string &source_file, const std::string &output_file)
{
    std::string compile_cmd = "g++ " + source_file + " -o " + output_file;
    int result = system(compile_cmd.c_str());
    if (result != 0)
    {
        std::cerr << "Compilation failed." << std::endl;
        return false;
    }
    std::cout << "Compilation successful." << std::endl;
    return true;
}

bool run_cpp(const std::string &output_file)
{
    int result = system(("./" + output_file).c_str());
    return result == 0;
}
