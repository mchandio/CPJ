import sys
from tools.cpj_parser import parse_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ast_dump.py <cpj_file>")
        sys.exit(1)
    ast = parse_file(sys.argv[1])
    import pprint
    pprint.pprint(ast)
