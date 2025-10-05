// cpj_parser.h
// Parser for CPJ language
#ifndef CPJ_PARSER_H
#define CPJ_PARSER_H
#include "cpj_lexer.h"
#include <vector>
#include <string>
#include <iostream>

class CPJParser
{
public:
    void parse(const std::vector<Token> &tokens)
    {
        for (size_t i = 0; i < tokens.size(); ++i)
        {
            const auto &token = tokens[i];
            if (token.value == "print")
            {
                std::cout << "[CPJ] Print statement detected." << std::endl;
            }
            else if (token.value == "def")
            {
                std::cout << "[CPJ] Function definition detected." << std::endl;
            }
            else if (token.value == "class")
            {
                std::cout << "[CPJ] Class definition detected." << std::endl;
            }
            else if (token.value == "GUI")
            {
                std::cout << "[CPJ] GUI creation detected." << std::endl;
            }
            else if (token.value == "addLabel")
            {
                std::cout << "[CPJ] GUI label detected." << std::endl;
            }
            else if (token.value == "addButton")
            {
                std::cout << "[CPJ] GUI button detected." << std::endl;
            }
            else if (token.value == "addTextField")
            {
                std::cout << "[CPJ] GUI text field detected." << std::endl;
            }
            else if (token.value == "onClick")
            {
                std::cout << "[CPJ] GUI onClick handler detected." << std::endl;
            }
            else if (token.value == "show")
            {
                std::cout << "[CPJ] GUI show detected." << std::endl;
            }
        }
    }
};

#endif // CPJ_PARSER_H
