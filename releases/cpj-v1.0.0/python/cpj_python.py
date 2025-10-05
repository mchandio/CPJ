"""
CPJ Python Module
Handles Python code parsing, auto-library detection, installation, and execution
"""
import sys
import ast
import pkg_resources
from cpj_python_utils import run_python, install_package

def detect_required_libraries(source_file):
    with open(source_file, 'r') as f:
        tree = ast.parse(f.read(), filename=source_file)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def install_missing_packages(packages):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    stdlib_modules = {
        'sys', 'os', 'subprocess', 'ast', 'pkg_resources', 'math', 'json', 're', 'datetime', 'time', 'random',
        'itertools', 'functools', 'collections', 'threading', 'multiprocessing', 'logging', 'argparse', 'typing',
        'pathlib', 'shutil', 'glob', 'csv', 'copy', 'enum', 'traceback', 'unittest', 'http', 'email', 'socket',
        'struct', 'base64', 'hashlib', 'getopt', 'statistics', 'pprint', 'inspect', 'ctypes', 'queue', 'weakref',
        'abc', 'array', 'bisect', 'codecs', 'contextlib', 'decimal', 'difflib', 'fileinput', 'fractions', 'heapq',
        'hmac', 'io', 'locale', 'mmap', 'numbers', 'pickle', 'selectors', 'signal', 'ssl', 'string', 'tarfile',
        'tempfile', 'textwrap', 'uuid', 'xml', 'zipfile', 'zoneinfo'
    }
    missing = [pkg for pkg in packages if pkg.lower() not in installed and pkg.lower() not in stdlib_modules]
    if missing:
        print(f"Installing missing packages: {missing}")
        for pkg in missing:
            install_package(pkg)

def run_python_file(source_file):
    run_python(source_file)

def main():
    if len(sys.argv) < 2:
        print("Usage: cpj_python.py <source_file.py>")
        sys.exit(1)
    source_file = sys.argv[1]
    required_libs = detect_required_libraries(source_file)
    install_missing_packages(required_libs)
    print("Running Python program...")
    run_python_file(source_file)

if __name__ == "__main__":
    main()
