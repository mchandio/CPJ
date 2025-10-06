"""
CPJ Integration Test Suite

This module provides comprehensive testing for CPJ's multi-language integration,
including dependency management, code optimization, and cross-language communication.
"""
import unittest
import os
import sys
import subprocess
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from cpj_connector import run_code, DependencyManager
from cpj_parser import IndentAwareParser
from cpj_runtime import CPJRuntime


class TestCPJIntegration(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(__file__).parent
        self.samples_dir = self.test_dir / 'samples'
        self.samples_dir.mkdir(exist_ok=True)
        self.dep_manager = DependencyManager()
        self.parser = IndentAwareParser()
        self.runtime = CPJRuntime()

    def create_test_file(self, filename: str, content: str) -> Path:
        """Helper to create test files"""
        path = self.samples_dir / filename
        path.write_text(content)
        return path

    def test_python_dependency_detection(self):
        """Test Python dependency detection and installation"""
        code = """
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data):
    return np.mean(data)
"""
        path = self.create_test_file('python_deps.py', code)
        deps = self.dep_manager.detect_python_imports(code)
        self.assertIn('numpy', deps)
        self.assertIn('pandas', deps)
        self.assertIn('matplotlib', deps)

    def test_cpp_dependency_detection(self):
        """Test C++ dependency detection"""
        code = """
#include <boost/algorithm/string.hpp>
#include <nlohmann/json.hpp>
#include <fmt/format.h>

int main() {
    return 0;
}
"""
        path = self.create_test_file('cpp_deps.cpp', code)
        deps = self.dep_manager.detect_cpp_includes(code)
        self.assertIn('boost', deps)
        self.assertIn('nlohmann/json.hpp', deps)
        self.assertIn('fmt/format.h', deps)

    def test_java_dependency_detection(self):
        """Test Java dependency detection"""
        code = """
import org.apache.commons.lang3.StringUtils;
import com.google.gson.Gson;
import org.slf4j.Logger;

public class TestClass {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
"""
        path = self.create_test_file('java_deps.java', code)
        deps = self.dep_manager.detect_java_imports(code)
        self.assertIn('org.apache.commons', deps)
        self.assertIn('com.google.gson', deps)
        self.assertIn('org.slf4j', deps)

    def test_python_optimization(self):
        """Test Python code optimization"""
        code = """
const PI = 3.14159
const RADIUS = 5.0

def calculate_area():
    return PI * RADIUS * RADIUS

def main():
    if False:
        print("Dead code")
    area = calculate_area()
    print(f"Area: {area}")
"""
        path = self.create_test_file('python_opt.py', code)
        tree = self.parser.parse_code(code)
        self.assertIsNotNone(tree)
        # Verify optimizations were applied
        optimized = str(tree)
        self.assertNotIn("Dead code", optimized)
        self.assertIn("78.53975", optimized)  # PI * RADIUS * RADIUS

    def test_cross_language_communication(self):
        """Test communication between Python, C++, and Java"""
        # Python code that sends data to C++
        py_code = """
def send_to_cpp(data):
    return runtime.forward_to_cpp(data)

result = send_to_cpp({"value": 42})
print(result)
"""
        # C++ code that processes data and sends to Java
        cpp_code = """
#include "cpj_runtime.h"
int main() {
    auto data = cpj::receive_from_python();
    data["processed"] = true;
    cpj::forward_to_java(data);
    return 0;
}
"""
        # Java code that receives and verifies data
        java_code = """
public class DataProcessor {
    public static void main(String[] args) {
        var data = CPJRuntime.receiveFromCpp();
        System.out.println("Received: " + data.toString());
    }
}
"""
        # Create test files
        py_path = self.create_test_file('sender.py', py_code)
        cpp_path = self.create_test_file('processor.cpp', cpp_code)
        java_path = self.create_test_file('receiver.java', java_code)

        # Run the communication test
        py_output = run_code(str(py_path), 'python')
        self.assertIsNotNone(py_output)
        self.assertIn("42", py_output)

    def tearDown(self):
        """Clean up test files"""
        import shutil
        if self.samples_dir.exists():
            shutil.rmtree(self.samples_dir)


if __name__ == '__main__':
    unittest.main()