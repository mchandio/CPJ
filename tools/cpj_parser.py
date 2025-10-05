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

class Return(Node):
    def __init__(self, expr):
        self.expr = expr

class GUIBlock(Node):
    def __init__(self, lines=None):
        self.lines = lines or []


class If(Node):
    def __init__(self, test, body=None, orelse=None):
        self.test = test
        self.body = body or []
        self.orelse = orelse or []
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
            if l.startswith('struct '):
                items.append(self.parse_struct())
            elif l.startswith('class '):
                items.append(self.parse_class())
            elif l.startswith('print'):
                items.append(self.parse_print())
            elif l.startswith('def '):
                items.append(self.parse_def())
            elif l.startswith('GUI'):
                items.append(self.parse_gui())
            elif '=' in l:
                items.append(self.parse_assign())
            else:
                # unknown, skip
                self.next_line()
        return Module(items)

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
        header = self.next_line().strip()
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
            l = self.peek_line().strip()
            if l == '}':
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
        parts = l.split('=', 1)
        if len(parts) == 2:
            target = parts[0].strip()
            expr = self.parse_expr_str(parts[1].strip())
            return Assign(target, expr)
        return Assign('<malformed>', Str(''))

    def parse_def(self):
        header_raw = self.next_line()
        header = header_raw.strip()
        header_indent = len(header_raw) - len(header_raw.lstrip()) if header_raw is not None else 0
        m = re.match(r'def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)\s*(?:->[^:]+)?\s*:\s*$', header)
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
                elif stmt.startswith('if '):
                    # parse simple if <expr>: with indented body and optional else
                    m2 = re.match(r'if\s+(.*):\s*$', stmt)
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
                            elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', inner):
                                parts = inner.split('=', 1)
                                if_body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                            self.next_line()
                        # check for else
                        orelse = []
                        if self.peek_line() is not None and self.peek_line().lstrip().startswith('else:'):
                            # consume else line
                            else_line = self.next_line()
                            else_indent = len(else_line) - len(else_line.lstrip())
                            while self.peek_line() is not None:
                                pl = self.peek_line()
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
                                elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', inner):
                                    parts = inner.split('=', 1)
                                    orelse.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                                self.next_line()
                        body.append(If(test_expr, if_body, orelse))
                        # continue without consuming next_line at end (we've already advanced)
                        continue
                elif re.match(r'^[A-Za-z_][A-Za-z0-9_]*\s*=\s*', stmt):
                    parts = stmt.split('=', 1)
                    body.append(Assign(parts[0].strip(), self.parse_expr_str(parts[1].strip())))
                self.next_line()
            else:
                break
        return FuncDef(name, args, body)

    def parse_gui(self):
        l = self.next_line().strip()
        # expect 'GUI {' on the same line or next
        rest = ''
        if l.endswith('{'):
            # collect until matching '}'
            lines = []
            while self.peek_line() is not None:
                ln = self.next_line().strip()
                if ln == '}':
                    break
                lines.append(ln)
            return GUIBlock(lines)
        else:
            # try to consume a following block
            if self.peek_line() and self.peek_line().strip().startswith('{'):
                self.next_line()
                lines = []
                while self.peek_line() is not None:
                    ln = self.next_line().strip()
                    if ln == '}': break
                    lines.append(ln)
                return GUIBlock(lines)
        return GUIBlock([])

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
    ('DOT',      r'\.'),
    ('COMMA',    r','),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('STAR',     r'\*'),
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
            # support dotted identifiers (e.g. obj.method) by peeking tokens
            name = t.value
            next_tok()
            while peek() and peek().type == 'DOT':
                # consume '.' and following ID
                next_tok()
                if not peek() or peek().type != 'ID':
                    raise SyntaxError('Expected identifier after .')
                name_part = next_tok().value
                name = name + '.' + name_part
            # function call?
            if peek() and peek().type == 'LPAREN':
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
                return Call(Var(name), args)
            return Var(name)
        if t.type == 'LPAREN':
            next_tok()
            node = parse_expression()
            if not peek() or peek().type != 'RPAREN':
                raise SyntaxError('Expected )')
            next_tok()
            return node
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

    def parse_term():
        left = parse_unary()
        while peek() and peek().type in ('STAR', 'SLASH', 'FLOORDIV'):
            op = next_tok().value
            right = parse_unary()
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
