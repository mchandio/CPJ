"""
CPJ Standard Library
====================

A comprehensive standard library for the CPJ programming language.

Available Modules:
- Math: Mathematical functions and constants
- String: String manipulation functions
- File: File I/O operations
- JSON: JSON parsing and generation
- System: System operations and platform information
"""

# Import standard library modules
try:
    from .cpj_math import Math
except ImportError:
    from cpj_math import Math

try:
    from .cpj_string import String
except ImportError:
    from cpj_string import String

try:
    from .cpj_file import File, open_file, open
except ImportError:
    from cpj_file import File, open_file, open

try:
    from .cpj_json import JSON, parse, stringify
except ImportError:
    from cpj_json import JSON, parse, stringify

try:
    from .cpj_system import System, exit, getenv, exec_command, sleep
except ImportError:
    from cpj_system import System, exit, getenv, exec_command, sleep

__all__ = [
    'Math',
    'String',
    'File',
    'JSON',
    'System',
    'open_file',
    'open',
    'parse',
    'stringify',
    'exit',
    'getenv',
    'exec_command',
    'sleep'
]

__version__ = '5.0.0'
__author__ = 'CPJ Development Team'

# Module information
MODULES = {
    'Math': 'Mathematical functions and constants',
    'String': 'String manipulation and processing',
    'File': 'File I/O operations',
    'JSON': 'JSON encoding and decoding',
    'System': 'System and platform operations'
}

def help_stdlib():
    """Display help information about the standard library"""
    print("CPJ Standard Library v{}".format(__version__))
    print("=" * 50)
    print("\nAvailable Modules:")
    for module, description in MODULES.items():
        print("  - {}: {}".format(module, description))
    print("\nUsage:")
    print("  import Math")
    print("  result = Math.sqrt(16)")
    print("\nFor detailed help on a module, use:")
    print("  help(Math)")
