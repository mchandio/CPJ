#!/usr/bin/env python3
"""Very small fallback CPJ emitter for brace-style samples.
Supports: imports (ignored), class ... { def ... { ... } }, def main() { ... }, simple statements (return, print_line, expressions).
Not a full parser — intended only to validate/execute simple samples while the main parser is being fixed.
"""
import sys
import re

def read_file(path):
    with open(path, 'r') as f:
        return f.read().splitlines()

def emit_python(lines):
    out = []
    out.append("# Fallback emitted Python")
    out.append("def print_line(s):\n    print(s)\n")

    # We'll implement a simple brace-to-indentation converter.
    stack = [0]  # indentation stack (number of spaces)
    indent = 0
    i = 0
    n = len(lines)
    while i < n:
        raw = lines[i]
        l = raw.strip()
        i += 1
        if not l or l.startswith('#'):
            continue
        if l.startswith('import '):
            continue

        # open brace handling (class or other)
        m_class = re.match(r'class\s+(\w+)\s*\{', l)
        if m_class:
            cls = m_class.group(1)
            out.append(' ' * indent + f'class {cls}:')
            # increase indentation for class body
            indent += 4
            stack.append(indent)
            continue

        # closing brace
        if l == '}':
            if len(stack) > 1:
                stack.pop()
                indent = stack[-1]
            continue

        # def inside a brace-style class or at top-level
        m_def = re.match(r'def\s+(\w+)\s*\(([^)]*)\)\s*(?:->[^:]+)?\s*:\s*$', l) or re.match(r'def\s+(\w+)\s*\(([^)]*)\)\s*(?:->[^\{]+)?\s*\{', l)
        if m_def:
            name = m_def.group(1)
            args = m_def.group(2).strip()
            # drop type annotations
            argnames = []
            if args:
                for a in args.split(','):
                    an = a.split(':',1)[0].split('=',1)[0].strip()
                    if an:
                        argnames.append(an)
            sig = ', '.join(argnames)
            # if inside a class and first arg isn't self, add it
            if indent > 0 and (not sig or sig.split(',')[0] != 'self'):
                if sig:
                    sig = 'self, ' + sig
                else:
                    sig = 'self'
            out.append(' ' * indent + f'def {name}({sig}):')
            # if brace-style (header had '{'), the body will follow; if colon-style with indentation,
            # we treat next indented lines as body; for brace-style, consume until a '}' at same level.
            # Increase indentation for function body
            indent += 4
            stack.append(indent)
            # collect body lines until indentation reduces or a closing brace
            # determine body indentation expected for this function (based on current indent)
            func_body_indent = indent
            while i < n:
                pline = lines[i]
                s = pline.strip()
                pline_indent = len(pline) - len(pline.lstrip())
                # if this line is less-indented than the function body, it's outside -> break
                if pline_indent < func_body_indent or s == '}':
                    break
                # handle 'if' with strict indent comparison
                if s.startswith('if ') and s.endswith(':'):
                    # emit the if at function body indent
                    out.append(' ' * func_body_indent + s)
                    i += 1
                    # if block uses deeper indentation than the if line
                    if_indent = pline_indent
                    while i < n:
                        inner_line = lines[i]
                        inner_indent = len(inner_line) - len(inner_line.lstrip())
                        if inner_indent <= if_indent:
                            break
                        out.append(' ' * inner_indent + inner_line.strip())
                        i += 1
                    continue
                if s.lstrip().startswith('else:'):
                    # emit else at the same level as if (which is one indent less than body)
                    out.append(' ' * (func_body_indent - 4) + 'else:')
                    i += 1
                    # collect else body lines with indent > (func_body_indent - 4)
                    else_indent = len(lines[i-1]) - len(lines[i-1].lstrip()) if i-1 < n else func_body_indent - 4
                    while i < n:
                        inner_line = lines[i]
                        inner_indent = len(inner_line) - len(inner_line.lstrip())
                        if inner_indent <= else_indent:
                            break
                        out.append(' ' * inner_indent + inner_line.strip())
                        i += 1
                    continue
                if s:
                    out.append(' ' * func_body_indent + s)
                i += 1
            # ensure function has at least a pass
            if not any(x.strip() for x in out[-1:]):
                out.append(' ' * indent + 'pass')
            # pop indentation for function
            if len(stack) > 1:
                stack.pop()
                indent = stack[-1]
            continue

        # top-level calls
        if re.match(r'\w+\s*\(', l):
            out.append(' ' * indent + l)
            continue

        # any other line - emit at current indent
        out.append(' ' * indent + l)

    return '\n'.join(out) + '\n'

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('input')
    p.add_argument('-o','--output', required=True)
    args = p.parse_args()
    lines = read_file(args.input)
    py = emit_python(lines)
    with open(args.output, 'w') as f:
        f.write(py)
    print(f"[SimpleEmitter] wrote {args.output}")

if __name__ == '__main__':
    main()
