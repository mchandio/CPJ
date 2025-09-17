// cpj_cpp.h
// Header for CPJ C++ compiler module
#ifndef CPJ_CPP_H
#define CPJ_CPP_H

#include <string>

bool compile_cpp(const std::string &source_file, const std::string &output_file);
bool run_cpp(const std::string &output_file);

#endif // CPJ_CPP_H
