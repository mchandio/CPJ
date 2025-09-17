"""
Simple AST -> Java emitter for CPJ subset (StructDef, ClassDef)
Generates Java source as a string.
"""
from tools.cpj_parser import StructDef, ClassDef, FuncDef
from typing import List

class JavaEmitter:
    def __init__(self):
        self.lines: List[str] = []

    def emit(self, node):
        method = getattr(self, f'emit_{node.__class__.__name__}', None)
        if method:
            method(node)
        else:
            self.lines.append(f"// Unsupported node: {node}")

    def emit_StructDef(self, node: StructDef):
        self.lines.append(f"public class {node.name} {{")
        for name, typ in node.fields:
            self.lines.append(f"    public {self.java_type(typ)} {name};")
        self.lines.append("}")

    def emit_ClassDef(self, node: ClassDef):
        self.lines.append(f"public class {node.name} {{")
        for name, typ in node.fields:
            self.lines.append(f"    public {self.java_type(typ)} {name};")
        # Emit methods
        for m in node.methods:
            self.emit_FuncDef(m)
        self.lines.append("}")

    def emit_FuncDef(self, node: FuncDef):
        # For demo: emit as void method with no body
        args = ', '.join(f"{self.java_type('int')} {a}" for a in node.args if a)
        self.lines.append(f"    public void {node.name}({args}) {{ /* ... */ }}")

    def java_type(self, typ):
        mapping = {'int': 'int', 'float': 'double', 'str': 'String', 'string': 'String', 'bool': 'boolean'}
        return mapping.get(typ, 'Object')

    def to_source(self):
        return '\n'.join(self.lines) + '\n'
