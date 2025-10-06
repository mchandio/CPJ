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
import cpj_orchestrator
import time


class TestCPJIntegration(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(__file__).parent
        self.samples_dir = self.test_dir / 'samples'
        self.samples_dir.mkdir(exist_ok=True)
        self.dep_manager = DependencyManager()
        self.parser = IndentAwareParser()
        self.runtime = CPJRuntime()
        self.orchestrator = cpj_orchestrator

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

def process_result(result):
    if result["status"] == "success":
        return result["value"] * 2
    return None

result = send_to_cpp({"value": 42, "operation": "double"})
processed = process_result(result)
print(f"Final result: {processed}")
"""
        # C++ code that processes data and sends to Java
        cpp_code = """
#include "cpj_runtime.h"
int main() {
    auto data = cpj::receive_from_python();
    data["processed"] = true;
    if (data.contains("operation") && data["operation"] == "double") {
        data["value"] = data["value"].get<int>() * 2;
    }
    cpj::forward_to_java(data);
    return 0;
}
"""
        # Java code that receives and verifies data
        java_code = """
public class DataProcessor {
    public static void main(String[] args) {
        var data = CPJRuntime.receiveFromCpp();
        data.put("status", "success");
        System.out.println("Processed in Java: " + data.toString());
        CPJRuntime.returnToPython(data);
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
        assert isinstance(py_output, str)
        self.assertIn("Final result: 168", py_output)  # 42 * 2 * 2
        
    def test_error_handling(self):
        """Test error propagation across languages"""
        py_code = """
try:
    result = runtime.forward_to_cpp({"command": "divide", "x": 10, "y": 0})
except CPJRuntimeError as e:
    print(f"Caught error: {e}")
"""
        cpp_code = """
#include "cpj_runtime.h"
int main() {
    auto data = cpj::receive_from_python();
    try {
        if (data["command"] == "divide") {
            int x = data["x"].get<int>();
            int y = data["y"].get<int>();
            if (y == 0) {
                throw cpj::CPJException("Division by zero");
            }
            data["result"] = x / y;
        }
    } catch (const std::exception& e) {
        cpj::throw_error(e.what());
    }
    return 0;
}
"""
        py_path = self.create_test_file('error_test.py', py_code)
        cpp_path = self.create_test_file('error_handler.cpp', cpp_code)
        
        py_output = run_code(str(py_path), 'python')
        self.assertIsNotNone(py_output)
        assert isinstance(py_output, str)
        self.assertIn("Division by zero", py_output)
        
    def test_shared_memory_communication(self):
        """Test shared memory communication between languages"""
        py_code = """
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
shared_id = runtime.share_memory(data)
result = runtime.forward_to_cpp({"command": "process_matrix", "shared_id": shared_id})
processed_data = runtime.get_shared_memory(result["output_id"])
print(f"Sum of processed data: {processed_data.sum()}")
"""
        cpp_code = """
#include "cpj_runtime.h"
#include <Eigen/Dense>

int main() {
    auto data = cpj::receive_from_python();
    if (data["command"] == "process_matrix") {
        std::string shared_id = data["shared_id"];
        auto matrix = cpj::get_shared_matrix(shared_id);
        matrix = matrix * 2.0;  // Double all values
        std::string output_id = cpj::share_matrix(matrix);
        data["output_id"] = output_id;
    }
    cpj::return_to_python(data);
    return 0;
}
"""
        py_path = self.create_test_file('shared_mem_test.py', py_code)
        cpp_path = self.create_test_file('matrix_processor.cpp', cpp_code)
        
        py_output = run_code(str(py_path), 'python')
        self.assertIsNotNone(py_output)
        assert isinstance(py_output, str)
        self.assertIn("Sum of processed data: 42.0", py_output)  # (1+2+3+4+5+6)*2=42
        
    def test_orchestrator(self):
        """Test the orchestrator functionality with multi-language code"""
        source = """
# Define house style in Python
def calculate_room_cost(width, length, height):
    base_cost = width * length * 100  # $100 per sq ft base cost
    if height > 8:
        base_cost *= 1.2  # 20% premium for high ceilings
    return base_cost

// C++ implementation for structural analysis
struct RoomDimensions {
    double width;
    double length;
    double height;
};

bool verify_structure(RoomDimensions dims) {
    double volume = dims.width * dims.length * dims.height;
    double ratio = dims.height / ((dims.width + dims.length) / 2);
    return volume <= 5000 && ratio <= 2.0;  // Basic structural constraints
}

# Java UI component for room visualization
public class RoomVisualizer {
    private double width;
    private double length;
    private double height;
    
    public void setDimensions(double w, double l, double h) {
        width = w;
        length = l;
        height = h;
    }
    
    public void draw() {
        System.out.println("Drawing room with dimensions: " + 
                         width + "x" + length + "x" + height);
    }
}
"""
        path = self.create_test_file('multi_lang_house.cpj', source)
        
        # Run through each language separately first
        self.orchestrator.run_python(path)
        python_result = subprocess.run([sys.executable, "-c", "from multi_lang_house import calculate_room_cost; print(calculate_room_cost(20, 15, 10))"], capture_output=True, text=True)
        self.assertEqual(float(python_result.stdout.strip()), 3600.0)  # 20*15*100*1.2
        
        self.orchestrator.run_cpp(path)
        cpp_result = subprocess.run(["./cpp_out"], input="20 15 10", capture_output=True, text=True)
        self.assertIn("Structure verification: true", cpp_result.stdout)
        
        self.orchestrator.run_java(path)
        java_result = subprocess.run(["java", "-cp", "java", "RoomVisualizer"], input="20 15 10", capture_output=True, text=True)
        self.assertIn("Drawing room with dimensions: 20x15x10", java_result.stdout)
        
        # Test GUI functionality
        self.orchestrator.run_gui_and_listen("RoomVisualizer", poll_secs=1)
        time.sleep(1)  # Give GUI time to initialize
        
        # Check for event file
        event_file = Path("/tmp/cpj_event.json")
        self.assertTrue(event_file.exists())
        
    def test_cross_language_debugging(self):
        """Test debug information propagation across languages"""
        py_code = """
runtime.set_debug(True)
debug_info = []

def debug_callback(info):
    debug_info.append(info)

runtime.set_debug_callback(debug_callback)
result = runtime.forward_to_cpp({"command": "complex_operation", "value": 42})
for info in debug_info:
    print(f"Debug: {info}")
"""
        cpp_code = """
#include "cpj_runtime.h"

void process_data(const nlohmann::json& data) {
    CPJ_DEBUG("Processing data in C++");
    // Simulate complex processing
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    CPJ_DEBUG("C++ processing complete");
}

int main() {
    auto data = cpj::receive_from_python();
    process_data(data);
    cpj::forward_to_java(data);
    return 0;
}
"""
        java_code = """
public class DebugProcessor {
    public static void main(String[] args) {
        CPJRuntime.debug("Starting Java processing");
        var data = CPJRuntime.receiveFromCpp();
        // Simulate complex processing
        Thread.sleep(100);
        CPJRuntime.debug("Java processing complete");
        CPJRuntime.returnToPython(data);
    }
}
"""
        py_path = self.create_test_file('debug_test.py', py_code)
        cpp_path = self.create_test_file('debug_processor.cpp', cpp_code)
        java_path = self.create_test_file('debug_handler.java', java_code)
        
        py_output = run_code(str(py_path), 'python')
        self.assertIsNotNone(py_output)
        assert isinstance(py_output, str)
        self.assertIn("Processing data in C++", py_output)
        self.assertIn("C++ processing complete", py_output)
        self.assertIn("Starting Java processing", py_output)
        self.assertIn("Java processing complete", py_output)

    def tearDown(self):
        """Clean up test files"""
        import shutil
        if self.samples_dir.exists():
            shutil.rmtree(self.samples_dir)


if __name__ == '__main__':
    unittest.main()