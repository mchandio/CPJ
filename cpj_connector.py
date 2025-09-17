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


import jsonschema
import os

EVENT_FILE = '/tmp/cpj_event.json'
REPLY_FILE = '/tmp/cpj_event_reply.json'
EVENT_QUEUE_FILE = '/tmp/cpj_event_queue.jsonl'  # For async event queue


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
