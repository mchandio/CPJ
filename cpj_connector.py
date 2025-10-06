"""
CPJ Connector: Cross-runtime event forwarding and reply protocol

Features:
- Unified event JSON schema and validation for bi-directional delivery
- Async event queue support (file-based, can be extended to sockets/IPC)
- Cross-runtime handler invocation (Python, C++, Java)
- Robust error handling and reply mechanism
"""

import json
import time
import uuid
import threading
import queue
import pkg_resources
import subprocess
import sys
import re
from typing import Dict, List, Set
import importlib
import importlib.util

import jsonschema
import os

EVENT_FILE = '/tmp/cpj_event.json'
REPLY_FILE = '/tmp/cpj_event_reply.json'
EVENT_QUEUE_FILE = '/tmp/cpj_event_queue.jsonl'  # For async event queue

# Dependency management
PYTHON_DEPS_FILE = 'requirements.txt'
CPP_DEPS_FILE = 'conanfile.txt'
JAVA_DEPS_FILE = 'pom.xml'

class DependencyManager:
    def __init__(self):
        self.python_deps: Set[str] = set()
        self.cpp_deps: Set[str] = set()
        self.java_deps: Set[str] = set()
        self._load_existing_deps()
    
    def _load_existing_deps(self):
        """Load existing dependencies from files"""
        if os.path.exists(PYTHON_DEPS_FILE):
            with open(PYTHON_DEPS_FILE) as f:
                self.python_deps.update(line.strip() for line in f if line.strip())
        
        if os.path.exists(CPP_DEPS_FILE):
            with open(CPP_DEPS_FILE) as f:
                self.cpp_deps.update(
                    line.strip() for line in f 
                    if line.strip() and not line.startswith('#')
                )
        
        if os.path.exists(JAVA_DEPS_FILE):
            # Parse Maven dependencies
            import xml.etree.ElementTree as ET
            if os.path.exists(JAVA_DEPS_FILE):
                tree = ET.parse(JAVA_DEPS_FILE)
                root = tree.getroot()
                for dep in root.findall('.//dependency'):
                    group_id = dep.find('groupId').text
                    artifact_id = dep.find('artifactId').text
                    version = dep.find('version').text
                    self.java_deps.add(f'{group_id}:{artifact_id}:{version}')
    
    def detect_python_imports(self, code: str) -> Set[str]:
        """Detect Python package imports from code"""
        imports = set()
        for line in code.split('\n'):
            if line.strip().startswith(('import ', 'from ')):
                module = line.split()[1].split('.')[0]
                if module not in ('os', 'sys', 'time', 'json', 'threading', 'queue'):
                    imports.add(module)
        return imports
    
    def detect_cpp_includes(self, code: str) -> Set[str]:
        """Detect C++ includes from code"""
        includes = set()
        for line in code.split('\n'):
            if line.strip().startswith('#include'):
                header = line.split('<')[-1].split('>')[0]
                if not header.endswith('.h'):
                    includes.add(header)
        return includes
    
    def detect_java_imports(self, code: str) -> Set[str]:
        """Detect Java package imports from code"""
        imports = set()
        for line in code.split('\n'):
            if line.strip().startswith('import '):
                package = line.split()[1].split('.')[0]
                if package not in ('java', 'javax'):
                    imports.add(package)
        return imports
    
    def install_python_deps(self, deps: Set[str]):
        """Install Python dependencies using pip"""
        if deps:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + list(deps))
            with open(PYTHON_DEPS_FILE, 'a') as f:
                for dep in deps:
                    f.write(f'{dep}\n')
    
    def install_cpp_deps(self, deps: Set[str]):
        """Install C++ dependencies using conan"""
        if deps:
            with open(CPP_DEPS_FILE, 'a') as f:
                for dep in deps:
                    f.write(f'{dep}\n')
            subprocess.check_call(['conan', 'install', '.'])
    
    def install_java_deps(self, deps: Set[str]):
        """Add Java dependencies to pom.xml"""
        if deps and os.path.exists(JAVA_DEPS_FILE):
            import xml.etree.ElementTree as ET
            tree = ET.parse(JAVA_DEPS_FILE)
            root = tree.getroot()
            deps_elem = root.find('.//dependencies')
            
            if deps_elem is not None:
                for dep in deps:
                    group_id, artifact_id, version = dep.split(':')
                    dep_elem = ET.SubElement(deps_elem, 'dependency')
                    ET.SubElement(dep_elem, 'groupId').text = group_id
                    ET.SubElement(dep_elem, 'artifactId').text = artifact_id
                    ET.SubElement(dep_elem, 'version').text = version
                
                tree.write(JAVA_DEPS_FILE)
                subprocess.check_call(['mvn', 'install'])

# Global dependency manager instance
dep_manager = DependencyManager()


# Unified event JSON schema for all runtimes
EVENT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "type": {"type": "string"},
        "payload": {"type": ["object", "null"]},
        "reply_to": {"type": "string"},
        "error": {"type": "string"},
        "runtime": {"type": "string"},
        "timestamp": {"type": "number"}
    },
    "required": ["id", "type"],
    "additionalProperties": True
}


def validate_event(event):
    """Validate an event dict against the unified EVENT_SCHEMA. Raises jsonschema.ValidationError if invalid."""
    jsonschema.validate(event, EVENT_SCHEMA)


def forward_event_to_runtime(event, runtime='python', wait_reply=True, timeout=5, async_mode=False):
    """
    Forward event to a runtime (simulated by writing to EVENT_FILE or queue).
    If async_mode is True, append to EVENT_QUEUE_FILE for async processing.
    Wait for reply if requested.
    """
    event = dict(event)
    if 'id' not in event:
        event['id'] = str(uuid.uuid4())
    event['timestamp'] = time.time()
    # Validate event before writing
    validate_event(event)
    if async_mode:
        # Append event to queue file (JSONL)
        with open(EVENT_QUEUE_FILE, 'a') as f:
            f.write(json.dumps(event) + '\n')
        return {'queued': True, 'id': event['id']}
    else:
        with open(EVENT_FILE, 'w') as f:
            f.write(json.dumps(event))
        if wait_reply:
            start = time.time()
            while time.time() - start < timeout:
                if os.path.exists(REPLY_FILE):
                    try:
                        with open(REPLY_FILE, 'r') as f:
                            reply = json.load(f)
                        if reply.get('reply_to') == event['id']:
                            os.remove(REPLY_FILE)
                            return reply
                    except Exception:
                        pass
                time.sleep(0.05)
            return {'error': {'type': 'Timeout', 'message': 'No reply received'}}
        return {'queued': True, 'id': event['id']}


def write_event_reply(reply):
    """Write a reply event to REPLY_FILE (simulates runtime reply)."""
    if 'reply_to' not in reply:
        reply['reply_to'] = reply.get('id', str(uuid.uuid4()))
    reply['timestamp'] = time.time()
    with open(REPLY_FILE, 'w') as f:
        f.write(json.dumps(reply))


# --- Async Event Queue Processor (Python example) ---
class EventQueueProcessor(threading.Thread):
    """Background thread to process async event queue and invoke handler callbacks."""
    def __init__(self, handler_map):
        super().__init__(daemon=True)
        self.handler_map = handler_map
        self.running = True

    def run(self):
        while self.running:
            try:
                if os.path.exists(EVENT_QUEUE_FILE):
                    with open(EVENT_QUEUE_FILE, 'r') as f:
                        lines = f.readlines()
                    if lines:
                        # Only process the first event (FIFO)
                        event = json.loads(lines[0])
                        # Remove processed event from queue
                        with open(EVENT_QUEUE_FILE, 'w') as f:
                            f.writelines(lines[1:])
                        # Validate and dispatch
                        try:
                            validate_event(event)
                            handler = self.handler_map.get(event['type'])
                            if handler:
                                handler(event)
                        except Exception as e:
                            print(f"EventQueueProcessor error: {e}")
                time.sleep(0.1)
            except Exception as e:
                print(f"EventQueueProcessor main loop error: {e}")

    def stop(self):
        self.running = False

"""
cpj_connector.py
Connector module for CPJ to enable communication between C++, Python, and Java
Includes async event queue processor and robust event delivery.
"""
import subprocess
import sys

def run_code(source_file: str, language: str) -> str | None:
    """
    Run code in any supported language (C++, Python, Java) with automatic dependency management
    
    Args:
        source_file: Path to the source file
        language: 'cpp', 'python', or 'java'
        
    Returns:
        stdout output from running the code
    """
    # Read source code
    with open(source_file, 'r') as f:
        code = f.read()
    
    # Detect and install dependencies
    if language == 'python':
        deps = dep_manager.detect_python_imports(code)
        if deps - dep_manager.python_deps:  # Only install new deps
            print(f"Installing Python dependencies: {deps - dep_manager.python_deps}")
            dep_manager.install_python_deps(deps - dep_manager.python_deps)
            dep_manager.python_deps.update(deps)
        
        result = subprocess.run([sys.executable, source_file], capture_output=True, text=True)
        return result.stdout
        
    elif language == 'cpp':
        deps = dep_manager.detect_cpp_includes(code)
        if deps - dep_manager.cpp_deps:  # Only install new deps
            print(f"Installing C++ dependencies: {deps - dep_manager.cpp_deps}")
            dep_manager.install_cpp_deps(deps - dep_manager.cpp_deps)
            dep_manager.cpp_deps.update(deps)
            
        result = subprocess.run(["g++", source_file, "-o", "cpp_out"])
        if result.returncode != 0:
            print("C++ compilation failed.")
            return None
        result = subprocess.run(["./cpp_out"], capture_output=True, text=True)
        return result.stdout
        
    elif language == 'java':
        deps = dep_manager.detect_java_imports(code)
        if deps - dep_manager.java_deps:  # Only install new deps
            print(f"Installing Java dependencies: {deps - dep_manager.java_deps}")
            dep_manager.install_java_deps(deps - dep_manager.java_deps)
            dep_manager.java_deps.update(deps)
            
        result = subprocess.run(["javac", source_file])
        if result.returncode != 0:
            print("Java compilation failed.")
            return None
        class_name = os.path.splitext(os.path.basename(source_file))[0]
        result = subprocess.run(["java", class_name], capture_output=True, text=True)
        return result.stdout
        
    else:
        raise ValueError(f"Unsupported language: {language}")

# Legacy run functions now consolidated into run_code above
"""
def run_cpp(source_file):
    result = subprocess.run(["g++", source_file, "-o", "cpp_out"])
    if result.returncode != 0:
        print("C++ compilation failed.")
        return None
    result = subprocess.run(["./cpp_out"], capture_output=True, text=True)
    return result.stdout

def run_python(source_file):
    result = subprocess.run([sys.executable, source_file], capture_output=True, text=True)
    return result.stdout

def run_java(source_file):
    result = subprocess.run(["javac", source_file])
    if result.returncode != 0:
        print("Java compilation failed.")
        return None
    class_name = os.path.splitext(os.path.basename(source_file))[0]
    result = subprocess.run(["java", class_name], capture_output=True, text=True)
    return result.stdout
"""

def exchange_data(data, filename):
    with open(filename, 'w') as f:
        f.write(data)

def read_data(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_event_json():
    path = '/tmp/cpj_event.json'
    if not os.path.exists(path):
        return None
    try:
        return read_data(path)
    except Exception as e:
        print('Error reading event json:', e)
        return None



# --- Integration Test Stub ---
def _integration_test():
    """Basic integration test for event delivery and async queue."""
    print("[TEST] Starting integration test...")
    # Test direct event delivery
    event = {"type": "test_event", "payload": {"msg": "hello"}}
    reply = forward_event_to_runtime(event, wait_reply=False)
    print("[TEST] Direct event delivery result:", reply)
    # Test async queue
    handler_called = []
    def handler(ev):
        print("[TEST] Handler called with:", ev)
        handler_called.append(ev)
    eqp = EventQueueProcessor({"test_event": handler})
    eqp.start()
    forward_event_to_runtime(event, async_mode=True)
    time.sleep(0.5)
    eqp.stop()
    eqp.join()
    assert handler_called, "Handler was not called for async event!"
    print("[TEST] Integration test passed.")


if __name__ == '__main__':
    # Simple CLI for integration: exchange_data <filename> <data...>
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        _integration_test()
        sys.exit(0)
    if len(sys.argv) >= 3:
        cmd = sys.argv[1]
        if cmd == 'exchange_data' and len(sys.argv) >= 4:
            filename = sys.argv[2]
            data = ' '.join(sys.argv[3:])
            with open(filename, 'w') as f:
                f.write(data)
            print('OK')
        elif cmd == 'read_data' and len(sys.argv) == 3:
            print(read_data(sys.argv[2]))
        else:
            print('Unknown command or bad args')

# Example usage:
# cpp_output = run_cpp('cpp/test.cpp')
# exchange_data(cpp_output, 'shared_data.txt')
# python_output = run_python('python/test.py')
# exchange_data(python_output, 'shared_data.txt')
# java_output = run_java('java/Test.java')
# exchange_data(java_output, 'shared_data.txt')
