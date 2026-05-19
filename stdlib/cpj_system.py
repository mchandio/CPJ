"""
CPJ System Module
Provides system operations for the CPJ programming language
"""

import os
import sys
import platform
import subprocess
import time


class System:
    """System operations"""

    # Command line arguments
    @staticmethod
    def argv():
        """Get command line arguments"""
        return sys.argv

    @staticmethod
    def argc():
        """Get number of command line arguments"""
        return len(sys.argv)

    # Exit
    @staticmethod
    def exit(code=0):
        """Exit program with status code"""
        sys.exit(code)

    # Environment variables
    @staticmethod
    def getenv(key, default=None):
        """Get environment variable"""
        return os.environ.get(key, default)

    @staticmethod
    def setenv(key, value):
        """Set environment variable"""
        os.environ[key] = str(value)

    @staticmethod
    def environ():
        """Get all environment variables"""
        return dict(os.environ)

    @staticmethod
    def has_env(key):
        """Check if environment variable exists"""
        return key in os.environ

    # Path operations
    @staticmethod
    def cwd():
        """Get current working directory"""
        return os.getcwd()

    @staticmethod
    def chdir(path):
        """Change current working directory"""
        os.chdir(path)

    @staticmethod
    def home():
        """Get user home directory"""
        return os.path.expanduser("~")

    @staticmethod
    def temp():
        """Get temporary directory"""
        import tempfile
        return tempfile.gettempdir()

    # Platform information
    @staticmethod
    def platform():
        """Get platform name (linux, windows, darwin)"""
        return sys.platform

    @staticmethod
    def os_name():
        """Get OS name"""
        return os.name

    @staticmethod
    def arch():
        """Get architecture (x86_64, arm64, etc.)"""
        return platform.machine()

    @staticmethod
    def python_version():
        """Get Python version"""
        return platform.python_version()

    @staticmethod
    def system_info():
        """Get detailed system information"""
        return {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'machine': platform.machine(),
            'processor': platform.processor(),
            'python_version': platform.python_version()
        }

    # Process execution
    @staticmethod
    def exec(command, shell=True, capture=True):
        """Execute shell command"""
        try:
            if capture:
                result = subprocess.run(
                    command,
                    shell=shell,
                    capture_output=True,
                    text=True
                )
                return {
                    'code': result.returncode,
                    'stdout': result.stdout,
                    'stderr': result.stderr,
                    'success': result.returncode == 0
                }
            else:
                code = subprocess.call(command, shell=shell)
                return {
                    'code': code,
                    'stdout': '',
                    'stderr': '',
                    'success': code == 0
                }
        except Exception as e:
            return {
                'code': -1,
                'stdout': '',
                'stderr': str(e),
                'success': False
            }

    @staticmethod
    def run(command, *args):
        """Run command with arguments"""
        cmd_list = [command] + list(args)
        return System.exec(' '.join(cmd_list))

    # Time operations
    @staticmethod
    def sleep(seconds):
        """Sleep for specified seconds"""
        time.sleep(seconds)

    @staticmethod
    def timestamp():
        """Get current Unix timestamp"""
        return time.time()

    @staticmethod
    def time_ns():
        """Get current time in nanoseconds"""
        return time.time_ns()

    # Process information
    @staticmethod
    def pid():
        """Get current process ID"""
        return os.getpid()

    @staticmethod
    def ppid():
        """Get parent process ID"""
        return os.getppid()

    # Path utilities
    @staticmethod
    def path_join(*parts):
        """Join path components"""
        return os.path.join(*parts)

    @staticmethod
    def path_split(path):
        """Split path into directory and filename"""
        return os.path.split(path)

    @staticmethod
    def path_dirname(path):
        """Get directory name from path"""
        return os.path.dirname(path)

    @staticmethod
    def path_basename(path):
        """Get base name from path"""
        return os.path.basename(path)

    @staticmethod
    def path_exists(path):
        """Check if path exists"""
        return os.path.exists(path)

    @staticmethod
    def path_isabs(path):
        """Check if path is absolute"""
        return os.path.isabs(path)

    @staticmethod
    def path_abspath(path):
        """Get absolute path"""
        return os.path.abspath(path)

    @staticmethod
    def path_realpath(path):
        """Get real path (resolves symlinks)"""
        return os.path.realpath(path)

    # Directory operations
    @staticmethod
    def listdir(path='.'):
        """List directory contents"""
        return os.listdir(path)

    @staticmethod
    def mkdir(path, parents=False):
        """Create directory"""
        if parents:
            os.makedirs(path, exist_ok=True)
        else:
            os.mkdir(path)

    @staticmethod
    def rmdir(path):
        """Remove directory"""
        os.rmdir(path)

    @staticmethod
    def remove(path):
        """Remove file"""
        os.remove(path)

    @staticmethod
    def rename(src, dst):
        """Rename file or directory"""
        os.rename(src, dst)

    # Standard streams
    @staticmethod
    def stdin_read():
        """Read from stdin"""
        return sys.stdin.read()

    @staticmethod
    def stdin_readline():
        """Read line from stdin"""
        return sys.stdin.readline()

    @staticmethod
    def stdout_write(text):
        """Write to stdout"""
        sys.stdout.write(str(text))
        sys.stdout.flush()

    @staticmethod
    def stderr_write(text):
        """Write to stderr"""
        sys.stderr.write(str(text))
        sys.stderr.flush()

    # Input/Output
    @staticmethod
    def input(prompt=''):
        """Read line from user input"""
        return input(prompt)

    @staticmethod
    def print(*args, sep=' ', end='\n'):
        """Print to stdout"""
        print(*args, sep=sep, end=end)


# Convenience functions
def exit(code=0):
    """Exit program"""
    System.exit(code)


def getenv(key, default=None):
    """Get environment variable"""
    return System.getenv(key, default)


def exec_command(cmd):
    """Execute command"""
    return System.exec(cmd)


def sleep(seconds):
    """Sleep"""
    System.sleep(seconds)
