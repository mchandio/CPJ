# CPJ IDE Integration

## Features
- Intelligent code completion (LSP)
- Real-time error detection (diagnostics)
- Cross-language navigation
- Debugging hooks (planned)
- Performance profiling (planned)

## Usage
1. Install [pygls](https://pypi.org/project/pygls/):
   ```bash
   pip install pygls
   ```
2. Start the LSP server:
   ```bash
   python3 tools/cpj_lsp_server.py
   ```
3. Connect your IDE (VS Code, etc.) to the server using LSP protocol.

## Roadmap
- Integrate with CPJ compiler for completions
- Integrate with semantic analyzer for diagnostics
- Add debugging and profiling support
