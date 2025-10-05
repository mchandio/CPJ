#pragma once
#include <string>
#include <vector>
#include <memory>
#include <nlohmann/json.hpp>

namespace cpj::lsp {

struct Position {
    int line;
    int character;
};

struct Range {
    Position start;
    Position end;
};

struct Location {
    std::string uri;
    Range range;
};

struct Diagnostic {
    Range range;
    std::string message;
    int severity;
};

class LanguageServer {
public:
    static LanguageServer& instance();
    
    // LSP protocol implementation
    void initialize(const std::string& rootUri);
    void shutdown();
    void exit();
    
    // Document management
    void didOpen(const std::string& uri, const std::string& text);
    void didChange(const std::string& uri, const std::vector<std::string>& changes);
    void didClose(const std::string& uri);
    
    // Language features
    std::vector<Location> getDefinition(const std::string& uri, Position position);
    std::vector<Location> getReferences(const std::string& uri, Position position);
    std::vector<Diagnostic> getDiagnostics(const std::string& uri);
    nlohmann::json getCompletion(const std::string& uri, Position position);
    
    // Cross-language features
    std::vector<Location> getCrossLanguageReferences(const std::string& uri, Position position);
    nlohmann::json getSymbolInfo(const std::string& uri, Position position);

private:
    LanguageServer() = default;
    std::string rootUri;
};

} // namespace cpj::lsp