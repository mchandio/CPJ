#ifndef CPJ_PLATFORM_H
#define CPJ_PLATFORM_H

#include <string>

namespace cpj
{
// Platform identification
#if defined(_WIN32) || defined(_WIN64)
#define CPJ_PLATFORM_WINDOWS
    const std::string PLATFORM = "windows";
#elif defined(__APPLE__)
#define CPJ_PLATFORM_MACOS
    const std::string PLATFORM = "macos";
#elif defined(__linux__)
#define CPJ_PLATFORM_LINUX
    const std::string PLATFORM = "linux";
#else
#error "Unsupported platform"
#endif

// Architecture identification
#if defined(__x86_64__) || defined(_M_X64)
#define CPJ_ARCH_X64
    const std::string ARCHITECTURE = "x64";
#elif defined(__i386__) || defined(_M_IX86)
#define CPJ_ARCH_X86
    const std::string ARCHITECTURE = "x86";
#elif defined(__arm__) || defined(_M_ARM)
#define CPJ_ARCH_ARM
    const std::string ARCHITECTURE = "arm";
#elif defined(__aarch64__)
#define CPJ_ARCH_ARM64
    const std::string ARCHITECTURE = "arm64";
#else
#error "Unsupported architecture"
#endif

// Platform-specific macros for machine code generation
#ifdef CPJ_PLATFORM_WINDOWS
#define CPJ_EXPORT __declspec(dllexport)
#define CPJ_IMPORT __declspec(dllimport)
#else
#define CPJ_EXPORT __attribute__((visibility("default")))
#define CPJ_IMPORT
#endif

    // Function to check platform compatibility
    inline bool is_compatible_platform()
    {
        return true; // Base compatibility check, can be extended
    }

    // Function to get target triple for LLVM
    inline std::string get_target_triple()
    {
        return ARCHITECTURE + "-" + PLATFORM;
    }
}

#endif // CPJ_PLATFORM_H