"""
CPJ String Module
Provides string manipulation functions for the CPJ programming language
"""


class String:
    """String manipulation functions"""

    # Case conversion
    @staticmethod
    def upper(s):
        """Convert string to uppercase"""
        return s.upper()

    @staticmethod
    def lower(s):
        """Convert string to lowercase"""
        return s.lower()

    @staticmethod
    def capitalize(s):
        """Capitalize first character"""
        return s.capitalize()

    @staticmethod
    def title(s):
        """Convert to title case"""
        return s.title()

    @staticmethod
    def swapcase(s):
        """Swap case of all characters"""
        return s.swapcase()

    # Trimming
    @staticmethod
    def strip(s, chars=None):
        """Remove leading and trailing characters"""
        return s.strip(chars)

    @staticmethod
    def lstrip(s, chars=None):
        """Remove leading characters"""
        return s.lstrip(chars)

    @staticmethod
    def rstrip(s, chars=None):
        """Remove trailing characters"""
        return s.rstrip(chars)

    # Splitting and joining
    @staticmethod
    def split(s, sep=None, maxsplit=-1):
        """Split string by separator"""
        return s.split(sep, maxsplit)

    @staticmethod
    def rsplit(s, sep=None, maxsplit=-1):
        """Split string from right"""
        return s.rsplit(sep, maxsplit)

    @staticmethod
    def splitlines(s, keepends=False):
        """Split string by line breaks"""
        return s.splitlines(keepends)

    @staticmethod
    def join(sep, iterable):
        """Join iterable with separator"""
        return sep.join(iterable)

    # Searching
    @staticmethod
    def find(s, sub, start=0, end=None):
        """Find first occurrence of substring"""
        if end is None:
            return s.find(sub, start)
        return s.find(sub, start, end)

    @staticmethod
    def rfind(s, sub, start=0, end=None):
        """Find last occurrence of substring"""
        if end is None:
            return s.rfind(sub, start)
        return s.rfind(sub, start, end)

    @staticmethod
    def index(s, sub, start=0, end=None):
        """Find first occurrence (raises error if not found)"""
        if end is None:
            return s.index(sub, start)
        return s.index(sub, start, end)

    @staticmethod
    def rindex(s, sub, start=0, end=None):
        """Find last occurrence (raises error if not found)"""
        if end is None:
            return s.rindex(sub, start)
        return s.rindex(sub, start, end)

    @staticmethod
    def count(s, sub, start=0, end=None):
        """Count occurrences of substring"""
        if end is None:
            return s.count(sub, start)
        return s.count(sub, start, end)

    # Checking
    @staticmethod
    def startswith(s, prefix, start=0, end=None):
        """Check if string starts with prefix"""
        if end is None:
            return s.startswith(prefix, start)
        return s.startswith(prefix, start, end)

    @staticmethod
    def endswith(s, suffix, start=0, end=None):
        """Check if string ends with suffix"""
        if end is None:
            return s.endswith(suffix, start)
        return s.endswith(suffix, start, end)

    @staticmethod
    def contains(s, sub):
        """Check if string contains substring"""
        return sub in s

    # Character type checking
    @staticmethod
    def isalpha(s):
        """Check if all characters are alphabetic"""
        return s.isalpha()

    @staticmethod
    def isdigit(s):
        """Check if all characters are digits"""
        return s.isdigit()

    @staticmethod
    def isalnum(s):
        """Check if all characters are alphanumeric"""
        return s.isalnum()

    @staticmethod
    def isspace(s):
        """Check if all characters are whitespace"""
        return s.isspace()

    @staticmethod
    def islower(s):
        """Check if all cased characters are lowercase"""
        return s.islower()

    @staticmethod
    def isupper(s):
        """Check if all cased characters are uppercase"""
        return s.isupper()

    @staticmethod
    def istitle(s):
        """Check if string is in title case"""
        return s.istitle()

    @staticmethod
    def isnumeric(s):
        """Check if all characters are numeric"""
        return s.isnumeric()

    @staticmethod
    def isdecimal(s):
        """Check if all characters are decimal"""
        return s.isdecimal()

    @staticmethod
    def isascii(s):
        """Check if all characters are ASCII"""
        return s.isascii()

    # Replacement
    @staticmethod
    def replace(s, old, new, count=-1):
        """Replace occurrences of substring"""
        return s.replace(old, new, count)

    # Padding and alignment
    @staticmethod
    def center(s, width, fillchar=' '):
        """Center string in field of width"""
        return s.center(width, fillchar)

    @staticmethod
    def ljust(s, width, fillchar=' '):
        """Left-justify string in field of width"""
        return s.ljust(width, fillchar)

    @staticmethod
    def rjust(s, width, fillchar=' '):
        """Right-justify string in field of width"""
        return s.rjust(width, fillchar)

    @staticmethod
    def zfill(s, width):
        """Pad string with zeros on left"""
        return s.zfill(width)

    # Length and access
    @staticmethod
    def length(s):
        """Get string length"""
        return len(s)

    @staticmethod
    def substring(s, start, end=None):
        """Get substring"""
        if end is None:
            return s[start:]
        return s[start:end]

    @staticmethod
    def char_at(s, index):
        """Get character at index"""
        return s[index]

    # Encoding
    @staticmethod
    def encode(s, encoding='utf-8', errors='strict'):
        """Encode string to bytes"""
        return s.encode(encoding, errors)

    @staticmethod
    def decode(b, encoding='utf-8', errors='strict'):
        """Decode bytes to string"""
        return b.decode(encoding, errors)

    # Formatting
    @staticmethod
    def format(template, *args, **kwargs):
        """Format string with arguments"""
        return template.format(*args, **kwargs)

    @staticmethod
    def reverse(s):
        """Reverse string"""
        return s[::-1]

    @staticmethod
    def repeat(s, count):
        """Repeat string count times"""
        return s * count

    # Parsing
    @staticmethod
    def to_int(s, base=10):
        """Convert string to integer"""
        return int(s, base)

    @staticmethod
    def to_float(s):
        """Convert string to float"""
        return float(s)

    @staticmethod
    def to_bool(s):
        """Convert string to boolean"""
        s_lower = s.lower().strip()
        if s_lower in ('true', '1', 'yes', 'y', 't'):
            return True
        elif s_lower in ('false', '0', 'no', 'n', 'f'):
            return False
        else:
            return bool(s)

    # Advanced operations
    @staticmethod
    def partition(s, sep):
        """Partition string at first occurrence of sep"""
        return s.partition(sep)

    @staticmethod
    def rpartition(s, sep):
        """Partition string at last occurrence of sep"""
        return s.rpartition(sep)

    @staticmethod
    def expandtabs(s, tabsize=8):
        """Expand tabs to spaces"""
        return s.expandtabs(tabsize)

    @staticmethod
    def translate(s, table):
        """Translate string using translation table"""
        return s.translate(table)

    @staticmethod
    def maketrans(x, y=None, z=None):
        """Create translation table"""
        return str.maketrans(x, y, z)
