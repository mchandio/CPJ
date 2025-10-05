
#include <iostream>
#include "code_analyzer.h"

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <input_file.cpj>\n";
        return 1;
    }

    CodeAnalyzer analyzer;
    analyzer.processFile(argv[1]);
    return 0;
}
