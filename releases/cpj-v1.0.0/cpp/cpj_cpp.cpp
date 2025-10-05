// CPJ C++ Module
// Handles C++ code parsing, compilation, and execution

#include "cpj_cpp.h"
#include <iostream>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: cpj_cpp <source_file.cpp>" << std::endl;
        return 1;
    }
    std::string source_file = argv[1];
    std::string output_file = "a.out";
    if (!compile_cpp(source_file, output_file))
    {
        return 2;
    }
    std::cout << "Running program..." << std::endl;
    if (!run_cpp(output_file))
    {
        return 3;
    }
    return 0;
}
