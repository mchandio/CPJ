import re
import sys


class Node:
    pass

class StructDef(Node):
    def __init__(self, name, fields, generics=None):
        self.name = name
        self.fields = fields  # list of (name, type)
        self.generics = generics or []

# --- lightweight AST statement/container nodes used by the emitter ---
class Module(Node):
    def __init__(self, items):
        self.items = items

class ClassDef(Node):
    def __init__(self, name, fields=None, methods=None, generics=None):
        self.name = name
        self.fields = fields or []
        self.methods = methods or []
        self.generics = generics or []

class FuncDef(Node):
    def __init__(self, name, args=None, body=None):
        self.name = name
        self.args = args or []
        self.body = body or []

class Print(Node):
    def __init__(self, expr):
        self.expr = expr

class Assign(Node):
    def __init__(self, target, expr):
        self.target = target
        self.expr = expr

class AugAssign(Node):
    def __init__(self, target, op, expr):
        self.target = target
        self.op = op
        self.expr = expr

class Return(Node):
    def __init__(self, expr):
        self.expr = expr

class GUIBlock(Node):
    def __init__(self, lines=None):
        self.lines = lines or []


class WebBlock(Node):
    def __init__(self, lines=None):
        self.lines = lines or []


class If(Node):
    def __init__(self, test, body=None, orelse=None):
        self.test = test
        self.body = body or []
        self.orelse = orelse or []

class While(Node):
    def __init__(self, test, body=None):
        self.test = test
        self.body = body or []

class For(Node):
    def __init__(self, target, iter_expr, body=None):
        self.target = target
        self.iter_expr = iter_expr
        self.body = body or []

class Try(Node):
    def __init__(self, body=None, handlers=None, orelse=None, finalbody=None):
        self.body = body or []
        self.handlers = handlers or []
        self.orelse = orelse or []
        self.finalbody = finalbody or []

class ExceptHandler(Node):
    def __init__(self, type=None, name=None, body=None):
        self.type = type
        self.name = name
        self.body = body or []

class Raise(Node):
    def __init__(self, exc=None):
        self.exc = exc

class With(Node):
    def __init__(self, items=None, body=None):
        self.items = items or []  # List of (context_expr, optional_vars)
        self.body = body or []

class Import(Node):
    def __init__(self, module, alias=None):
        self.module = module
        self.alias = alias

class ImportFrom(Node):
    def __init__(self, module, names, aliases=None):
        self.module = module
        self.names = names  # List of names to import
        self.aliases = aliases or {}  # Dict of name -> alias

# Expression nodes: Literal (string/number), Var, BinOp
class Expr(Node):
    pass


class Str(Expr):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return f"Str({self.s})"


class Num(Expr):
    def __init__(self, v):
        self.v = v
    def __repr__(self):
        return f"Num({self.v})"


class Var(Expr):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Var({self.name})"


class BinOp(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left} {self.op} {self.right})"


class Call(Expr):
    def __init__(self, func, args):
        self.func = func  # Var or other expr
        self.args = args
    def __repr__(self):
        return f"Call({self.func}, args={self.args})"


class List(Expr):
    def __init__(self, elements):
        self.elements = elements or []
    def __repr__(self):
        return f"List({self.elements})"


class UnaryOp(Expr):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand
    def __repr__(self):
        return f"UnaryOp({self.op} {self.operand})"


class Compare(Expr):
    def __init__(self, left, ops, comparators):
        # ops: list of operator strings, comparators: list of Expr
        self.left = left
        self.ops = ops
        self.comparators = comparators
    def __repr__(self):
        parts = []
        cur = repr(self.left)
        for o, c in zip(self.ops, self.comparators):
            cur = f"({cur} {o} {c})"
            parts.append(cur)
        return f"Compare({', '.join(parts)})"


class BoolOp(Expr):
    def __init__(self, op, values):
        self.op = op  # 'and' or 'or'
        self.values = values
    def __repr__(self):
        return f"BoolOp({self.op}, {self.values})"


class Dict(Expr):
    def __init__(self, keys, values):
        self.keys = keys or []
        self.values = values or []
    def __repr__(self):
        return f"Dict({dict(zip(self.keys, self.values))})"


class Lambda(Expr):
    def __init__(self, args, body):
        self.args = args or []
        self.body = body
    def __repr__(self):
        return f"Lambda({self.args}, {self.body})"


class ListComp(Expr):
    def __init__(self, elt, generators):
        self.elt = elt
        self.generators = generators
    def __repr__(self):
        return f"ListComp({self.elt}, {self.generators})"


class DictComp(Expr):
    def __init__(self, key, value, generators):
        self.key = key
        self.value = value
        self.generators = generators
    def __repr__(self):
        return f"DictComp({self.key}: {self.value}, {self.generators})"


class Subscript(Expr):
    def __init__(self, value, slice):
        self.value = value
        self.slice = slice
    def __repr__(self):
        return f"Subscript({self.value}[{self.slice}])"


class Attribute(Expr):
    def __init__(self, value, attr):
        self.value = value
        self.attr = attr
    def __repr__(self):
        return f"Attribute({self.value}.{self.attr})"


class Parser:
    def __init__(self, src: str):
        # src may be the source text or a path to a file
        import os
        if os.path.exists(src):
            with open(src, 'r') as f:
                text = f.read()
        else:
            text = src
        # simple line-based parser, track indentation
        self.lines = text.splitlines()
        self.i = 0

    def peek_line(self):
        if self.i < len(self.lines):
            return self.lines[self.i]
        return None

    def next_line(self):
        l = self.peek_line()
        self.i += 1
        return l

    def parse(self):
        items = []
        while self.peek_line() is not None:
            l = self.peek_line().strip()
            if not l:
                self.next_line(); continue
            if l.startswith('import '):
                items.append(self.parse_import())
            elif l.startswith('from ') and ' import ' in l:
                items.append(self.parse_import_from())
            elif l.startswith('struct '):
                items.append(self.parse_struct())
            elif l.startswith('class '):
                items.append(self.parse_class())
            elif l.startswith('print'):
                items.append(self.parse_print())
            elif l.startswith('def '):
                items.append(self.parse_def())
            elif l.startswith('GUI'):
                items.append(self.parse_gui())
            elif re.match(r'(?i)^web\b', l):
                items.append(self.parse_web())
            elif l.startswith('try:'):
                items.append(self.parse_try())
            elif l.startswith('raise ') or l == 'raise':
                items.append(self.parse_raise())
            elif l.startswith('with '):
                items.append(self.parse_with())
            elif '=' in l:
                items.append(self.parse_assign())
            else:
                # unknown, skip
                self.next_line()
        return Module(items)

    def parse_try(self):
        """Parse try-except-finally block"""
        self.next_line()  # consume 'try:'
        try_indent = self.get_current_indent()

        # Parse try body
        body = []
        while self.peek_line() is not None:
            pl = self.peek_line()
            pl_indent = len(pl) - len(pl.lstrip())
            stripped = pl.strip()

            if stripped.startswith('catch ') or stripped.startswith('except '):
                break
            if stripped.startswith('finally:'):
                break
            if pl_indent <= try_indent and stripped:
                break

            body.append(self.parse_statement_line(pl))
            self.next_line()

        # Parse catch/except handlers
        handlers = []
        while self.peek_line() is not None:
            pl = self.peek_line().strip()
            if pl.startswith('catch ') or pl.startswith('except '):
                self.next_line()
                # Parse: catch ExceptionType as name:
                m = re.match(r'(?:catch|except)\s+([A-Za-z_][A-Za-z0-9_]*)?(?:\s+as\s+([A-Za-z_][A-Za-z0-9_]*))?\s*:\s*$', pl)
                exc_type = m.group(1) if m and m.group(1) else None
                exc_name = m.group(2) if m and m.group(2) else None

                handler_indent = self.get_current_indent()
                handler_body = []
                while self.peek_line() is not None:
                    hl = self.peek_line()
                    hl_indent = len(hl) - len(hl.lstrip())
                    if hl.strip().startswith('catch ') or hl.strip().startswith('except '):
                        break
                    if hl.strip().startswith('finally:'):
                        break
                    if hl_indent <= handler_indent and hl.strip():
                        break
                    handler_body.append(self.parse_statement_line(hl))
                    self.next_line()

                handlers.append(ExceptHandler(exc_type, exc_name, handler_body))
            else:
                break

        # Parse finally block
        finalbody = []
        if self.peek_line() and self.peek_line().strip().startswith('finally:'):
            self.next_line()
            finally_indent = self.get_current_indent()
            while self.peek_line() is not None:
                fl = self.peek_line()
                fl_indent = len(fl) - len(fl.lstrip())
                if fl_indent <= finally_indent and fl.strip():
                    break
                finalbody.append(self.parse_statement_line(fl))
                self.next_line()

        return Try(body, handlers, [], finalbody)

    def parse_raise(self):
        """Parse raise/throw statement"""
        line = self.next_line().strip()
        m = re.match(r'raise\s+(.+)$', line)
        if m:
            exc_expr = self.parse_expr_str(m.group(1))
            return Raise(exc_expr)
        return Raise(None)

    def get_current_indent(self):
        """Get indentation level of current line"""
        if self.i > 0 and self.i - 1 < len(self.lines):
            line = self.lines[self.i - 1]
            return len(line) - len(line.lstrip())
        return 0

    def parse_statement_line(self, line):
        """Parse a single statement line"""
        stmt = line.strip()
        if stmt.startswith('print'):
            m = re.match(r'print\((.*)\)\s*$', stmt)
            if m:
                inner = m.group(1)
                parts = self._split_print_args(inner)
                if len(parts) == 1:
                    return Print(self.parse_expr_str(parts[0]))
                else:
                    exprs = [self.parse_expr_str(p) for p in parts]
                    return Print(exprs)
        elif stmt.startswith('return'):
            m = re.match(r'return\s+(.*)$', stmt)
            if m:
                return Return(self.parse_expr_str(m.group(1)))
        elif stmt.startswith('raise'):
            m = re.match(r'raise\s+(.+)$', stmt)
            if m:
                return Raise(self.parse_expr_str(m.group(1)))
        elif '=' in stmt and not any(op in stmt for op in ['==', '!=', '<=', '>=']):
            # Check for augmented assignment
            for op in ['**=', '//=', '+=', '-=', '*=', '/=', '%=']:
                if op in stmt:
                    idx = stmt.find(op)
                    if idx > 0:
                        target = stmt[:idx].strip()
                        expr_str = stmt[idx+len(op):].strip()
                        if expr_str:
                            return AugAssign(target, op[:-1], self.parse_expr_str(expr_str))
            # Regular assignment
            parts = stmt.split('=', 1)
            if len(parts) == 2 and parts[1].strip():
                return Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip()))
        return None

    def parse_with(self):
        """Parse with statement (context manager)"""
        line = self.next_line().strip()
        # Parse: with expr as var: or with expr:
        m = re.match(r'with\s+(.+?)(?:\s+as\s+([A-Za-z_][A-Za-z0-9_]*))?\s*:\s*$', line)
        if not m:
            return With([], [])

        context_expr = self.parse_expr_str(m.group(1))
        var_name = m.group(2) if m.group(2) else None

        with_indent = self.get_current_indent()

        # Parse body
        body = []
        while self.peek_line() is not None:
            pl = self.peek_line()
            pl_indent = len(pl) - len(pl.lstrip())
            stripped = pl.strip()

            if pl_indent <= with_indent and stripped:
                break

            stmt = self.parse_statement_line(pl)
            if stmt:
                body.append(stmt)
            self.next_line()

        return With([(context_expr, var_name)], body)

    def parse_import(self):
        """Parse import statement: import Module or import Module as Alias"""
        line = self.next_line().strip()
        m = re.match(r'import\s+([A-Za-z_][A-Za-z0-9_.]*)(?:\s+as\s+([A-Za-z_][A-Za-z0-9_]*))?\s*$', line)
        if m:
            module = m.group(1)
            alias = m.group(2) if m.group(2) else None
            return Import(module, alias)
        return Import('', None)

    def parse_import_from(self):
        """Parse from...import statement: from Module import name1, name2 as alias"""
        line = self.next_line().strip()
        m = re.match(r'from\s+([A-Za-z_][A-Za-z0-9_.]*)\s+import\s+(.+)$', line)
        if not m:
            return ImportFrom('', [], {})

        module = m.group(1)
        imports_str = m.group(2).strip()

        names = []
        aliases = {}

        # Parse comma-separated imports with optional 'as' aliases
        parts = imports_str.split(',')
        for part in parts:
            part = part.strip()
            if ' as ' in part:
                name, alias = part.split(' as ', 1)
                name = name.strip()
                alias = alias.strip()
                names.append(name)
                aliases[name] = alias
            else:
                names.append(part)

        return ImportFrom(module, names, aliases)

    def parse_struct(self):
        header = self.next_line().strip()
        m = re.match(r'struct\s+([A-Za-z_][A-Za-z0-9_]*)(<([A-Za-z0-9_, ]+)>)?\s*\{', header)
        if not m:
            return StructDef('<malformed>', [], [])
        name = m.group(1)
        generics = []
        if m.group(3):
            generics = [g.strip() for g in m.group(3).split(',') if g.strip()]
        fields = []
        while self.peek_line() is not None:
            l = self.peek_line().strip()
            if l == '}':
                self.next_line(); break
            # expect: name: type
            m2 = re.match(r'([A-Za-z_][A-Za-z0-9_]*)\s*:\s*([A-Za-z_][A-Za-z0-9_<> ,]*)', l)
            if m2:
                fields.append((m2.group(1), m2.group(2)))
            self.next_line()
        return StructDef(name, fields, generics)

    def parse_class(self):
        header_raw = self.next_line()
        header = header_raw.strip()
        class_indent = len(header_raw) - len(header_raw.lstrip())
        m = re.match(r'class\s+([A-Za-z_][A-Za-z0-9_]*)(<([A-Za-z0-9_, ]+)>)?\s*\{', header)
        if not m:
            return ClassDef('<malformed>', [], [], [])
        name = m.group(1)
        generics = []
        if m.group(3):
            generics = [g.strip() for g in m.group(3).split(',') if g.strip()]
        fields = []
        methods = []
        while self.peek_line() is not None:
            nxt = self.peek_line()
            nxt_indent = len(nxt) - len(nxt.lstrip()) if nxt else 0
            l = nxt.strip()
            # Only consider } at the class indentation level as closing the class
            if l == '}' and nxt_indent <= class_indent:
                self.next_line(); break
            # field: name: type
            m2 = re.match(r'([A-Za-z_][A-Za-z0-9_]*)\s*:\s*([A-Za-z_][A-Za-z0-9_<> ,]*)', l)
            if m2:
                fields.append((m2.group(1), m2.group(2)))
                self.next_line(); continue
            # method: def ...
            if l.startswith('def '):
                methods.append(self.parse_def())
                continue
            self.next_line()
        return ClassDef(name, fields, methods, generics)

    def parse_print(self):
        l = self.next_line().strip()
        m = re.match(r'print\((.*)\)\s*$', l)
        if m:
            inner = m.group(1)
            # split top-level commas into separate exprs
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
            if len(parts) == 1:
                expr = self.parse_expr_str(parts[0])
                return Print(expr)
            exprs = [self.parse_expr_str(p) for p in parts]
            return Print(exprs)
        return Print(Str('<malformed>'))

    def parse_assign(self):
        l = self.next_line().strip()
        # Check for augmented assignment (check longest operators first to avoid conflicts)
        for op in ['**=', '//=', '+=', '-=', '*=', '/=', '%=']:
            if op in l and not any(cmp in l for cmp in ['==', '!=', '<=', '>=']):
                idx = l.find(op)
                if idx > 0:
                    target = l[:idx].strip()
                    expr_str = l[idx+len(op):].strip()
                    if expr_str:  # Make sure there's an expression
                        expr = self.parse_expr_str(expr_str)
                        return AugAssign(target, op[:-1], expr)  # Remove the '=' from op
        # Regular assignment
        parts = l.split('=', 1)
        if len(parts) == 2:
            target = parts[0].strip()
            expr_str = parts[1].strip()
            if expr_str:
                expr = self.parse_expr_str(expr_str)
                return Assign(target, expr)
        return Assign('<malformed>', Str(''))

    def parse_def(self):
        header_raw = self.next_line()
        header = header_raw.strip()
        header_indent = len(header_raw) - len(header_raw.lstrip()) if header_raw is not None else 0
        m = re.match(r'def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)\s*(?:->[^:{]+)?\s*[:{]\s*$', header)
        if not m:
            # fallback: name parsing
            mm = re.match(r'def\s+([A-Za-z_][A-Za-z0-9_]*)', header)
            name = mm.group(1) if mm else '<anon>'
            return FuncDef(name, [], [])
        name = m.group(1)
        argstr = m.group(2).strip()
        args = [a.strip() for a in argstr.split(',')] if argstr else []
        # parse indented body (lines starting with 4 spaces or a tab)
        body = []
        while self.peek_line() is not None:
            nxt = self.peek_line()
            # Check if this is a closing brace - if so, consume it and stop
            if nxt.strip() == '}':
                self.next_line()
                break
            # Skip empty lines - they don't break function bodies
            if not nxt.strip():
                self.next_line()
                continue
            # compute indentation of the next line; only accept lines with greater indentation than the header
            nxt_indent = len(nxt) - len(nxt.lstrip()) if nxt is not None else 0
            if nxt_indent > header_indent:
                stmt = nxt.lstrip()
                # if the indented line is another method header at the same indent, stop
                if stmt.startswith('def '):
                    break
                # fake a mini-parser for body statements
                if stmt.startswith('print') or stmt.startswith('print_line'):
                    m2 = re.match(r'print\((.*)\)\s*$', stmt)
                    if not m2 and stmt.startswith('print_line'):
                        m2 = re.match(r'print_line\((.*)\)\s*$', stmt)
                    if m2:
                        inner = m2.group(1)
                        # split top-level commas into separate exprs
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
                        if len(parts) == 1:
                            expr = self.parse_expr_str(parts[0])
                            body.append(Print(expr))
                        else:
                            exprs = [self.parse_expr_str(p) for p in parts]
                            body.append(Print(exprs))
                elif stmt.startswith('return'):
                    m2 = re.match(r'return\s+(.*)$', stmt)
                    if m2:
                        body.append(Return(self.parse_expr_str(m2.group(1))))
                elif stmt.startswith('try:'):
                    # Parse try-except block inside function
                    # Consume the try: line first
                    self.next_line()
                    try_node = self.parse_try_in_function(header_indent)
                    body.append(try_node)
                    continue
                elif stmt.startswith('with '):
                    # Parse with statement inside function
                    with_node = self.parse_with_in_function(header_indent)
                    body.append(with_node)
                    continue
                elif stmt.startswith('if '):
                    # parse if statement with : or { syntax
                    m2 = re.match(r'if\s+(.*)[:{]\s*$', stmt)
                    if m2:
                        test_expr = self.parse_expr_str(m2.group(1))
                        # consume this line
                        consumed_if = nxt
                        self.next_line()
                        # parse indented body; require indent strictly greater than the if line
                        if_indent = len(consumed_if) - len(consumed_if.lstrip())
                        if_body = []
                        while self.peek_line() is not None:
                            pl = self.peek_line()
                            if pl.strip() == '}':
                                self.next_line()
                                break
                            pl_indent = len(pl) - len(pl.lstrip())
                            if pl_indent <= if_indent:
                                break
                            inner = pl.lstrip()
                            # we only support print/return/assign inside if for now
                            if inner.startswith('print') or inner.startswith('print_line'):
                                mm = re.match(r'print\((.*)\)\s*$', inner)
                                if not mm and inner.startswith('print_line'):
                                    mm = re.match(r'print_line\((.*)\)\s*$', inner)
                                if mm:
                                    if_body.append(Print(self.parse_expr_str(mm.group(1))))
                            elif inner.startswith('return'):
                                mm = re.match(r'return\s+(.*)$', inner)
                                if mm:
                                    if_body.append(Return(self.parse_expr_str(mm.group(1))))
                            elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', inner) or any(op in inner for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']):
                                # Check for augmented assignment
                                aug_found = False
                                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                                    if op in inner:
                                        parts = inner.split(op, 1)
                                        if len(parts) == 2:
                                            if_body.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                            aug_found = True
                                            break
                                if not aug_found:
                                    parts = inner.split('=', 1)
                                    if_body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                            self.next_line()
                        # check for else (supports both else: and else {)
                        orelse = []
                        next_line_stripped = self.peek_line().lstrip() if self.peek_line() else ""
                        if self.peek_line() is not None and (next_line_stripped.startswith('else:') or next_line_stripped.startswith('else {')):
                            # consume else line
                            else_line = self.next_line()
                            else_indent = len(else_line) - len(else_line.lstrip())
                            while self.peek_line() is not None:
                                pl = self.peek_line()
                                if pl.strip() == '}':
                                    self.next_line()
                                    break
                                pl_indent = len(pl) - len(pl.lstrip())
                                if pl_indent <= else_indent:
                                    break
                                inner = pl.lstrip()
                                if inner.startswith('print') or inner.startswith('print_line'):
                                    mm = re.match(r'print\((.*)\)\s*$', inner)
                                    if not mm and inner.startswith('print_line'):
                                        mm = re.match(r'print_line\((.*)\)\s*$', inner)
                                    if mm:
                                        orelse.append(Print(self.parse_expr_str(mm.group(1))))
                                elif inner.startswith('return'):
                                    mm = re.match(r'return\s+(.*)$', inner)
                                    if mm:
                                        orelse.append(Return(self.parse_expr_str(mm.group(1))))
                                elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', inner) or any(op in inner for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']):
                                    # Check for augmented assignment
                                    aug_found = False
                                    for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                                        if op in inner:
                                            parts = inner.split(op, 1)
                                            if len(parts) == 2:
                                                orelse.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                                aug_found = True
                                                break
                                    if not aug_found:
                                        parts = inner.split('=', 1)
                                        orelse.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                                self.next_line()
                        body.append(If(test_expr, if_body, orelse))
                        # continue without consuming next_line at end (we've already advanced)
                        continue
                elif stmt.startswith('while '):
                    # parse while loop with : or { syntax
                    m2 = re.match(r'while\s+(.*)[:{]\s*$', stmt)
                    if m2:
                        test_expr = self.parse_expr_str(m2.group(1))
                        consumed_while = nxt
                        self.next_line()
                        while_indent = len(consumed_while) - len(consumed_while.lstrip())
                        while_body = []
                        while self.peek_line() is not None:
                            pl = self.peek_line()
                            if pl.strip() == '}':
                                self.next_line()
                                break
                            pl_indent = len(pl) - len(pl.lstrip())
                            if pl_indent <= while_indent:
                                break
                            inner = pl.lstrip()
                            if inner.startswith('print') or inner.startswith('print_line'):
                                mm = re.match(r'print\((.*)\)\s*$', inner)
                                if not mm and inner.startswith('print_line'):
                                    mm = re.match(r'print_line\((.*)\)\s*$', inner)
                                if mm:
                                    while_body.append(Print(self.parse_expr_str(mm.group(1))))
                            elif inner.startswith('return'):
                                mm = re.match(r'return\s+(.*)$', inner)
                                if mm:
                                    while_body.append(Return(self.parse_expr_str(mm.group(1))))
                            elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', inner) or any(op in inner for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']):
                                # Check for augmented assignment
                                aug_found = False
                                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                                    if op in inner:
                                        parts = inner.split(op, 1)
                                        if len(parts) == 2:
                                            while_body.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                            aug_found = True
                                            break
                                if not aug_found:
                                    parts = inner.split('=', 1)
                                    while_body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                            self.next_line()
                        body.append(While(test_expr, while_body))
                        continue
                elif stmt.startswith('for '):
                    # parse for loop: for var in expr { or for var in expr:
                    m2 = re.match(r'for\s+([A-Za-z_][A-Za-z0-9_]*)\s+in\s+(.*)[:{]\s*$', stmt)
                    if m2:
                        target = m2.group(1)
                        iter_expr = self.parse_expr_str(m2.group(2))
                        consumed_for = nxt
                        self.next_line()
                        for_indent = len(consumed_for) - len(consumed_for.lstrip())
                        for_body = []
                        while self.peek_line() is not None:
                            pl = self.peek_line()
                            if pl.strip() == '}':
                                self.next_line()
                                break
                            pl_indent = len(pl) - len(pl.lstrip())
                            if pl_indent <= for_indent:
                                break
                            inner = pl.lstrip()
                            if inner.startswith('print') or inner.startswith('print_line'):
                                mm = re.match(r'print\((.*)\)\s*$', inner)
                                if not mm and inner.startswith('print_line'):
                                    mm = re.match(r'print_line\((.*)\)\s*$', inner)
                                if mm:
                                    for_body.append(Print(self.parse_expr_str(mm.group(1))))
                            elif inner.startswith('return'):
                                mm = re.match(r'return\s+(.*)$', inner)
                                if mm:
                                    for_body.append(Return(self.parse_expr_str(mm.group(1))))
                            elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', inner) or any(op in inner for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']):
                                # Check for augmented assignment
                                aug_found = False
                                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                                    if op in inner:
                                        parts = inner.split(op, 1)
                                        if len(parts) == 2:
                                            for_body.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                            aug_found = True
                                            break
                                if not aug_found:
                                    parts = inner.split('=', 1)
                                    for_body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                            self.next_line()
                        body.append(For(target, iter_expr, for_body))
                        continue
                elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', stmt) or any(op in stmt for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']):
                    # Check for augmented assignment
                    aug_found = False
                    for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                        if op in stmt:
                            parts = stmt.split(op, 1)
                            if len(parts) == 2:
                                body.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                aug_found = True
                                break
                    if not aug_found:
                        parts = stmt.split('=', 1)
                        body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                elif re.match(r'^[A-Za-z_][A-Za-z0-9_.]*\s*\(', stmt):
                    # Standalone function call
                    try:
                        call_expr = self.parse_expr_str(stmt)
                        body.append(call_expr)
                    except:
                        pass  # Skip unparseable lines
                self.next_line()
            else:
                break
        return FuncDef(name, args, body)

    def parse_try_in_function(self, parent_indent):
        """Parse try-except-finally block inside a function body"""
        # The 'try:' line has already been consumed by caller
        try_indent = self.get_current_indent()

        # Parse try body
        body = []
        while self.peek_line() is not None:
            pl = self.peek_line()
            pl_indent = len(pl) - len(pl.lstrip())
            stripped = pl.strip()

            if stripped.startswith('catch ') or stripped.startswith('except '):
                break
            if stripped.startswith('finally:'):
                break
            if pl_indent <= parent_indent and stripped:
                break

            stmt = stripped
            if stmt.startswith('print'):
                m = re.match(r'print\((.*)\)\s*$', stmt)
                if m:
                    inner = m.group(1)
                    # Split on commas for multiple print arguments
                    parts = self._split_print_args(inner)
                    if len(parts) == 1:
                        body.append(Print(self.parse_expr_str(parts[0])))
                    else:
                        exprs = [self.parse_expr_str(p) for p in parts]
                        body.append(Print(exprs))
            elif stmt.startswith('return'):
                m = re.match(r'return\s+(.*)$', stmt)
                if m:
                    body.append(Return(self.parse_expr_str(m.group(1))))
            elif '=' in stmt and not any(op in stmt for op in ['==', '!=', '<=', '>=']):
                # Check for augmented assignment
                aug_found = False
                for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                    if op in stmt:
                        parts = stmt.split(op, 1)
                        if len(parts) == 2:
                            body.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                            aug_found = True
                            break
                if not aug_found:
                    parts = stmt.split('=', 1)
                    body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
            self.next_line()

        # Parse catch/except handlers
        handlers = []
        while self.peek_line() is not None:
            pl = self.peek_line().strip()
            if pl.startswith('catch ') or pl.startswith('except '):
                self.next_line()
                # Parse: catch ExceptionType as name:
                m = re.match(r'(?:catch|except)\s+([A-Za-z_][A-Za-z0-9_]*)?(?:\s+as\s+([A-Za-z_][A-Za-z0-9_]*))?\s*:\s*$', pl)
                exc_type = m.group(1) if m and m.group(1) else None
                exc_name = m.group(2) if m and m.group(2) else None

                handler_body = []
                while self.peek_line() is not None:
                    hl = self.peek_line()
                    hl_indent = len(hl) - len(hl.lstrip())
                    hl_stripped = hl.strip()

                    if hl_stripped.startswith('catch ') or hl_stripped.startswith('except '):
                        break
                    if hl_stripped.startswith('finally:'):
                        break
                    if hl_indent <= parent_indent and hl_stripped:
                        break

                    stmt = hl_stripped
                    if stmt.startswith('print'):
                        m = re.match(r'print\((.*)\)\s*$', stmt)
                        if m:
                            inner = m.group(1)
                            parts = self._split_print_args(inner)
                            if len(parts) == 1:
                                handler_body.append(Print(self.parse_expr_str(parts[0])))
                            else:
                                exprs = [self.parse_expr_str(p) for p in parts]
                                handler_body.append(Print(exprs))
                    elif stmt.startswith('return'):
                        m = re.match(r'return\s+(.*)$', stmt)
                        if m:
                            handler_body.append(Return(self.parse_expr_str(m.group(1))))
                    elif '=' in stmt and not any(op in stmt for op in ['==', '!=', '<=', '>=']):
                        # Check for augmented assignment
                        aug_found = False
                        for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                            if op in stmt:
                                parts = stmt.split(op, 1)
                                if len(parts) == 2:
                                    handler_body.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                    aug_found = True
                                    break
                        if not aug_found:
                            parts = stmt.split('=', 1)
                            handler_body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                    self.next_line()

                handlers.append(ExceptHandler(exc_type, exc_name, handler_body))
            else:
                break

        # Parse finally block
        finalbody = []
        if self.peek_line() and self.peek_line().strip().startswith('finally:'):
            self.next_line()
            while self.peek_line() is not None:
                fl = self.peek_line()
                fl_indent = len(fl) - len(fl.lstrip())
                fl_stripped = fl.strip()

                if fl_indent <= parent_indent and fl_stripped:
                    break

                stmt = fl_stripped
                if stmt.startswith('print'):
                    m = re.match(r'print\((.*)\)\s*$', stmt)
                    if m:
                        inner = m.group(1)
                        parts = self._split_print_args(inner)
                        if len(parts) == 1:
                            finalbody.append(Print(self.parse_expr_str(parts[0])))
                        else:
                            exprs = [self.parse_expr_str(p) for p in parts]
                            finalbody.append(Print(exprs))
                elif stmt.startswith('return'):
                    m = re.match(r'return\s+(.*)$', stmt)
                    if m:
                        finalbody.append(Return(self.parse_expr_str(m.group(1))))
                elif '=' in stmt and not any(op in stmt for op in ['==', '!=', '<=', '>=']):
                    # Check for augmented assignment
                    aug_found = False
                    for op in ['+=', '-=', '*=', '/=', '//=', '%=', '**=']:
                        if op in stmt:
                            parts = stmt.split(op, 1)
                            if len(parts) == 2:
                                finalbody.append(AugAssign(parts[0].strip(), op[:-1], self.parse_expr_str(parts[1].strip())))
                                aug_found = True
                                break
                    if not aug_found:
                        parts = stmt.split('=', 1)
                        finalbody.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                self.next_line()

        return Try(body, handlers, [], finalbody)

    def parse_with_in_function(self, parent_indent):
        """Parse with statement inside a function body"""
        # Already positioned at 'with' line
        line = self.next_line().strip()

        # Parse: with expr as var: or with expr:
        m = re.match(r'with\s+(.+?)(?:\s+as\s+([A-Za-z_][A-Za-z0-9_]*))?\s*:\s*$', line)
        if not m:
            return With([], [])

        context_expr = self.parse_expr_str(m.group(1))
        var_name = m.group(2) if m.group(2) else None

        # Parse body
        body = []
        while self.peek_line() is not None:
            pl = self.peek_line()
            pl_indent = len(pl) - len(pl.lstrip())
            pl_stripped = pl.strip()

            if pl_indent <= parent_indent and pl_stripped:
                break

            stmt = pl_stripped
            if stmt.startswith('print'):
                m = re.match(r'print\((.*)\)\s*$', stmt)
                if m:
                    inner = m.group(1)
                    parts = self._split_print_args(inner)
                    if len(parts) == 1:
                        body.append(Print(self.parse_expr_str(parts[0])))
                    else:
                        exprs = [self.parse_expr_str(p) for p in parts]
                        body.append(Print(exprs))
            elif stmt.startswith('return'):
                m = re.match(r'return\s+(.*)$', stmt)
                if m:
                    body.append(Return(self.parse_expr_str(m.group(1))))
            elif '=' in stmt and not any(op in stmt for op in ['==', '!=', '<=', '>=']):
                # Check for augmented assignment
                for op in ['**=', '//=', '+=', '-=', '*=', '/=', '%=']:
                    if op in stmt:
                        idx = stmt.find(op)
                        if idx > 0:
                            target = stmt[:idx].strip()
                            expr_str = stmt[idx+len(op):].strip()
                            if expr_str:
                                body.append(AugAssign(target, op[:-1], self.parse_expr_str(expr_str)))
                                break
                else:
                    parts = stmt.split('=', 1)
                    if len(parts) == 2 and parts[1].strip():
                        body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
            self.next_line()

        return With([(context_expr, var_name)], body)

    def _split_print_args(self, inner):
        """Split print arguments on top-level commas"""
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
                elif ch in '([{':
                    depth += 1
                    cur += ch
                elif ch in ')]}':
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

    def parse_gui(self):
        l = self.next_line().strip()
        # expect 'GUI {' on the same line or next
        if l.endswith('{'):
            # collect until the matching top-level '}', preserving nested blocks
            lines = []
            depth = l.count('{') - l.count('}')
            while self.peek_line() is not None and depth > 0:
                ln = self.next_line().strip()
                depth += ln.count('{') - ln.count('}')
                if depth <= 0 and ln == '}':
                    break
                lines.append(ln)
            return GUIBlock(lines)
        else:
            # try to consume a following block
            if self.peek_line() and self.peek_line().strip().startswith('{'):
                self.next_line()
                lines = []
                depth = 1
                while self.peek_line() is not None and depth > 0:
                    ln = self.next_line().strip()
                    depth += ln.count('{') - ln.count('}')
                    if depth <= 0 and ln == '}':
                        break
                    lines.append(ln)
                return GUIBlock(lines)
        return GUIBlock([])

    def parse_web(self):
        """Parse a standalone web block.

        The web emitter owns the nested DSL, so the parser preserves block lines
        with braces while balancing nested sections/components.
        """
        header = self.next_line().strip()
        lines = []

        if '{' not in header:
            if self.peek_line() and self.peek_line().strip().startswith('{'):
                self.next_line()
            else:
                return WebBlock([])

        depth = header.count('{') - header.count('}')
        while self.peek_line() is not None and depth > 0:
            raw = self.next_line()
            stripped = raw.strip()
            opens = stripped.count('{')
            closes = stripped.count('}')

            if closes >= depth and opens == 0 and stripped == '}':
                depth += opens - closes
                continue

            lines.append(stripped)
            depth += opens - closes

        return WebBlock(lines)

    def parse_expr_str(self, s: str):
        # Use a more complete expression parser to support nesting and calls.
        return parse_expr_text(s)

### Expression parser utilities
TOKEN_SPEC = [
    ('NUMBER',   r'\d+(?:\.\d+)?'),
    # boolean operators as tokens (word boundaries)
    ('AND',      r'\band\b'),
    ('OR',       r'\bor\b'),
    ('NOT',      r'\bnot\b'),
    # identifiers
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
    # support single-quoted or double-quoted strings
    ('STRING',   r"'(\\.|[^\\'])*'|\"(\\.|[^\\\"])*\""),
    # comparisons (multi-char first)
    ('EQ',       r'=='),
    ('NE',       r'!='),
    ('LE',       r'<='),
    ('GE',       r'>='),
    ('LT',       r'<'),
    ('GT',       r'>'),
    # bitwise
    ('LSHIFT',   r'<<'),
    ('RSHIFT',   r'>>'),
    ('BITAND',   r'&'),
    ('BITXOR',   r'\^'),
    ('BITOR',    r'\|'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('DOT',      r'\.'),
    ('COMMA',    r','),
    ('COLON',    r':'),
    ('PLUSEQ',   r'\+='),
    ('MINUSEQ',  r'-='),
    ('STAREQ',   r'\*='),
    ('SLASHEQ',  r'/='),
    ('FLOORDIVEQ', r'//='),
    ('MODEQ',    r'%='),
    ('POWEREQ',  r'\*\*='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('STAR',     r'\*\*|\*'),
    ('MOD',      r'%'),
    ('FLOORDIV', r'//'),
    ('SLASH',    r'/'),
    ('SKIP',     r'[ \t]+'),
    ('MISMATCH', r'.'),
]

_tok_re = re.compile('|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC))

class _Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"_Token({self.type},{self.value})"

def _tokenize_expr(s: str):
    pos = 0
    for m in _tok_re.finditer(s):
        typ = m.lastgroup
        val = m.group(typ)
        if typ == 'SKIP':
            continue
        if typ == 'MISMATCH':
            raise SyntaxError(f"Unexpected char in expression: {val}")
        yield _Token(typ, val)


def parse_expr_text(s: str):
    """Parse an expression string into Expr AST (supports identifiers, strings, numbers, +, and function calls)."""
    tokens = list(_tokenize_expr(s))
    i = 0

    def peek():
        return tokens[i] if i < len(tokens) else None

    def next_tok():
        nonlocal i
        t = peek()
        i += 1
        return t

    def parse_primary():
        t = peek()
        if not t:
            raise SyntaxError('Unexpected end of expr')
        if t.type == 'STRING':
            next_tok()
            return Str(t.value[1:-1])
        if t.type == 'NUMBER':
            next_tok()
            if '.' in t.value:
                return Num(float(t.value))
            else:
                return Num(int(t.value))
        if t.type == 'ID':
            # Check for lambda
            if t.value == 'lambda':
                next_tok()
                # Parse lambda args
                args = []
                if peek() and peek().type == 'ID':
                    while True:
                        args.append(next_tok().value)
                        if peek() and peek().type == 'COMMA':
                            next_tok()
                            continue
                        break
                # Expect colon
                if not peek() or peek().type != 'COLON':
                    raise SyntaxError('Expected : in lambda')
                next_tok()
                # Parse body expression
                body = parse_expression()
                return Lambda(args, body)

            # support dotted identifiers (e.g. obj.method) by peeking tokens
            name = t.value
            next_tok()
            # Check for subscript or attribute access
            result = Var(name)
            while True:
                if peek() and peek().type == 'DOT':
                    # consume '.' and following ID
                    next_tok()
                    if not peek() or peek().type != 'ID':
                        raise SyntaxError('Expected identifier after .')
                    attr = next_tok().value
                    result = Attribute(result, attr)
                elif peek() and peek().type == 'LBRACKET':
                    # subscript access
                    next_tok()
                    index = parse_expression()
                    if not peek() or peek().type != 'RBRACKET':
                        raise SyntaxError('Expected ]')
                    next_tok()
                    result = Subscript(result, index)
                elif peek() and peek().type == 'LPAREN':
                    # function call
                    next_tok()
                    args = []
                    if peek() and peek().type != 'RPAREN':
                        while True:
                            args.append(parse_expression())
                            if peek() and peek().type == 'COMMA':
                                next_tok()
                                continue
                            break
                    if not peek() or peek().type != 'RPAREN':
                        raise SyntaxError('Expected )')
                    next_tok()
                    result = Call(result, args)
                else:
                    break
            return result
        if t.type == 'LPAREN':
            next_tok()
            node = parse_expression()
            if not peek() or peek().type != 'RPAREN':
                raise SyntaxError('Expected )')
            next_tok()
            return node
        if t.type == 'LBRACKET':
            # Parse list literal [expr, expr, ...]
            next_tok()
            elements = []
            if peek() and peek().type != 'RBRACKET':
                # Check if this is a list comprehension
                first_expr = parse_or()  # Don't recurse into full expression yet
                if peek() and peek().type == 'ID' and peek().value == 'for':
                    # List comprehension
                    next_tok()  # consume 'for'
                    if not peek() or peek().type != 'ID':
                        raise SyntaxError('Expected variable in comprehension')
                    var = next_tok().value
                    if not peek() or peek().type != 'ID' or peek().value != 'in':
                        raise SyntaxError('Expected in')
                    next_tok()
                    iter_expr = parse_or()
                    # TODO: support filters with 'if'
                    generators = [(var, iter_expr)]
                    if not peek() or peek().type != 'RBRACKET':
                        raise SyntaxError('Expected ]')
                    next_tok()
                    return ListComp(first_expr, generators)
                else:
                    # Regular list
                    elements.append(first_expr)
                    while peek() and peek().type == 'COMMA':
                        next_tok()
                        if peek() and peek().type == 'RBRACKET':
                            break
                        elements.append(parse_expression())
            if not peek() or peek().type != 'RBRACKET':
                raise SyntaxError('Expected ]')
            next_tok()
            return List(elements)
        if t.type == 'LBRACE':
            # Parse dictionary literal {key: value, ...}
            next_tok()
            keys = []
            values = []
            if peek() and peek().type != 'RBRACE':
                while True:
                    key = parse_or()
                    if not peek() or peek().type != 'COLON':
                        raise SyntaxError('Expected : in dict')
                    next_tok()
                    value = parse_or()
                    keys.append(key)
                    values.append(value)
                    if peek() and peek().type == 'COMMA':
                        next_tok()
                        if peek() and peek().type == 'RBRACE':
                            break
                        continue
                    break
            if not peek() or peek().type != 'RBRACE':
                raise SyntaxError('Expected }')
            next_tok()
            return Dict(keys, values)
        raise SyntaxError(f'Unexpected token: {t}')
    def parse_unary():
        if peek() and peek().type == 'MINUS':
            next_tok()
            node = parse_unary()
            return UnaryOp('-', node)
        if peek() and peek().type == 'NOT':
            next_tok()
            node = parse_unary()
            return UnaryOp('not', node)
        return parse_primary()

    def parse_power():
        left = parse_unary()
        if peek() and peek().type == 'STAR' and peek().value == '**':
            op = next_tok().value
            right = parse_power()  # Right associative
            return BinOp(left, op, right)
        return left

    def parse_term():
        left = parse_power()
        while peek() and peek().type in ('STAR', 'SLASH', 'FLOORDIV', 'MOD'):
            op = next_tok().value
            if op == '**':
                continue  # Already handled in parse_power
            right = parse_power()
            left = BinOp(left, op, right)
        return left

    def parse_add():
        left = parse_term()
        while peek() and peek().type in ('PLUS', 'MINUS'):
            op = next_tok().value
            right = parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_shift():
        left = parse_add()
        while peek() and peek().type in ('LSHIFT', 'RSHIFT'):
            op = next_tok().value
            right = parse_add()
            left = BinOp(left, op, right)
        return left

    def parse_bitwise():
        left = parse_shift()
        # XOR has lower precedence than AND, OR lower than XOR
        # parse BITAND
        while peek() and peek().type == 'BITAND':
            op = next_tok().value
            right = parse_shift()
            left = BinOp(left, op, right)
        # parse BITXOR
        while peek() and peek().type == 'BITXOR':
            op = next_tok().value
            right = parse_shift()
            left = BinOp(left, op, right)
        # parse BITOR
        while peek() and peek().type == 'BITOR':
            op = next_tok().value
            right = parse_shift()
            left = BinOp(left, op, right)
        return left

    def parse_cmp():
        left = parse_bitwise()
        ops = []
        comparators = []
        while peek() and peek().type in ('EQ', 'NE', 'LE', 'GE', 'LT', 'GT'):
            tok = next_tok()
            op = tok.value
            right = parse_add()
            ops.append(op)
            comparators.append(right)
            # allow chained comparisons by continuing the loop
        if ops:
            return Compare(left, ops, comparators)
        return left

    def parse_and():
        left = parse_cmp()
        while peek() and peek().type == 'AND':
            next_tok()
            right = parse_cmp()
            left = BoolOp('and', [left, right])
        return left

    def parse_or():
        left = parse_and()
        while peek() and peek().type == 'OR':
            next_tok()
            right = parse_and()
            left = BoolOp('or', [left, right])
        return left

    def parse_expression():
        return parse_or()

    if not s.strip():
        raise SyntaxError('Empty expression')
    node = parse_expression()
    if i < len(tokens):
        raise SyntaxError('Extra tokens in expression')
    return node


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'samples/hello.cpj'
    with open(path, 'r') as f:
        src = f.read()
    p = Parser(src)
    ast = p.parse()
    print(ast)


def parse_file(path: str):
    """Convenience: parse a file path and return Module AST."""
    with open(path, 'r') as f:
        src = f.read()
    p = Parser(src)
    return p.parse()
