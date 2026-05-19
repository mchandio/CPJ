"""
CPJ File I/O Module
Provides file operations for the CPJ programming language
"""

import os
import shutil


class File:
    """File operations"""

    @staticmethod
    def read(path):
        """Read entire file contents"""
        with open(path, 'r') as f:
            return f.read()

    @staticmethod
    def write(path, content):
        """Write content to file"""
        with open(path, 'w') as f:
            f.write(content)

    @staticmethod
    def append(path, content):
        """Append content to file"""
        with open(path, 'a') as f:
            f.write(content)

    @staticmethod
    def readlines(path):
        """Read file as list of lines"""
        with open(path, 'r') as f:
            return f.readlines()

    @staticmethod
    def writelines(path, lines):
        """Write list of lines to file"""
        with open(path, 'w') as f:
            f.writelines(lines)

    @staticmethod
    def exists(path):
        """Check if file exists"""
        return os.path.exists(path)

    @staticmethod
    def delete(path):
        """Delete a file"""
        if os.path.exists(path):
            os.remove(path)
            return True
        return False

    @staticmethod
    def copy(src, dst):
        """Copy file from src to dst"""
        shutil.copy2(src, dst)

    @staticmethod
    def move(src, dst):
        """Move file from src to dst"""
        shutil.move(src, dst)

    @staticmethod
    def size(path):
        """Get file size in bytes"""
        return os.path.getsize(path)

    @staticmethod
    def isfile(path):
        """Check if path is a file"""
        return os.path.isfile(path)

    @staticmethod
    def isdir(path):
        """Check if path is a directory"""
        return os.path.isdir(path)


class FileHandle:
    """File handle for context manager support"""

    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False


def open_file(path, mode='r'):
    """Open a file and return a file handle"""
    return FileHandle(path, mode)


# Backwards compatibility
open = open_file
