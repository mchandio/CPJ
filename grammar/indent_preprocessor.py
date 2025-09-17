#!/usr/bin/env python3
"""
Simple indentation preprocessor for CPJ source files.

It reads a CPJ file and writes to stdout the same content but with explicit
<INDENT> and <DEDENT> tokens inserted on lines where indentation increases
or decreases. This is a pragmatic helper so the ANTLR grammar can be exercised
without implementing a full lexer rule for Python-style INDENT/DEDENT.

Limitations:
- Tabs are treated as 8 spaces (naive).
- Mixed tabs/spaces may behave unexpectedly.
- Intended for use during grammar prototyping, not production parsing.

Usage:
    python3 grammar/indent_preprocessor.py input.cpj > preproc.cpj

The output can then be fed to ANTLR or a parser expecting literal '<INDENT>'
and '<DEDENT>' tokens.
"""
import sys

def _count_leading_spaces(s: str) -> int:
    count = 0
    for ch in s:
        if ch == ' ':
            count += 1
        elif ch == '\t':
            count += 8
        else:
            break
    return count


def preprocess(lines):
    stack = [0]
    out = []
    for raw in lines:
        # preserve existing newlines
        line = raw.rstrip('\n')
        # ignore blank lines for indentation logic but keep them in output
        if line.strip() == '':
            out.append('')
            continue
        indent = _count_leading_spaces(line)
        if indent > stack[-1]:
            stack.append(indent)
            # emit INDENT marker inline with the current line to avoid a separate
            # newline token before the INDENT marker
            out.append('<INDENT> ' + line.lstrip())
        else:
            # emit one or more DEDENT markers inline before the current line
            dedents = ''
            while indent < stack[-1]:
                stack.pop()
                dedents += '<DEDENT> '
            out.append(dedents + line.lstrip())
    # close any remaining indents: attach trailing DEDENTs to the last non-empty
    # output line to avoid creating a bare '<DEDENT>' line which would produce
    # an extra NEWLINE token.
    while len(stack) > 1:
        stack.pop()
        if out:
            # append to the last output line with a leading space so the DEDENT token
            # doesn't glue to the previous token
            out[-1] = out[-1] + ' <DEDENT>'
        else:
            out.append('<DEDENT>')
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: indent_preprocessor.py <file.cpj>', file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out = preprocess(lines)
    for l in out:
        print(l)
