"""
cpj_python_utils.py
Utility functions for CPJ Python compiler module
"""
import subprocess
import sys

def run_python(source_file):
    subprocess.run([sys.executable, source_file])

def install_package(package):
    subprocess.run([sys.executable, '-m', 'pip', 'install', package])
