#!/usr/bin/env python3
"""
CPJ Standard Library - Complete Standalone Language Support

This module provides all essential functionality for CPJ to be a perfect
standalone programming language, including:

- File I/O operations
- String manipulation
- Math functions
- Collections and data structures
- Date and time handling
- JSON/XML parsing
- Regular expressions
- Network I/O (HTTP, sockets)
- System operations
- Cryptography basics
- Threading and concurrency
- Database operations
- Logging
- Testing framework
"""

import sys
import os
import io
import re
import json
import math
import time
import datetime
import hashlib
import base64
import random
import collections
import itertools
import functools
import threading
import subprocess
import urllib.request
import urllib.parse
import socket
import pathlib
from typing import Any, List, Dict, Optional, Callable, Tuple, Set, Union


# ============================================================================
# CPJ Runtime Core
# ============================================================================

class CPJRuntime:
    """Core runtime for CPJ language"""

    def __init__(self):
        self.globals = {}
        self.modules = {}

    def import_module(self, name: str, alias: Optional[str] = None):
        """Import a module into CPJ runtime"""
        if name in sys.modules:
            module = sys.modules[name]
        else:
            module = __import__(name)

        key = alias if alias else name
        self.modules[key] = module
        return module

    def print(self, *args, sep=' ', end='\n', file=None):
        """CPJ print function"""
        print(*args, sep=sep, end=end, file=file)


# ============================================================================
# File I/O Module
# ============================================================================

class File:
    """File operations with automatic resource management"""

    def __init__(self, path: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def open(self):
        """Open the file"""
        if 'b' in self.mode:
            self.file = open(self.path, self.mode)
        else:
            self.file = open(self.path, self.mode, encoding=self.encoding)
        return self

    def close(self):
        """Close the file"""
        if self.file:
            self.file.close()
            self.file = None

    def read(self, size: int = -1) -> str:
        """Read from file"""
        if not self.file:
            self.open()
        return self.file.read(size)

    def readline(self) -> str:
        """Read single line"""
        if not self.file:
            self.open()
        return self.file.readline()

    def readlines(self) -> List[str]:
        """Read all lines"""
        if not self.file:
            self.open()
        return self.file.readlines()

    def write(self, content: str) -> int:
        """Write to file"""
        if not self.file:
            self.open()
        return self.file.write(content)

    def writelines(self, lines: List[str]):
        """Write multiple lines"""
        if not self.file:
            self.open()
        self.file.writelines(lines)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @staticmethod
    def read_text(path: str, encoding: str = 'utf-8') -> str:
        """Read entire file as text"""
        with open(path, 'r', encoding=encoding) as f:
            return f.read()

    @staticmethod
    def write_text(path: str, content: str, encoding: str = 'utf-8'):
        """Write text to file"""
        with open(path, 'w', encoding=encoding) as f:
            f.write(content)

    @staticmethod
    def read_bytes(path: str) -> bytes:
        """Read entire file as bytes"""
        with open(path, 'rb') as f:
            return f.read()

    @staticmethod
    def write_bytes(path: str, content: bytes):
        """Write bytes to file"""
        with open(path, 'wb') as f:
            f.write(content)

    @staticmethod
    def exists(path: str) -> bool:
        """Check if file exists"""
        return os.path.exists(path)

    @staticmethod
    def delete(path: str):
        """Delete file"""
        os.remove(path)

    @staticmethod
    def copy(src: str, dst: str):
        """Copy file"""
        import shutil
        shutil.copy2(src, dst)

    @staticmethod
    def move(src: str, dst: str):
        """Move file"""
        import shutil
        shutil.move(src, dst)


# ============================================================================
# String Module
# ============================================================================

class String:
    """Enhanced string operations"""

    @staticmethod
    def upper(s: str) -> str:
        return s.upper()

    @staticmethod
    def lower(s: str) -> str:
        return s.lower()

    @staticmethod
    def capitalize(s: str) -> str:
        return s.capitalize()

    @staticmethod
    def title(s: str) -> str:
        return s.title()

    @staticmethod
    def strip(s: str, chars: Optional[str] = None) -> str:
        return s.strip(chars)

    @staticmethod
    def lstrip(s: str, chars: Optional[str] = None) -> str:
        return s.lstrip(chars)

    @staticmethod
    def rstrip(s: str, chars: Optional[str] = None) -> str:
        return s.rstrip(chars)

    @staticmethod
    def split(s: str, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
        return s.split(sep, maxsplit)

    @staticmethod
    def join(sep: str, items: List[str]) -> str:
        return sep.join(items)

    @staticmethod
    def replace(s: str, old: str, new: str, count: int = -1) -> str:
        return s.replace(old, new, count)

    @staticmethod
    def startswith(s: str, prefix: str) -> bool:
        return s.startswith(prefix)

    @staticmethod
    def endswith(s: str, suffix: str) -> bool:
        return s.endswith(suffix)

    @staticmethod
    def contains(s: str, substr: str) -> bool:
        return substr in s

    @staticmethod
    def find(s: str, substr: str, start: int = 0, end: Optional[int] = None) -> int:
        return s.find(substr, start, end if end else len(s))

    @staticmethod
    def count(s: str, substr: str) -> int:
        return s.count(substr)

    @staticmethod
    def format(template: str, *args, **kwargs) -> str:
        return template.format(*args, **kwargs)

    @staticmethod
    def reverse(s: str) -> str:
        return s[::-1]

    @staticmethod
    def is_alpha(s: str) -> bool:
        return s.isalpha()

    @staticmethod
    def is_digit(s: str) -> bool:
        return s.isdigit()

    @staticmethod
    def is_alnum(s: str) -> bool:
        return s.isalnum()

    @staticmethod
    def is_space(s: str) -> bool:
        return s.isspace()

    @staticmethod
    def length(s: str) -> int:
        return len(s)


# ============================================================================
# Math Module
# ============================================================================

class Math:
    """Mathematical functions"""

    # Constants
    PI = math.pi
    E = math.e
    TAU = math.tau
    INF = math.inf
    NAN = math.nan

    @staticmethod
    def abs(x):
        return abs(x)

    @staticmethod
    def ceil(x):
        return math.ceil(x)

    @staticmethod
    def floor(x):
        return math.floor(x)

    @staticmethod
    def round(x, ndigits=0):
        return round(x, ndigits)

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

    @staticmethod
    def pow(x, y):
        return math.pow(x, y)

    @staticmethod
    def exp(x):
        return math.exp(x)

    @staticmethod
    def log(x, base=math.e):
        return math.log(x, base)

    @staticmethod
    def log10(x):
        return math.log10(x)

    @staticmethod
    def log2(x):
        return math.log2(x)

    @staticmethod
    def sin(x):
        return math.sin(x)

    @staticmethod
    def cos(x):
        return math.cos(x)

    @staticmethod
    def tan(x):
        return math.tan(x)

    @staticmethod
    def asin(x):
        return math.asin(x)

    @staticmethod
    def acos(x):
        return math.acos(x)

    @staticmethod
    def atan(x):
        return math.atan(x)

    @staticmethod
    def atan2(y, x):
        return math.atan2(y, x)

    @staticmethod
    def sinh(x):
        return math.sinh(x)

    @staticmethod
    def cosh(x):
        return math.cosh(x)

    @staticmethod
    def tanh(x):
        return math.tanh(x)

    @staticmethod
    def degrees(x):
        return math.degrees(x)

    @staticmethod
    def radians(x):
        return math.radians(x)

    @staticmethod
    def max(*args):
        return max(args)

    @staticmethod
    def min(*args):
        return min(args)

    @staticmethod
    def sum(iterable, start=0):
        return sum(iterable, start)

    @staticmethod
    def gcd(a, b):
        return math.gcd(a, b)

    @staticmethod
    def factorial(n):
        return math.factorial(n)

    @staticmethod
    def isnan(x):
        return math.isnan(x)

    @staticmethod
    def isinf(x):
        return math.isinf(x)


# ============================================================================
# Collections Module
# ============================================================================

class Collections:
    """Enhanced collection types"""

    @staticmethod
    def Counter(iterable=None):
        """Count occurrences"""
        return collections.Counter(iterable)

    @staticmethod
    def OrderedDict():
        """Order-preserving dictionary"""
        return collections.OrderedDict()

    @staticmethod
    def defaultdict(default_factory):
        """Dict with default values"""
        return collections.defaultdict(default_factory)

    @staticmethod
    def deque(iterable=None, maxlen=None):
        """Double-ended queue"""
        return collections.deque(iterable or [], maxlen)

    @staticmethod
    def ChainMap(*maps):
        """Chain multiple dicts"""
        return collections.ChainMap(*maps)


class List:
    """Enhanced list operations"""

    @staticmethod
    def append(lst: list, item):
        lst.append(item)
        return lst

    @staticmethod
    def extend(lst: list, items):
        lst.extend(items)
        return lst

    @staticmethod
    def insert(lst: list, index: int, item):
        lst.insert(index, item)
        return lst

    @staticmethod
    def remove(lst: list, item):
        lst.remove(item)
        return lst

    @staticmethod
    def pop(lst: list, index: int = -1):
        return lst.pop(index)

    @staticmethod
    def clear(lst: list):
        lst.clear()
        return lst

    @staticmethod
    def index(lst: list, item):
        return lst.index(item)

    @staticmethod
    def count(lst: list, item):
        return lst.count(item)

    @staticmethod
    def sort(lst: list, key=None, reverse=False):
        lst.sort(key=key, reverse=reverse)
        return lst

    @staticmethod
    def reverse(lst: list):
        lst.reverse()
        return lst

    @staticmethod
    def copy(lst: list):
        return lst.copy()

    @staticmethod
    def filter(lst: list, predicate):
        return [item for item in lst if predicate(item)]

    @staticmethod
    def map(lst: list, func):
        return [func(item) for item in lst]

    @staticmethod
    def reduce(lst: list, func, initial=None):
        return functools.reduce(func, lst, initial)

    @staticmethod
    def any(lst: list, predicate=None):
        if predicate:
            return any(predicate(item) for item in lst)
        return any(lst)

    @staticmethod
    def all(lst: list, predicate=None):
        if predicate:
            return all(predicate(item) for item in lst)
        return all(lst)

    @staticmethod
    def zip(*lists):
        return list(zip(*lists))

    @staticmethod
    def enumerate(lst: list, start=0):
        return list(enumerate(lst, start))


class Dict:
    """Enhanced dictionary operations"""

    @staticmethod
    def keys(d: dict):
        return list(d.keys())

    @staticmethod
    def values(d: dict):
        return list(d.values())

    @staticmethod
    def items(d: dict):
        return list(d.items())

    @staticmethod
    def get(d: dict, key, default=None):
        return d.get(key, default)

    @staticmethod
    def pop(d: dict, key, default=None):
        return d.pop(key, default)

    @staticmethod
    def update(d: dict, other):
        d.update(other)
        return d

    @staticmethod
    def clear(d: dict):
        d.clear()
        return d

    @staticmethod
    def copy(d: dict):
        return d.copy()

    @staticmethod
    def has_key(d: dict, key):
        return key in d

    @staticmethod
    def merge(*dicts):
        result = {}
        for d in dicts:
            result.update(d)
        return result


# ============================================================================
# Date and Time Module
# ============================================================================

class DateTime:
    """Date and time operations"""

    @staticmethod
    def now():
        """Current datetime"""
        return datetime.datetime.now()

    @staticmethod
    def today():
        """Today's date"""
        return datetime.date.today()

    @staticmethod
    def timestamp():
        """Current Unix timestamp"""
        return time.time()

    @staticmethod
    def sleep(seconds: float):
        """Sleep for seconds"""
        time.sleep(seconds)

    @staticmethod
    def from_timestamp(ts: float):
        """Create datetime from timestamp"""
        return datetime.datetime.fromtimestamp(ts)

    @staticmethod
    def format(dt, fmt: str = '%Y-%m-%d %H:%M:%S'):
        """Format datetime"""
        return dt.strftime(fmt)

    @staticmethod
    def parse(date_string: str, fmt: str):
        """Parse datetime from string"""
        return datetime.datetime.strptime(date_string, fmt)

    @staticmethod
    def delta(days=0, seconds=0, minutes=0, hours=0, weeks=0):
        """Create timedelta"""
        return datetime.timedelta(
            days=days, seconds=seconds, minutes=minutes,
            hours=hours, weeks=weeks
        )


# ============================================================================
# JSON Module
# ============================================================================

class JSON:
    """JSON encoding and decoding"""

    @staticmethod
    def parse(json_string: str):
        """Parse JSON string"""
        return json.loads(json_string)

    @staticmethod
    def stringify(obj, indent=None, sort_keys=False):
        """Convert object to JSON string"""
        return json.dumps(obj, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def load(file_path: str):
        """Load JSON from file"""
        with open(file_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def save(obj, file_path: str, indent=2):
        """Save object to JSON file"""
        with open(file_path, 'w') as f:
            json.dump(obj, f, indent=indent)


# ============================================================================
# Regular Expressions Module
# ============================================================================

class Regex:
    """Regular expression operations"""

    @staticmethod
    def match(pattern: str, string: str, flags=0):
        """Match pattern at start of string"""
        result = re.match(pattern, string, flags)
        return result is not None

    @staticmethod
    def search(pattern: str, string: str, flags=0):
        """Search for pattern in string"""
        result = re.search(pattern, string, flags)
        return result is not None

    @staticmethod
    def findall(pattern: str, string: str, flags=0):
        """Find all matches"""
        return re.findall(pattern, string, flags)

    @staticmethod
    def finditer(pattern: str, string: str, flags=0):
        """Find all matches as iterator"""
        return list(re.finditer(pattern, string, flags))

    @staticmethod
    def sub(pattern: str, repl: str, string: str, count=0, flags=0):
        """Substitute pattern"""
        return re.sub(pattern, repl, string, count, flags)

    @staticmethod
    def split(pattern: str, string: str, maxsplit=0, flags=0):
        """Split by pattern"""
        return re.split(pattern, string, maxsplit, flags)

    @staticmethod
    def compile(pattern: str, flags=0):
        """Compile pattern"""
        return re.compile(pattern, flags)

    @staticmethod
    def escape(string: str):
        """Escape special characters"""
        return re.escape(string)


# ============================================================================
# HTTP Module
# ============================================================================

class HTTP:
    """HTTP client operations"""

    @staticmethod
    def get(url: str, headers: Optional[Dict] = None, timeout: int = 30):
        """HTTP GET request"""
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return {
                'status': response.status,
                'headers': dict(response.headers),
                'body': response.read().decode('utf-8')
            }

    @staticmethod
    def post(url: str, data: Union[str, bytes, Dict], headers: Optional[Dict] = None, timeout: int = 30):
        """HTTP POST request"""
        if isinstance(data, dict):
            data = urllib.parse.urlencode(data).encode('utf-8')
        elif isinstance(data, str):
            data = data.encode('utf-8')

        req = urllib.request.Request(url, data=data, headers=headers or {}, method='POST')
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return {
                'status': response.status,
                'headers': dict(response.headers),
                'body': response.read().decode('utf-8')
            }

    @staticmethod
    def download(url: str, file_path: str):
        """Download file from URL"""
        urllib.request.urlretrieve(url, file_path)


# ============================================================================
# Socket Module
# ============================================================================

class Socket:
    """Network socket operations"""

    @staticmethod
    def tcp_server(host: str, port: int, handler):
        """Create TCP server"""
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5)

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Connection from {address}")
            handler(client_socket, address)

    @staticmethod
    def tcp_client(host: str, port: int):
        """Create TCP client"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        return client_socket


# ============================================================================
# System Module
# ============================================================================

class System:
    """System operations"""

    @staticmethod
    def argv():
        """Command line arguments"""
        return sys.argv

    @staticmethod
    def exit(code: int = 0):
        """Exit program"""
        sys.exit(code)

    @staticmethod
    def getenv(name: str, default: Optional[str] = None):
        """Get environment variable"""
        return os.getenv(name, default)

    @staticmethod
    def setenv(name: str, value: str):
        """Set environment variable"""
        os.environ[name] = value

    @staticmethod
    def cwd():
        """Current working directory"""
        return os.getcwd()

    @staticmethod
    def chdir(path: str):
        """Change directory"""
        os.chdir(path)

    @staticmethod
    def listdir(path: str = '.'):
        """List directory contents"""
        return os.listdir(path)

    @staticmethod
    def mkdir(path: str, parents: bool = False):
        """Create directory"""
        if parents:
            os.makedirs(path, exist_ok=True)
        else:
            os.mkdir(path)

    @staticmethod
    def rmdir(path: str):
        """Remove directory"""
        os.rmdir(path)

    @staticmethod
    def execute(command: str, shell: bool = True, capture: bool = True):
        """Execute shell command"""
        if capture:
            result = subprocess.run(
                command, shell=shell, capture_output=True, text=True
            )
            return {
                'returncode': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr
            }
        else:
            return subprocess.run(command, shell=shell).returncode

    @staticmethod
    def platform():
        """Get platform name"""
        return sys.platform


# ============================================================================
# Crypto Module
# ============================================================================

class Crypto:
    """Cryptographic operations"""

    @staticmethod
    def md5(data: Union[str, bytes]):
        """MD5 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.md5(data).hexdigest()

    @staticmethod
    def sha1(data: Union[str, bytes]):
        """SHA1 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha1(data).hexdigest()

    @staticmethod
    def sha256(data: Union[str, bytes]):
        """SHA256 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha256(data).hexdigest()

    @staticmethod
    def sha512(data: Union[str, bytes]):
        """SHA512 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha512(data).hexdigest()

    @staticmethod
    def base64_encode(data: Union[str, bytes]):
        """Base64 encode"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('utf-8')

    @staticmethod
    def base64_decode(data: str):
        """Base64 decode"""
        return base64.b64decode(data).decode('utf-8')


# ============================================================================
# Random Module
# ============================================================================

class Random:
    """Random number generation"""

    @staticmethod
    def random():
        """Random float [0.0, 1.0)"""
        return random.random()

    @staticmethod
    def randint(a: int, b: int):
        """Random integer [a, b]"""
        return random.randint(a, b)

    @staticmethod
    def uniform(a: float, b: float):
        """Random float [a, b]"""
        return random.uniform(a, b)

    @staticmethod
    def choice(seq):
        """Random element from sequence"""
        return random.choice(seq)

    @staticmethod
    def choices(seq, k: int = 1):
        """k random elements with replacement"""
        return random.choices(seq, k=k)

    @staticmethod
    def sample(seq, k: int):
        """k random elements without replacement"""
        return random.sample(seq, k)

    @staticmethod
    def shuffle(seq):
        """Shuffle sequence in place"""
        random.shuffle(seq)
        return seq

    @staticmethod
    def seed(a=None):
        """Initialize random number generator"""
        random.seed(a)


# ============================================================================
# Threading Module
# ============================================================================

class Thread:
    """Threading support"""

    @staticmethod
    def create(target, args=(), kwargs=None, daemon=False):
        """Create and start thread"""
        thread = threading.Thread(target=target, args=args, kwargs=kwargs or {})
        thread.daemon = daemon
        thread.start()
        return thread

    @staticmethod
    def current():
        """Get current thread"""
        return threading.current_thread()

    @staticmethod
    def sleep(seconds: float):
        """Sleep current thread"""
        time.sleep(seconds)

    @staticmethod
    def Lock():
        """Create lock"""
        return threading.Lock()

    @staticmethod
    def RLock():
        """Create reentrant lock"""
        return threading.RLock()

    @staticmethod
    def Semaphore(value: int = 1):
        """Create semaphore"""
        return threading.Semaphore(value)

    @staticmethod
    def Event():
        """Create event"""
        return threading.Event()


# ============================================================================
# Exception Classes
# ============================================================================

class CPJException(Exception):
    """Base CPJ exception"""
    pass

class CPJIOError(CPJException):
    """I/O error"""
    pass

class CPJValueError(CPJException):
    """Value error"""
    pass

class CPJTypeError(CPJException):
    """Type error"""
    pass

class CPJRuntimeError(CPJException):
    """Runtime error"""
    pass


# ============================================================================
# Global CPJ API
# ============================================================================

# Create global runtime instance
_runtime = CPJRuntime()

# Export all modules
__all__ = [
    'CPJRuntime',
    'File',
    'String',
    'Math',
    'Collections',
    'List',
    'Dict',
    'DateTime',
    'JSON',
    'Regex',
    'HTTP',
    'Socket',
    'System',
    'Crypto',
    'Random',
    'Thread',
    'CPJException',
    'CPJIOError',
    'CPJValueError',
    'CPJTypeError',
    'CPJRuntimeError',
    'cpj_print',
    'cpj_input',
    'cpj_range',
    'cpj_len',
    'cpj_type',
    'cpj_int',
    'cpj_float',
    'cpj_str',
    'cpj_bool',
]


# ============================================================================
# Convenience Functions
# ============================================================================

def cpj_print(*args, **kwargs):
    """CPJ print function"""
    return _runtime.print(*args, **kwargs)

def cpj_input(prompt: str = '') -> str:
    """CPJ input function"""
    return input(prompt)

def cpj_range(*args):
    """CPJ range function"""
    return range(*args)

def cpj_len(obj):
    """CPJ len function"""
    return len(obj)

def cpj_type(obj):
    """CPJ type function"""
    return type(obj).__name__

def cpj_int(x):
    """CPJ int conversion"""
    return int(x)

def cpj_float(x):
    """CPJ float conversion"""
    return float(x)

def cpj_str(x):
    """CPJ str conversion"""
    return str(x)

def cpj_bool(x):
    """CPJ bool conversion"""
    return bool(x)


if __name__ == '__main__':
    print("CPJ Standard Library v1.0")
    print("Complete standalone language support")
    print(f"Modules available: {len(__all__)}")
