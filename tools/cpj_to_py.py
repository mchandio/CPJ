"""
Quick CPJ to Python converter for DOS system
"""
import sys
import re

def convert_cpj_to_py(cpj_file, py_file):
    with open(cpj_file, 'r') as f:
        cpj_code = f.read()
    
    # Add imports
    py_code = "from dataclasses import dataclass\nfrom typing import List, Dict, Optional\n\n" + cpj_code
    
    # Convert type definitions to dataclasses
    py_code = py_code.replace('type ', '@dataclass\nclass ')
    
    # Handle constants
    const_pattern = r'const (\w+): \w+ = (.+)'
    py_code = re.sub(const_pattern, r'\1 = \2', py_code)
    
    # Fix exception handling
    py_code = py_code.replace('catch', 'except')
    
    # Convert syntax
    py_code = py_code.replace('{', ':')
    py_code = py_code.replace('}', '')
    py_code = py_code.replace('-> void', '')
    py_code = py_code.replace('private:', '# private:')
    py_code = py_code.replace('public:', '# public:')
    py_code = py_code.replace('self.', 'self.')
    
    # Fix dataclass field definitions
    field_pattern = r'(\w+): (\w+),'
    py_code = re.sub(field_pattern, r'\1: \2', py_code)
    
    # Add self parameters to methods
    method_pattern = r'def (\w+)\((.*?)\)'
    def add_self(match):
        method_name = match.group(1)
        params = match.group(2)
        if params and not params.startswith('self'):
            return f'def {method_name}(self, {params})'
        elif not params:
            return f'def {method_name}(self)'
        return match.group(0)
    
    py_code = re.sub(method_pattern, add_self, py_code)
    
    # Fix indentation
    lines = py_code.split('\n')
    fixed_lines = []
    indent_level = 0
    for line in lines:
        stripped = line.strip()
        if not stripped:
            fixed_lines.append('')
            continue
            
        # Decrease indent for else/except
        if stripped.startswith(('else:', 'except', 'elif')):
            indent_level -= 1
            
        # Add line with proper indentation
        fixed_lines.append('    ' * indent_level + stripped)
        
        # Increase indent after :
        if stripped.endswith(':'):
            indent_level += 1
            
    py_code = '\n'.join(fixed_lines)
    
    with open(py_file, 'w') as f:
        f.write(py_code)

def main():
    # Convert each DOS system file
    files = ['dos_shell.cpj', 'dos_filesystem.cpj', 'dos_memory.cpj']
    for file in files:
        py_file = file.replace('.cpj', '.py')
        print(f"Converting {file} to {py_file}")
        convert_cpj_to_py(file, py_file)

if __name__ == '__main__':
    main()