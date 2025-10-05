# CPJ Static Type Checker (initial draft)
# Walks the AST and checks GUI block widget types and handler signatures

from tools.cpj_parser import Parser, GUIBlock, FuncDef


class TypeChecker:
    def __init__(self, src):
        self.src = src
        self.errors = []
        self.ast = Parser(src).parse()
        self.widget_types = {}  # {var: type}
        self.func_sigs = {}     # {func: [param,...]}
        self.type_table = {}    # {type_name: {'fields': set, 'methods': set, 'generics': list}}
        self.var_types = {}     # {var: type} for type inference

    def check(self):
        self._collect_types()
        self._collect_func_sigs()
        self._collect_widget_types()
        self._infer_types()
        self._check_handler_calls()
        self._check_type_usages()
        return self.errors

    def _collect_types(self):
        for item in getattr(self.ast, 'items', []):
            if item.__class__.__name__ == 'StructDef':
                self.type_table[item.name] = {
                    'fields': set(f for f, _ in item.fields),
                    'methods': set(),
                    'generics': getattr(item, 'generics', [])
                }
            if item.__class__.__name__ == 'ClassDef':
                fields = set(f for f, _ in item.fields)
                methods = set(m.name for m in getattr(item, 'methods', []))
                self.type_table[item.name] = {
                    'fields': fields,
                    'methods': methods,
                    'generics': getattr(item, 'generics', [])
                }

    def _infer_types(self):
        # Simple type inference for assignments: var = Expr
        for item in getattr(self.ast, 'items', []):
            if item.__class__.__name__ == 'Assign':
                target = item.target
                expr = item.expr
                # Infer type from right-hand side if possible
                t = self._infer_expr_type(expr)
                if t:
                    self.var_types[target] = t

    def _infer_expr_type(self, expr):
        # Infer type from expression node
        if hasattr(expr, 'v'):
            if isinstance(expr.v, int):
                return 'int'
            if isinstance(expr.v, float):
                return 'float'
        if hasattr(expr, 's'):
            return 'string'
        if expr.__class__.__name__ == 'Var':
            return self.var_types.get(expr.name)
        if expr.__class__.__name__ == 'Call':
            # For demo: infer type from function name if known
            fn = expr.func.name if hasattr(expr.func, 'name') else None
            # Could look up function return type if annotated
            return None
        return None

    def _check_type_usages(self):
        # Example: check assignments and field accesses (expand as needed)
        for item in getattr(self.ast, 'items', []):
            if item.__class__.__name__ == 'Assign':
                target = item.target
                if '.' in target:
                    var, field = target.split('.', 1)
                    vtype = self.var_types.get(var)
                    found = False
                    for tname, tinfo in self.type_table.items():
                        if field in tinfo['fields']:
                            # If generic, allow any instantiation
                            if tinfo.get('generics'):
                                found = True
                                break
                            if vtype == tname:
                                found = True
                                break
                    if not found:
                        self.errors.append(
                            f"Type Error: Field '{field}' not found in any user-defined type or generic. "
                            f"Assignment: {target} = ... (inferred type: {vtype})"
                        )
            # Add more checks for method calls, etc., as needed

    def _collect_func_sigs(self):
        for item in getattr(self.ast, 'items', []):
            if isinstance(item, FuncDef):
                self.func_sigs[item.name] = item.args

    def _collect_widget_types(self):
        import ast
        allowed = {'int', 'integer', 'float', 'double', 'bool', 'boolean', 'str', 'string'}
        for item in getattr(self.ast, 'items', []):
            if isinstance(item, GUIBlock):
                lines = getattr(item, 'lines', [])
                for raw in lines:
                    s = raw.strip()
                    if not s or not s.startswith('types'):
                        continue
                    rest = s[len('types'):].strip()
                    if not rest:
                        continue
                    # dict-style
                    if rest.startswith('{'):
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
                                if isinstance(k, str) and isinstance(v, str) and v.strip().lower() in allowed:
                                    self.widget_types[k] = v.strip().lower()
                        continue
                    # token-style
                    tokens = [t.strip().strip(',') for t in rest.replace(',', ' ').split() if t.strip()]
                    for tok in tokens:
                        if ':' in tok:
                            k, v = tok.split(':', 1)
                        elif '=' in tok:
                            k, v = tok.split('=', 1)
                        else:
                            continue
                        k = k.strip()
                        v = v.strip().strip('"').strip("'").lower()
                        if k and v in allowed:
                            self.widget_types[k] = v

    def _check_handler_calls(self):
        for item in getattr(self.ast, 'items', []):
            if isinstance(item, GUIBlock):
                lines = getattr(item, 'lines', [])
                for raw in lines:
                    s = raw.strip()
                    if s.startswith('addButton('):
                        # parse handler call: addButton("Label", handler(args...))
                        inner = s[s.find('(')+1:s.rfind(')')]
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
                        if len(parts) > 1 and '(' in parts[1] and parts[1].endswith(')'):
                            handler = parts[1]
                            fn = handler[:handler.find('(')].strip()
                            arglist = handler[handler.find('(')+1:-1]
                            arg_names = [a.strip().strip('"').strip("'") for a in arglist.split(',') if a.strip()]
                            # static checks:
                            if fn not in self.func_sigs:
                                self.errors.append(
                                    f"Handler Error: '{fn}' not defined. Button: {raw}"
                                )
                                continue
                            expected = self.func_sigs[fn]
                            if len(arg_names) != len(expected):
                                self.errors.append(
                                    f"Handler Error: '{fn}' expects {len(expected)} args, got {len(arg_names)}. "
                                    f"Button: {raw}"
                                )
                            for i, arg in enumerate(arg_names):
                                if arg not in self.widget_types:
                                    self.errors.append(
                                        f"Handler Error: Argument '{arg}' not declared as widget in GUI block. "
                                        f"Button: {raw}"
                                    )

# Usage:
# checker = TypeChecker(src)
# errors = checker.check()
