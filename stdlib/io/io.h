#pragma once

#include <string>
#include <memory>
#include <iostream>
#include "../concurrent/concurrent.h"

namespace cpj::io
{

    class Path
    {
    public:
        static Path of(const std::string &path);

        bool exists() const;
        bool isDirectory() const;
        bool isFile() const;
        std::string toString() const;

        Path &resolve(const std::string &other);
        Path &normalize();
        Path &toAbsolutePath();

    private:
        std::string pathStr;
    };

    class AsyncFile
    {
    public:
        static Future<AsyncFile> open(const Path &path, const std::string &mode);

        Future<std::string> readAll();
        Future<size_t> write(const std::string &data);
        Future<void> close();

        // Language interop
        void *toPythonFile() const;
        void *toJavaPath() const;

    private:
        std::string path;
        std::string mode;
    };

    // Console IO with Unicode support
    class Console
    {
    public:
        static void print(const std::string &message);
        static void println(const std::string &message);
        static std::string readLine();
        static void setEncoding(const std::string &encoding);

        // Language interop bridges
        static void bridgePythonPrint();
        static void bridgeJavaSystemOut();
    };

} // namespace cpj::io