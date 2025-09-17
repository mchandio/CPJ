"""
Simple AST -> C++ emitter for CPJ subset (StructDef, ClassDef)
Generates C++ source as a string.
"""
from tools.cpj_parser import StructDef, ClassDef, FuncDef
from typing import List

class CppEmitter:
    def __init__(self):
        self.lines: List[str] = []

    def emit(self, node):
        method = getattr(self, f'emit_{node.__class__.__name__}', None)
        if method:
            method(node)
        else:
            self.lines.append(f"// Unsupported node: {node}")

    def emit_StructDef(self, node: StructDef):
        self.lines.append(f"struct {node.name} {{")
        for name, typ in node.fields:
            self.lines.append(f"    {self.cpp_type(typ)} {name};")
        self.lines.append("};\n")

    def emit_ClassDef(self, node: ClassDef):
        self.lines.append(f"class {node.name} {{")
        self.lines.append("public:")
        for name, typ in node.fields:
            self.lines.append(f"    {self.cpp_type(typ)} {name};")
        for m in node.methods:
            self.emit_FuncDef(m)
        self.lines.append("};\n")

    def emit_FuncDef(self, node: FuncDef):
        # For demo: emit as void method with no body
        args = ', '.join(f"{self.cpp_type('int')} {a}" for a in node.args if a)
        self.lines.append(f"    void {node.name}({args}) {{ /* ... */ }}")

    def cpp_type(self, typ):
        # Map CPJ types to C++ types
        mapping = {'int': 'int', 'float': 'double', 'str': 'std::string', 'string': 'std::string', 'bool': 'bool'}
        return mapping.get(typ, 'auto')

    def to_source(self):
        return '\n'.join(self.lines) + '\n'
