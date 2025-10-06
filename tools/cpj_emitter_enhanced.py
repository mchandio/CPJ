"""
Enhanced CPJ -> Python Emitter with support for C++/Java style syntax
Handles mixed-language features including arrays, semicolons, and static typing
"""
import sys
import re
from typing import List, Dict, Optional, Any
from tools.cpj_parser import Module, ClassDef, FuncDef, Print, Assign, Return, Call, Str, Num, Var, BinOp, GUIBlock, If, UnaryOp, Compare, BoolOp, parse_file, parse_expr_text

class Emitter:
    def __init__(self):
        self.lines = []
        self._btn_counter = 0
        self.imports = set()
        self.type_imports = {
            'List': 'typing.List',
            'Dict': 'typing.Dict',
            'Optional': 'typing.Optional',
        }
        
    def emit(self, node, indent=0):
        method = getattr(self, f'emit_{node.__class__.__name__}', None)
        if method:
            method(node, indent)
        else:
            self.emit_comment(f"Unsupported node: {node}", indent)

    def emit_Module(self, node, indent=0):
        # Add necessary imports
        if self.imports:
            for imp in sorted(self.imports):
                self.lines.append(f'import {imp}')
            self.lines.append('')
        
        for it in node.items:
            self.emit(it, indent)
        
        # Auto-invoke main if present
        main_func = any(isinstance(it, FuncDef) and it.name == 'main' for it in node.items)
        main_class = None
        for it in node.items:
            if isinstance(it, ClassDef):
                for m in it.methods:
                    if m.name == 'main':
                        main_class = it.name
                        break
            if main_class:
                break
        
        if main_func or main_class:
            self.lines.append("")
            self.lines.append("if __name__ == '__main__':")
            if main_func:
                self.lines.append("    main()")
            else:
                self.lines.append(f"    {main_class}.main()")

    def emit_ClassDef(self, node, indent=0):
        self.lines.append("" if indent == 0 else "\n")
        class_line = "    " * indent + f"class {node.name}"
        if node.bases:
            class_line += f"({', '.join(node.bases)})"
        self.lines.append(class_line + ":")
        
        # Handle constructor
        has_constructor = any(m.name == '__init__' for m in node.methods)
        if not has_constructor and node.fields:
            self.emit_default_constructor(node, indent + 1)
        
        # Emit methods
        for method in node.methods:
            self.emit(method, indent + 1)
            
    def emit_default_constructor(self, node, indent):
        self.lines.append("    " * indent + "def __init__(self):")
        for field in node.fields:
            self.lines.append("    " * (indent + 1) + f"self.{field.name} = None")
            
    def emit_ArrayExpr(self, node, indent=0):
        elements = []
        for elem in node.elements:
            elements.append(self.emit_expr(elem))
        return f"[{', '.join(elements)}]"
        
    def emit_ArrayAccess(self, node, indent=0):
        array = self.emit_expr(node.array)
        index = self.emit_expr(node.index)
        return f"{array}[{index}]"
        
    def emit_TypeRef(self, node):
        if node.is_array:
            elem_type = self.emit_TypeRef(node.element_type)
            self.imports.add('List')
            return f"List[{elem_type}]"
        return node.name

    def get_output(self) -> str:
        return "\n".join(self.lines)