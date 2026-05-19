"""
CPJ JSON Module
Provides JSON parsing and generation for the CPJ programming language
"""

import json


class JSON:
    """JSON operations"""

    @staticmethod
    def parse(json_string):
        """Parse JSON string to Python object"""
        return json.loads(json_string)

    @staticmethod
    def stringify(obj, indent=None, sort_keys=False):
        """Convert Python object to JSON string"""
        return json.dumps(obj, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def load(filepath):
        """Load JSON from file"""
        with open(filepath, 'r') as f:
            return json.load(f)

    @staticmethod
    def save(filepath, obj, indent=2, sort_keys=False):
        """Save object as JSON to file"""
        with open(filepath, 'w') as f:
            json.dump(obj, f, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def pretty(obj, indent=2):
        """Pretty print JSON"""
        return json.dumps(obj, indent=indent, sort_keys=True)

    @staticmethod
    def loads(s):
        """Alias for parse"""
        return json.loads(s)

    @staticmethod
    def dumps(obj, **kwargs):
        """Alias for stringify with options"""
        return json.dumps(obj, **kwargs)

    @staticmethod
    def validate(json_string):
        """Check if string is valid JSON"""
        try:
            json.loads(json_string)
            return True
        except (json.JSONDecodeError, ValueError):
            return False


class JSONEncoder:
    """Custom JSON encoder"""

    @staticmethod
    def encode_custom(obj):
        """Encode custom objects to JSON-serializable format"""
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
            return list(obj)
        else:
            return str(obj)


class JSONDecoder:
    """Custom JSON decoder"""

    @staticmethod
    def decode_custom(dct):
        """Decode JSON with custom handling"""
        return dct


# Convenience functions
def parse(s):
    """Parse JSON string"""
    return JSON.parse(s)


def stringify(obj, indent=None):
    """Convert to JSON string"""
    return JSON.stringify(obj, indent=indent)


def load_file(path):
    """Load JSON from file"""
    return JSON.load(path)


def save_file(path, obj, indent=2):
    """Save JSON to file"""
    return JSON.save(path, obj, indent=indent)
