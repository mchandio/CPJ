"""
Simple AST -> Python emitter for CPJ subset (based on tools/cpj_parser AST nodes)
Generates Python source as a string.
"""
from tools.cpj_parser import Module, Print, Assign, Return, FuncDef, GUIBlock, Str, Num, Var, BinOp, Call, parse_expr_text
import ast
from typing import List


class Emitter:
    def emit_StructDef(self, node):
        # Emit a Python class with __init__ for fields
        self.lines.append(f"class {node.name}:")
        if not node.fields:
            self.lines.append("    pass")
            return
        args = ', '.join(f"{name}: {typ}" for name, typ in node.fields)
        self.lines.append(f"    def __init__(self, {args}):")
        for name, _ in node.fields:
            self.lines.append(f"        self.{name} = {name}")

    def emit_ClassDef(self, node):
        self.lines.append(f"class {node.name}:")
        if not node.fields and not node.methods:
            self.lines.append("    pass")
            return
        # Emit __init__ for fields
        if node.fields:
            args = ', '.join(f"{name}: {typ}" for name, typ in node.fields)
            self.lines.append(f"    def __init__(self, {args}):")
            for name, _ in node.fields:
                self.lines.append(f"        self.{name} = {name}")
        # Emit methods
        for m in node.methods:
            src = Emitter()
            src.emit_FuncDef(m)
            for l in src.lines:
                self.lines.append("    " + l)
    def __init__(self):
        self.lines: List[str] = []
        self.needs_tk = False

    # Top-level dispatch
    def emit(self, node):
        method = getattr(self, f'emit_{node.__class__.__name__}', None)
        if method:
            method(node)
        else:
            self.lines.append(f"# Unsupported node: {node}")

    def emit_Module(self, node: Module):
        for it in node.items:
            self.emit(it)

    def emit_Print(self, node: Print):
        if isinstance(node.expr, list):
            args = ', '.join(self.emit_expr(e) for e in node.expr)
            self.lines.append(f"print({args})")
        else:
            self.lines.append(f"print({self.emit_expr(node.expr)})")

    def emit_Assign(self, node: Assign):
        self.lines.append(f"{node.target} = {self.emit_expr(node.expr)}")

    def emit_Return(self, node: Return):
        self.lines.append(f"return {self.emit_expr(node.expr)}")

    def emit_FuncDef(self, node: FuncDef):
        args = ', '.join(a for a in node.args if a)
        self.lines.append(f"def {node.name}({args}):")
        if not node.body:
            self.lines.append("    pass")
        else:
            for b in node.body:
                for l in self.emit_statement(b):
                    self.lines.append("    " + l)

    def emit_GUIBlock(self, node: GUIBlock):
        # Generate a minimal Tkinter UI for the GUI block.
        self.needs_tk = True
        self.lines.append("import tkinter as tk")
        self.lines.append("from cpj_runtime import gather_widget_data, invoke_or_emit_event")
        self.lines.append("import warnings")
        self.lines.append("root = tk.Tk()")
        self.lines.append("widgets = {}")
        self.lines.append("widget_types = {}")

        # scan all GUI lines for block-level types declarations. Accept either:
        # - a dict literal after `types`, e.g. types {"a":"int","b":"float"}
        # - or a token list after `types`, e.g. types a:int b:float c=bool
        block_types = {}
        allowed = {'int', 'integer', 'float', 'double', 'bool', 'boolean', 'str', 'string'}
        diag_msgs = []
        if node.lines:
            i = 0
            n = len(node.lines)
            while i < n:
                raw = node.lines[i]
                s = raw.strip()
                i += 1
                if not s or not s.startswith('types'):
                    continue
                rest = s[len('types'):].strip()
                if not rest:
                    continue
                # if rest starts a dict literal or begins a multi-line dict, collect until closing brace
                if rest.startswith('{'):
                    # collect chunk until we find a closing '}' (allow braces and tokens across lines)
                    chunk = rest
                    j = i
                    while '}' not in chunk and j < n:
                        chunk = chunk + '\n' + node.lines[j].strip()
                        j += 1
                    # advance outer index to skip collected lines
                    i = j
                    try:
                        start = chunk.find('{')
                        end = chunk.rfind('}')
                        if start != -1 and end != -1 and end > start:
                            dict_text = chunk[start:end+1]
                            blk = ast.literal_eval(dict_text)
                        else:
                            blk = None
                    except Exception:
                        blk = None
                    if isinstance(blk, dict):
                        for k, v in blk.items():
                            if not isinstance(k, str):
                                diag_msgs.append(f"ignored non-string key: {k!r}")
                                continue
                            if not isinstance(v, str):
                                diag_msgs.append(f"ignored non-string type for {k!r}: {v!r}")
                                continue
                            vt = v.strip().lower()
                            if vt in allowed:
                                block_types[k] = vt
                            else:
                                diag_msgs.append(f"ignored unknown type for {k!r}: {v!r}")
                    else:
                        # fallback: try a simple token parser for key:val pairs split by commas
                        try:
                            inner = chunk[chunk.find('{')+1:chunk.rfind('}')]
                            parts = [p.strip() for p in inner.split(',') if p.strip()]
                            for part in parts:
                                if ':' not in part:
                                    continue
                                k, v = part.split(':', 1)
                                k = k.strip().strip('"').strip("'")
                                v = v.strip().strip('"').strip("'").lower()
                                if k and v in allowed:
                                    block_types[k] = v
                                else:
                                    diag_msgs.append(f"ignored unknown or invalid entry: {part!r}")
                        except Exception:
                            diag_msgs.append("invalid types literal; ignored")
                    continue
                # if rest contains a single-line dict literal
                # single-line dict literal case (already contains closing brace)
                if rest.startswith('{') and '}' in rest:
                    try:
                        start = rest.find('{')
                        end = rest.rfind('}')
                        if start != -1 and end != -1 and end > start:
                            dict_text = rest[start:end+1]
                            blk = ast.literal_eval(dict_text)
                        else:
                            blk = None
                    except Exception:
                        blk = None
                    if isinstance(blk, dict):
                        for k, v in blk.items():
                            if not isinstance(k, str):
                                diag_msgs.append(f"ignored non-string key: {k!r}")
                                continue
                            if not isinstance(v, str):
                                diag_msgs.append(f"ignored non-string type for {k!r}: {v!r}")
                                continue
                            vt = v.strip().lower()
                            if vt in allowed:
                                block_types[k] = vt
                            else:
                                diag_msgs.append(f"ignored unknown type for {k!r}: {v!r}")
                    else:
                        # fallback token parser for single-line dict-like content
                        try:
                            inner = rest[rest.find('{')+1:rest.rfind('}')]
                            parts = [p.strip() for p in inner.split(',') if p.strip()]
                            for part in parts:
                                if ':' not in part:
                                    continue
                                k, v = part.split(':', 1)
                                k = k.strip().strip('"').strip("'")
                                v = v.strip().strip('"').strip("'").lower()
                                if k and v in allowed:
                                    block_types[k] = v
                                else:
                                    diag_msgs.append(f"ignored unknown or invalid entry: {part!r}")
                        except Exception:
                            diag_msgs.append("invalid types literal; ignored")
                    continue
                # otherwise accept simple tokens separated by whitespace or commas: key:val or key=val
                tokens = [t.strip().strip(',') for t in rest.replace(',', ' ').split() if t.strip()]
                for tok in tokens:
                    if ':' in tok:
                        k, v = tok.split(':', 1)
                    elif '=' in tok:
                        k, v = tok.split('=', 1)
                    else:
                        diag_msgs.append(f"ignored malformed token: {tok!r}")
                        continue
                    k = k.strip()
                    v = v.strip().strip('\"').strip("'" ).lower()
                    if not k:
                        diag_msgs.append(f"ignored empty key in token: {tok!r}")
                        continue
                    if not v or v not in allowed:
                        diag_msgs.append(f"ignored unknown or empty type for {k!r}: {v!r}")
                        continue
                    block_types[k] = v
        # emit diagnostics as comments before widget_types assignments and also emit runtime warnings
        for msg in diag_msgs:
            self.lines.append(f"# types: {msg}")
            # also warn at runtime so users see problems when running the generated UI
            self.lines.append(f"warnings.warn({repr(msg)})")
        # emit validated block-level types into widget_types
        for k, vt in block_types.items():
            self.lines.append(f"widget_types[{repr(k)}] = {repr(vt)}")

        for idx, ln in enumerate(node.lines):
            ln = ln.strip()
            if ln.startswith('addLabel('):
                text = self._extract_first_string(ln)
                self.lines.append(f"lbl{idx} = tk.Label(root, text={repr(text)})")
                self.lines.append(f"lbl{idx}.pack()")
            elif ln.startswith('addTextField('):
                parts = self._split_inner_parts(ln)
                name = self._extract_first_string(parts[0]) if parts else f"tf{idx}"
                # optional type annotation in second arg
                type_spec = None
                if len(parts) > 1 and parts[1]:
                    ts = parts[1].strip()
                    # strip quotes if present
                    if (ts.startswith('"') and ts.endswith('"')) or (ts.startswith("'") and ts.endswith("'")):
                        type_spec = ts[1:-1].strip().lower()
                    else:
                        type_spec = ts.strip().lower()
                self.lines.append(f"var_{name} = tk.StringVar()")
                self.lines.append(f"ent_{name} = tk.Entry(root, textvariable=var_{name})")
                self.lines.append(f"ent_{name}.pack()")
                self.lines.append(f"widgets[{repr(name)}] = var_{name}")
                # prefer explicit per-field annotation, else block-level types already emitted above
                if type_spec:
                    self.lines.append(f"widget_types[{repr(name)}] = {repr(type_spec)}")
            elif ln.startswith('addCheckbox('):
                parts = self._split_inner_parts(ln)
                name = self._extract_first_string(parts[0]) if parts else f"cb{idx}"
                # optional type annotation for checkbox (bool expected)
                type_spec = None
                if len(parts) > 1 and parts[1]:
                    ts = parts[1].strip()
                    if (ts.startswith('"') and ts.endswith('"')) or (ts.startswith("'") and ts.endswith("'")):
                        type_spec = ts[1:-1].strip().lower()
                    else:
                        type_spec = ts.strip().lower()
                self.lines.append(f"var_{name} = tk.BooleanVar()")
                self.lines.append(f"chk_{name} = tk.Checkbutton(root, variable=var_{name}, text={repr(name)})")
                self.lines.append(f"chk_{name}.pack()")
                self.lines.append(f"widgets[{repr(name)}] = var_{name}")
                if type_spec:
                    self.lines.append(f"widget_types[{repr(name)}] = {repr(type_spec)}")
            elif ln.startswith('addSlider('):
                parts = self._split_inner_parts(ln)
                name = self._extract_first_string(parts[0]) if parts else f"sl{idx}"
                # optional type annotation for slider (int/float)
                type_spec = None
                if len(parts) > 1 and parts[1]:
                    ts = parts[1].strip()
                    if (ts.startswith('"') and ts.endswith('"')) or (ts.startswith("'") and ts.endswith("'")):
                        type_spec = ts[1:-1].strip().lower()
                    else:
                        type_spec = ts.strip().lower()
                # default slider range
                self.lines.append(f"var_{name} = tk.DoubleVar()")
                self.lines.append(f"scl_{name} = tk.Scale(root, variable=var_{name}, from_=0, to=100, orient=tk.HORIZONTAL)")
                self.lines.append(f"scl_{name}.pack()")
                self.lines.append(f"widgets[{repr(name)}] = var_{name}")
                if type_spec:
                    self.lines.append(f"widget_types[{repr(name)}] = {repr(type_spec)}")
            elif ln.startswith('addButton('):
                label, handler_spec = self._split_button_parts(ln)
                text = label
                handler_name_gen = f"_on_click_{idx}"
                target_func, func_args = self._parse_handler_spec(handler_spec)

                # emit handler using helpers
                self._emit_gui_handler(idx, handler_name_gen, text, target_func, func_args)

                self.lines.append(f"btn{idx} = tk.Button(root, text={repr(text)}, command={handler_name_gen})")
                self.lines.append(f"btn{idx}.pack()")
            elif ln == 'show()':
                self.lines.append("# start the Tk main loop (call `root.mainloop()` to run)")
            else:
                self.lines.append(f"# GUI: {ln}")

    # Helpers for GUI emission
    def _extract_first_string(self, ln: str) -> str:
        m = ln.find('"')
        m2 = ln.rfind('"')
        if m != -1 and m2 != -1 and m2 > m:
            return ln[m+1:m2]
        # fallback: handle single quotes
        m = ln.find("'")
        m2 = ln.rfind("'")
        if m != -1 and m2 != -1 and m2 > m:
            return ln[m+1:m2]
        return ln

    def _split_button_parts(self, ln: str):
        inner = ln[ln.find('(')+1: ln.rfind(')')]
        parts = []
        cur = ''
        depth = 0
        in_str = False
        esc = False
        for ch in inner:
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
                    cur += ch
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
        if cur.strip():
            parts.append(cur.strip())
        label_part = parts[0] if parts else ''
        label = self._extract_first_string(label_part)
        handler_spec = parts[1] if len(parts) > 1 else None
        return label, handler_spec

    def _split_inner_parts(self, ln: str):
        inner = ln[ln.find('(')+1: ln.rfind(')')]
        parts = []
        cur = ''
        depth = 0
        in_str = False
        esc = False
        for ch in inner:
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
                    cur += ch
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
        if cur.strip():
            parts.append(cur.strip())
        return parts

    def _parse_handler_spec(self, handler_spec: str):
        if not handler_spec:
            return None, None
        hs = handler_spec
        if '(' in hs and hs.endswith(')'):
            fn = hs[:hs.find('(')].strip()
            arglist = hs[hs.find('(')+1:-1]
            arg_names = [a.strip().strip('"').strip("'") for a in arglist.split(',') if a.strip()]
            return fn, arg_names
        return hs.strip(), None

    def _emit_gui_handler(self, idx: int, handler_name_gen: str, text: str, target_func: str, func_args):
        self.lines.append(f"def {handler_name_gen}():")
        self.lines.append("    global _data")
        self.lines.append("    _data = gather_widget_data(widgets, widget_types)")
        if target_func:
            tf = target_func.strip()
            self.lines.append(f"    _fn = globals().get('{tf}')")
            if func_args:
                arg_exprs = []
                for a in func_args:
                    if a.startswith('"') and a.endswith('"'):
                        arg_exprs.append(repr(a[1:-1]))
                    else:
                        arg_exprs.append(f"_data.get('{a}')")
                args_code = ', '.join(arg_exprs)
                self.lines.append(f"    if callable(_fn):")
                self.lines.append(f"        invoke_or_emit_event(_fn, ({args_code},), _data, button_text={repr(text)})")
            else:
                self.lines.append(f"    if callable(_fn):")
                self.lines.append(f"        invoke_or_emit_event(_fn, None, _data, button_text={repr(text)})")
        else:
            func_name_conv = ''.join(c if (c.isalnum() or c==' ') else '_' for c in text).strip().lower().replace(' ', '_')
            self.lines.append(f"    _fn = globals().get('{func_name_conv}')")
            self.lines.append(f"    invoke_or_emit_event(_fn, None, _data, button_text={repr(text)})")

    def emit_statement(self, node):
        if isinstance(node, Print):
            if isinstance(node.expr, list):
                args = ', '.join(self.emit_expr(e) for e in node.expr)
                return [f"print({args})"]
            return [f"print({self.emit_expr(node.expr)})"]
        if isinstance(node, Assign):
            return [f"{node.target} = {self.emit_expr(node.expr)}"]
        if isinstance(node, Return):
            return [f"return {self.emit_expr(node.expr)}"]
        return [f"# stmt {node}"]

    def emit_expr(self, expr):
        if isinstance(expr, Str):
            return repr(expr.s)
        if isinstance(expr, Num):
            return repr(expr.v)
        if isinstance(expr, Var):
            return expr.name
        if hasattr(expr, 'op') and getattr(expr, '__class__').__name__ == 'UnaryOp':
            # UnaryOp(op, operand)
            return f"({expr.op} {self.emit_expr(expr.operand)})"
        # Compare
        if getattr(expr, '__class__').__name__ == 'Compare':
            # chained comparisons: left ops[0] comparators[0] ops[1] comparators[1] ...
            parts = [self.emit_expr(expr.left)]
            for op, comp in zip(expr.ops, expr.comparators):
                parts.append(op)
                parts.append(self.emit_expr(comp))
            return f"({' '.join(parts)})"
        # BoolOp
        if getattr(expr, '__class__').__name__ == 'BoolOp':
            op = expr.op
            vals = (' ' + op + ' ').join(self.emit_expr(v) for v in expr.values)
            return f"({vals})"
        if isinstance(expr, BinOp):
            left = self.emit_expr(expr.left)
            right = self.emit_expr(expr.right)
            return f"({left} {expr.op} {right})"
        return repr(expr)

    def to_source(self):
        return '\n'.join(self.lines) + '\n'
