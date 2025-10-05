// cpj_main.cpp
// Main entry for CPJ: calls C++, Python, and Java modules
#include <iostream>
#include <cstdlib>

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        std::cout << "Usage: ./cpj_main <language> <source_file>" << std::endl;
        std::cout << "Languages: cpp, python, java" << std::endl;
        return 1;
    }
    std::string lang = argv[1];
    std::string source_file = argv[2];
    if (lang == "cpp")
    {
        std::string cmd = "./cpj_cpp " + source_file;
        system(cmd.c_str());
    }
    else if (lang == "python")
    {
        std::string cmd = "python3 python/cpj_python.py " + source_file;
        system(cmd.c_str());
    }
    else if (lang == "java")
    {
        std::string cmd = "java -cp java CPJJava " + source_file;
        system(cmd.c_str());
    }
    else
    {
        std::cout << "Unsupported language." << std::endl;
        return 2;
    }
    return 0;
}
