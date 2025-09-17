// cpj_config.h
// Modular configuration for CPJ components
#ifndef CPJ_CONFIG_H
#define CPJ_CONFIG_H

#include <string>

struct CPJConfig
{
    std::string cppModulePath = "./cpj";
    std::string javaModulePath = "bin/GUIBridge.class";
    std::string pythonModulePath = "python/cpj_python.py";
    // Add more config options as needed
};

#endif // CPJ_CONFIG_H
