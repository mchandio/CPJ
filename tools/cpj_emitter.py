"""
CPJ -> Python Emitter (robust, extensible, clean)
Emits all statements in main(), handles method args/bodies, easy to extend.
"""
import sys
import re
from tools.cpj_parser import Module, ClassDef, FuncDef, Print, Assign, AugAssign, Return, Call, Str, Num, Var, BinOp, GUIBlock, If, While, For, List, UnaryOp, Compare, BoolOp, Try, ExceptHandler, Raise, Dict, Lambda, ListComp, DictComp, Subscript, Attribute, With, Import, ImportFrom, parse_file, parse_expr_text

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

    def emit_comment(self, text, indent=0):
        self.lines.append("    " * indent + f"# {text}")

    def emit_Module(self, node, indent=0):
        # Check if we need to add stdlib path
        has_cpj_imports = any(
            isinstance(it, (Import, ImportFrom)) and
            (it.module in ['Math', 'String', 'File', 'JSON', 'System'] if isinstance(it, Import) else
             it.module in ['Math', 'String', 'File', 'JSON', 'System'])
            for it in node.items
        )

        if has_cpj_imports:
            # Add stdlib to path
            self.lines.append('import sys')
            self.lines.append('import os')
            self.lines.append('# Add CPJ stdlib to path')
            self.lines.append('_cpj_file = os.path.abspath(__file__)')
            self.lines.append('_cpj_generated = os.path.dirname(_cpj_file)')
            self.lines.append('_cpj_root = os.path.dirname(os.path.dirname(_cpj_generated))')
            self.lines.append('_cpj_stdlib = os.path.join(_cpj_root, "stdlib")')
            self.lines.append('if _cpj_stdlib not in sys.path:')
            self.lines.append('    sys.path.insert(0, _cpj_stdlib)')
            self.lines.append('')

        # Emit import statements
        for it in node.items:
            if isinstance(it, (Import, ImportFrom)):
                self.emit(it, indent)

        # Add blank line after imports if there were any
        has_imports = any(isinstance(it, (Import, ImportFrom)) for it in node.items)
        if has_imports:
            self.lines.append('')

        # Add necessary internal imports
        regular_imports = sorted(imp for imp in self.imports if imp not in self.type_imports)
        if regular_imports:
            for imp in regular_imports:
                self.lines.append(f'import {imp}')
            self.lines.append('')

        # Emit non-import items
        for it in node.items:
            if not isinstance(it, (Import, ImportFrom)):
                self.emit(it, indent)

        # Emit type imports if needed
        type_names = sorted(t for t in self.imports if t in self.type_imports)
        if type_names:
            self.lines.insert(0, f"from typing import {', '.join(type_names)}")

        # After emitting all top-level items, auto-invoke main if present.
        # Prefer a top-level function `main()`; otherwise call a class `main` as a static method.
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
                # call class main as staticmethod to avoid injecting 'self'
                self.lines.append(f"    {main_class}.main()")

    def emit_ClassDef(self, node, indent=0):
        self.lines.append("    " * indent + f"class {node.name}:")
        if not hasattr(node, 'methods') or not node.methods:
            self.lines.append("    " * (indent+1) + "pass")
            return
        for m in node.methods:
            # If a method has no args, emit it as a @staticmethod so calling
            # <Class>.main() won't receive an implicit 'self' and won't error.
            method_args = getattr(m, 'args', None)
            if not method_args:
                self.lines.append("    " * (indent+1) + "@staticmethod")
                args = ''
            else:
                # Instance methods need 'self' as first parameter
                args = 'self, ' + ', '.join(method_args)
            # emit method signature
            self.lines.append("    " * (indent+1) + f"def {m.name}({args}):")
            if not getattr(m, 'body', None):
                self.lines.append("    " * (indent+2) + "pass")
            else:
                for stmt in m.body:
                    # emit statements inside method body with increased indent
                    self.emit_statement(stmt, indent+2)

    def emit_FuncDef(self, node, indent=0):
        args = ', '.join(node.args)
        self.lines.append("    " * indent + f"def {node.name}({args}):")
        if not hasattr(node, 'body') or not node.body:
            self.lines.append("    " * (indent+1) + "pass")
        else:
            for stmt in node.body:
                self.emit_statement(stmt, indent+1)

    def emit_Print(self, node, indent=0):
        if isinstance(node.expr, list):
            args = ', '.join(self.emit_expr(e) for e in node.expr)
            self.lines.append("    " * indent + f"print({args})")
        else:
            self.lines.append("    " * indent + f"print({self.emit_expr(node.expr)})")

    def emit_Assign(self, node, indent=0):
        self.lines.append("    " * indent + f"{node.target} = {self.emit_expr(node.expr)}")

    def emit_AugAssign(self, node, indent=0):
        self.lines.append("    " * indent + f"{node.target} {node.op}= {self.emit_expr(node.expr)}")

    def emit_Return(self, node, indent=0):
        self.lines.append("    " * indent + f"return {self.emit_expr(node.expr)}")

    def emit_If(self, node, indent=0):
        self.lines.append("    " * indent + f"if {self.emit_expr(node.test)}:")
        if not node.body:
            self.lines.append("    " * (indent+1) + "pass")
        else:
            for stmt in node.body:
                self.emit_statement(stmt, indent+1)
        if node.orelse:
            self.lines.append("    " * indent + "else:")
            for stmt in node.orelse:
                self.emit_statement(stmt, indent+1)

    def emit_While(self, node, indent=0):
        self.lines.append("    " * indent + f"while {self.emit_expr(node.test)}:")
        if not node.body:
            self.lines.append("    " * (indent+1) + "pass")
        else:
            for stmt in node.body:
                self.emit_statement(stmt, indent+1)

    def emit_For(self, node, indent=0):
        self.lines.append("    " * indent + f"for {node.target} in {self.emit_expr(node.iter_expr)}:")
        if not node.body:
            self.lines.append("    " * (indent+1) + "pass")
        else:
            for stmt in node.body:
                self.emit_statement(stmt, indent+1)

    def emit_Try(self, node, indent=0):
        self.lines.append("    " * indent + "try:")
        if not node.body:
            self.lines.append("    " * (indent+1) + "pass")
        else:
            for stmt in node.body:
                self.emit_statement(stmt, indent+1)

        for handler in node.handlers:
            if handler.type and handler.name:
                self.lines.append("    " * indent + f"except {handler.type} as {handler.name}:")
            elif handler.type:
                self.lines.append("    " * indent + f"except {handler.type}:")
            else:
                self.lines.append("    " * indent + "except:")

            if not handler.body:
                self.lines.append("    " * (indent+1) + "pass")
            else:
                for stmt in handler.body:
                    self.emit_statement(stmt, indent+1)

        if node.finalbody:
            self.lines.append("    " * indent + "finally:")
            for stmt in node.finalbody:
                self.emit_statement(stmt, indent+1)

    def emit_Raise(self, node, indent=0):
        if node.exc:
            self.lines.append("    " * indent + f"raise {self.emit_expr(node.exc)}")
        else:
            self.lines.append("    " * indent + "raise")

    def emit_With(self, node, indent=0):
        # Emit with statement
        items = []
        for context_expr, var_name in node.items:
            expr_str = self.emit_expr(context_expr)
            if var_name:
                items.append(f"{expr_str} as {var_name}")
            else:
                items.append(expr_str)

        self.lines.append("    " * indent + f"with {', '.join(items)}:")

        if not node.body:
            self.lines.append("    " * (indent+1) + "pass")
        else:
            for stmt in node.body:
                self.emit_statement(stmt, indent+1)

    def emit_Import(self, node, indent=0):
        # Map CPJ module names to stdlib modules
        cpj_modules = {
            'Math': 'cpj_math',
            'String': 'cpj_string',
            'File': 'cpj_file',
            'JSON': 'cpj_json',
            'System': 'cpj_system'
        }

        module = node.module
        if module in cpj_modules:
            # Import from CPJ stdlib
            real_module = cpj_modules[module]
            if node.alias:
                self.lines.append("    " * indent + f"from {real_module} import {module} as {node.alias}")
            else:
                self.lines.append("    " * indent + f"from {real_module} import {module}")
        else:
            if node.alias:
                self.lines.append("    " * indent + f"import {module} as {node.alias}")
            else:
                self.lines.append("    " * indent + f"import {module}")

    def emit_ImportFrom(self, node, indent=0):
        # Map CPJ module names to stdlib modules
        cpj_modules = {
            'Math': 'cpj_math',
            'String': 'cpj_string',
            'File': 'cpj_file',
            'JSON': 'cpj_json',
            'System': 'cpj_system'
        }

        module = node.module
        if module in cpj_modules:
            module = cpj_modules[module]

        # Build import list with aliases
        items = []
        for name in node.names:
            if name in node.aliases:
                items.append(f"{name} as {node.aliases[name]}")
            else:
                items.append(name)

        imports_str = ', '.join(items)
        self.lines.append("    " * indent + f"from {module} import {imports_str}")

    def emit_Call(self, node, indent=0):
        self.lines.append("    " * indent + self.emit_expr(node))

    def emit_statement(self, node, indent=0):
        method = getattr(self, f'emit_{node.__class__.__name__}', None)
        if method:
            method(node, indent)
        else:
            self.emit_comment(f"stmt {node}", indent)

    def emit_expr(self, expr):
        if isinstance(expr, Str):
            return repr(expr.s)
        if isinstance(expr, Num):
            return repr(expr.v)
        if isinstance(expr, Var):
            return expr.name
        if isinstance(expr, BinOp):
            left = self.emit_expr(expr.left)
            right = self.emit_expr(expr.right)
            return f"({left} {expr.op} {right})"
        if isinstance(expr, UnaryOp):
            op = expr.op
            val = self.emit_expr(expr.operand)
            return f"({op}{val})"
        if isinstance(expr, Compare):
            # support chained comparisons
            left = self.emit_expr(expr.left)
            parts = []
            for o, c in zip(expr.ops, expr.comparators):
                parts.append(f"{o} {self.emit_expr(c)}")
            return f"({left} {' '.join(parts)})"
        if isinstance(expr, BoolOp):
            vals = [self.emit_expr(v) for v in expr.values]
            return '(' + f" {expr.op} ".join(vals) + ')'
        if isinstance(expr, List):
            elements = [self.emit_expr(e) for e in expr.elements]
            return '[' + ', '.join(elements) + ']'
        if isinstance(expr, Call):
            func = self.emit_expr(expr.func)
            args = ', '.join(self.emit_expr(a) for a in expr.args)
            return f"{func}({args})"
        if isinstance(expr, Dict):
            items = []
            for k, v in zip(expr.keys, expr.values):
                items.append(f"{self.emit_expr(k)}: {self.emit_expr(v)}")
            return '{' + ', '.join(items) + '}'
        if isinstance(expr, Lambda):
            args = ', '.join(expr.args)
            body = self.emit_expr(expr.body)
            return f"lambda {args}: {body}"
        if isinstance(expr, ListComp):
            elt = self.emit_expr(expr.elt)
            parts = []
            for var, iter_expr in expr.generators:
                parts.append(f"for {var} in {self.emit_expr(iter_expr)}")
            return f"[{elt} {' '.join(parts)}]"
        if isinstance(expr, DictComp):
            key = self.emit_expr(expr.key)
            value = self.emit_expr(expr.value)
            parts = []
            for var, iter_expr in expr.generators:
                parts.append(f"for {var} in {self.emit_expr(iter_expr)}")
            return f"{{{key}: {value} {' '.join(parts)}}}"
        if isinstance(expr, Subscript):
            value = self.emit_expr(expr.value)
            slice_expr = self.emit_expr(expr.slice)
            return f"{value}[{slice_expr}]"
        if isinstance(expr, Attribute):
            value = self.emit_expr(expr.value)
            return f"{value}.{expr.attr}"
        return repr(expr)

    def gui_emit_expr(self, expr, use_arg_vars: bool = False):
        # Like emit_expr but turns bare Vars into widget accesses (widgets['name'].get())
        # If use_arg_vars is True, Vars are emitted as __var_<name> (prepared by handler)
        if isinstance(expr, Str):
            return repr(expr.s)
        if isinstance(expr, Num):
            return repr(expr.v)
        if isinstance(expr, Var):
            name = expr.name
            if use_arg_vars:
                return f"__var_{name}"
            return f"widgets['{name}'].get()"
        if isinstance(expr, BinOp):
            left = self.gui_emit_expr(expr.left, use_arg_vars=use_arg_vars)
            right = self.gui_emit_expr(expr.right, use_arg_vars=use_arg_vars)
            return f"({left} {expr.op} {right})"
        if hasattr(expr, 'ops') and hasattr(expr, 'comparators'):
            # Compare node
            left = self.gui_emit_expr(expr.left, use_arg_vars=use_arg_vars)
            parts = [left]
            for o, c in zip(expr.ops, expr.comparators):
                r = self.gui_emit_expr(c, use_arg_vars=use_arg_vars)
                parts.append(f"{o} {r}")
            return '(' + ' '.join(parts) + ')'
        if hasattr(expr, 'op') and hasattr(expr, 'values'):
            # BoolOp
            vals = [self.gui_emit_expr(v, use_arg_vars=use_arg_vars) for v in expr.values]
            return '(' + f" {expr.op} ".join(vals) + ')'
        if hasattr(expr, 'op') and hasattr(expr, 'operand'):
            # UnaryOp
            op = expr.op
            val = self.gui_emit_expr(expr.operand, use_arg_vars=use_arg_vars)
            return f"({op}{val})"
        if isinstance(expr, Call):
            # for calls, ensure function name is emitted normally (not as a widget access)
            if isinstance(expr.func, Var):
                func = self.emit_expr(expr.func)
            else:
                func = self.gui_emit_expr(expr.func, use_arg_vars=use_arg_vars)
            args = ', '.join(self.gui_emit_expr(a, use_arg_vars=use_arg_vars) for a in expr.args)
            return f"{func}({args})"
        return repr(expr)

    def to_source(self):
        return '\n'.join(self.lines) + '\n'

    def emit_GUIBlock(self, node, indent=0):
        # Ensure tkinter import and runtime scaffolding at top if not present
        self.lines.append("import tkinter")
        self.lines.append("")
        # lightweight widget variable to avoid requiring a Tk root at import time
        self.lines.append("class _WidgetVar:")
        self.lines.append("    def __init__(self, value=''):")
        self.lines.append("        self._v = value")
        self.lines.append("    def set(self, v):")
        self.lines.append("        self._v = v")
        self.lines.append("    def get(self):")
        self.lines.append("        return self._v")
        self.lines.append("")
        self.lines.append("# widgets container for GUI elements")
        self.lines.append("widgets = {}")
        self.lines.append("widget_types = {}")
        self.lines.append("_data = {}")
        self.lines.append("")
        # helpers
        self.lines.append("def invoke_or_emit_event(cb):")
        self.lines.append("    # helper to call callbacks; in emitted tests we call handlers directly")
        self.lines.append("    cb()")
        self.lines.append("")
        # process lines; each line is a string from parser
        i = 0
        while i < len(node.lines):
            ln = node.lines[i]
            i += 1
            if not ln: continue
            # handle multiline dict first: 'types {'
            if ln.startswith('types {') or ln.startswith('types{') or ln == 'types {':
                # collect subsequent lines until '}' and parse entries
                buf = ''
                if '{' in ln:
                    rest = ln[ln.find('{')+1:]
                    if '}' in rest:
                        # content and closing brace on same line
                        buf = rest[:rest.find('}')]
                    else:
                        buf += rest
                        while i < len(node.lines):
                            nextln = node.lines[i].strip()
                            i += 1
                            if nextln == '}':
                                break
                            buf += nextln
                for entry in buf.split(','):
                    entry = entry.strip()
                    if not entry: continue
                    # expect entries like "\"x\": \"int\"" or 'x': 'int'
                    if re.match(r"^\s*['\"].+['\"]\s*:\s*['\"].+['\"]\s*$", entry):
                        k, v = entry.split(':', 1)
                        k = k.strip().strip('"').strip("'")
                        v = v.strip().strip('"').strip("'")
                        self.lines.append(f"widget_types['{k}'] = '{v}'")
                    else:
                        # emit a diagnostic comment so tests can detect ignored entries
                        self.lines.append(f"# types: ignored entry: {entry}")
                continue
            # token-style types line: 'types a:int b:bool'
            if ln.startswith('types '):
                rest = ln[len('types '):].strip()
                for part in rest.split():
                    if ':' in part:
                        k, v = part.split(':', 1)
                        k = k.strip()
                        v = v.strip()
                        self.lines.append(f"widget_types['{k}'] = '{v}'")
                continue
            # handle addTextField("name")
            if ln.startswith('addTextField'):
                m = re.match(r"addTextField\s*\(\s*([\'\"]([^\'\"]+)[\'\"])\s*(?:,\s*([\'\"]([^\'\"]+)[\'\"]))?\s*\)", ln)
                if m:
                    name = m.group(2)
                    ptype = m.group(4)
                    self.lines.append(f"widgets['{name}'] = _WidgetVar()")
                    if ptype:
                        self.lines.append(f"widget_types['{name}'] = '{ptype}'")
                else:
                    # fallback naive parse
                    args = ln[ln.find('(')+1:ln.rfind(')')]
                    name = args.split(',')[0].strip().strip('"').strip("'")
                    self.lines.append(f"widgets['{name}'] = _WidgetVar()")
                self.lines.append(f"# Entry widget placeholder for {name}")
                continue
            # handle addLabel
            if ln.startswith('addLabel'):
                self.lines.append(f"# label: {ln}")
                continue
            if ln.startswith('addCheckbox'):
                m = re.match(r"addCheckbox\s*\(\s*([\'\"]([^\'\"]+)[\'\"])\s*(?:,\s*([\'\"]([^\'\"]+)[\'\"]))?\s*\)", ln)
                if m:
                    name = m.group(2)
                    typeann = m.group(4)
                    self.lines.append(f"widgets['{name}'] = _WidgetVar(False)")
                    if typeann:
                        self.lines.append(f"widget_types['{name}'] = '{typeann}'")
                else:
                    args = ln[ln.find('(')+1:ln.rfind(')')]
                    name = args.split(',')[0].strip().strip('"').strip("'")
                    self.lines.append(f"widgets['{name}'] = _WidgetVar(False)")
                self.lines.append(f"# Checkbox placeholder for {name}")
                continue
            if ln.startswith('addSlider'):
                m = re.match(r"addSlider\s*\(\s*([\'\"]([^\'\"]+)[\'\"])\s*(?:,\s*([\'\"]([^\'\"]+)[\'\"]))?\s*\)", ln)
                if m:
                    name = m.group(2)
                    typeann = m.group(4)
                    self.lines.append(f"widgets['{name}'] = _WidgetVar(0)")
                    if typeann:
                        self.lines.append(f"widget_types['{name}'] = '{typeann}'")
                else:
                    args = ln[ln.find('(')+1:ln.rfind(')')]
                    name = args.split(',')[0].strip().strip('"').strip("'")
                    self.lines.append(f"widgets['{name}'] = _WidgetVar(0)")
                self.lines.append(f"# Slider placeholder for {name}")
                continue
            # handle addButton("Label", handler?)
            if ln.startswith('addButton'):
                mstart = ln.find('(')
                mend = ln.rfind(')')
                args = ln[mstart+1:mend]
                parts = []
                cur = ''
                depth = 0
                in_str = False
                esc = False
                for ch in args:
                    if in_str:
                        cur += ch
                        if esc:
                            esc = False
                        elif ch == '\\':
                            esc = True
                        elif ch == '"' or ch == "'":
                            in_str = False
                    else:
                        if ch == '"' or ch == "'":
                            in_str = True
                        elif ch in '([':
                            depth += 1
                            cur += ch
                        elif ch in ')]':
                            depth -= 1
                            cur += ch
                        elif ch == ',' and depth == 0:
                            parts.append(cur.strip())
                            cur = ''
                        else:
                            cur += ch
                if cur.strip(): parts.append(cur.strip())
                label = parts[0].strip().strip('"').strip("'") if parts else f'btn{self._btn_counter}'
                handler_expr = None
                if len(parts) > 1:
                    try:
                        handler_expr = parse_expr_text(parts[1])
                    except Exception:
                        handler_expr = None
                # create handler function
                hname = f"_on_click_{self._btn_counter}"
                self._btn_counter += 1
                self.lines.append(f"def {hname}():")
                self.lines.append(f"    # generated handler for button {label}")
                if handler_expr is not None and isinstance(handler_expr, Call):
                    # prepare var collection for coercion
                    varnames = set()
                    def collect_vars(e):
                        if isinstance(e, Var):
                            varnames.add(e.name)
                        elif isinstance(e, Call):
                            # do not collect the function name itself as a variable
                            for a in e.args:
                                collect_vars(a)
                        elif isinstance(e, BinOp):
                            collect_vars(e.left); collect_vars(e.right)
                        elif hasattr(e, 'left') and hasattr(e, 'comparators'):
                            # Compare
                            collect_vars(e.left)
                            for c in e.comparators: collect_vars(c)
                        elif hasattr(e, 'values'):
                            for v in e.values: collect_vars(v)
                        elif hasattr(e, 'operand'):
                            collect_vars(e.operand)
                    collect_vars(handler_expr)
                    for vn in sorted(varnames):
                        self.lines.append(f"    __var_{vn} = widgets.get('{vn}').get()")
                        # try simple numeric coercion when value is a string
                        self.lines.append(f"    try:")
                        self.lines.append(f"        if isinstance(__var_{vn}, str):")
                        self.lines.append(f"            if __var_{vn}.isdigit(): __var_{vn} = int(__var_{vn})")
                        self.lines.append(f"            else:")
                        self.lines.append(f"                try:")
                        self.lines.append(f"                    __var_{vn} = float(__var_{vn})")
                        self.lines.append(f"                except: pass")
                        self.lines.append(f"    except Exception:")
                        self.lines.append(f"        _data.setdefault('_coercion_errors', []).append('{vn}')")
                    # emit call using prepared __var_ names
                    call_src = self.gui_emit_expr(handler_expr, use_arg_vars=True)
                    self.lines.append(f"    {call_src}")
                else:
                    # fallback: emit a pass or try to emit expression
                    if handler_expr is not None:
                        call_src = self.gui_emit_expr(handler_expr)
                        self.lines.append(f"    {call_src}")
                    else:
                        self.lines.append("    pass")
                # expose handler name and create a Button widget placeholder
                btn_key = f"btn{self._btn_counter-1}"
                self.lines.append(f"widgets['{btn_key}'] = tkinter.Button(text={repr(label)})")
                self.lines.append(f"# wire button {label} -> {hname}")
                self.lines.append(f"widgets['{btn_key}'].configure(command={hname})")
                continue
            # handle show()
            if ln.strip() == 'show()' or ln.strip() == 'show':
                self.lines.append("# GUI show() called - runtime would start mainloop")
                continue
            # unrecognized lines: comment them
            self.lines.append(f"# GUI line: {ln}")

# --- CLI entrypoint ---
def main():
    import argparse
    parser = argparse.ArgumentParser(description="CPJ -> Python emitter")
    parser.add_argument('input', help='Input .cpj file')
    parser.add_argument('-o', '--output', help='Output .py file', required=True)
    args = parser.parse_args()

    try:
        ast_root = parse_file(args.input)
    except Exception as e:
        print(f"[Emitter] Error parsing input: {e}", file=sys.stderr)
        sys.exit(1)

    emitter = Emitter()
    emitter.emit(ast_root)
    py_code = emitter.to_source()

    try:
        with open(args.output, 'w') as f:
            f.write(py_code)
    except Exception as e:
        print(f"[Emitter] Error writing output: {e}", file=sys.stderr)
        sys.exit(2)

    print(f"[Emitter] Python code emitted to {args.output}")

if __name__ == "__main__":
    main()
