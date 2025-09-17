// cpj_lexer.h
// Lexer for CPJ language
#ifndef CPJ_LEXER_H
#define CPJ_LEXER_H
#include <string>
#include <vector>
#include <regex>

struct Token
{
    std::string type;
    std::string value;
};

class CPJLexer
{
public:
    std::vector<Token> tokenize(const std::string &source)
    {
        std::vector<Token> tokens;
        std::regex word_regex("[A-Za-z_][A-Za-z0-9_]*|[0-9]+|[{}();=+*/<>-]|");
        auto words_begin = std::sregex_iterator(source.begin(), source.end(), word_regex);
        auto words_end = std::sregex_iterator();
        for (std::sregex_iterator i = words_begin; i != words_end; ++i)
        {
            std::string val = (*i).str();
            tokens.push_back({"TOKEN", val});
        }
        return tokens;
    }
};

#endif // CPJ_LEXER_H
