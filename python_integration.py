
import pip
import ast
import sys

def scan_imports(file_path):
    with open(file_path) as f:
        tree = ast.parse(f.read())
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.add(node.module)
    return imports

def install_requirements(requirements):
    pip.main(['install'] + list(requirements))
