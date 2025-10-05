import os
import sys
import json
import time
import subprocess
import importlib

import python.cpj_event_runtime as py_event
import cpj_connector as connector

def test_python_emit_and_python_consume_via_connector(tmp_path):
    # Simulate emitting an event in Python, writing to /tmp/cpj_event.json
    event = {'type': 'cross_test', 'payload': {'msg': 'hello from python'}}
    event_path = tmp_path / 'cpj_event.json'
    # Write event using connector
    connector.exchange_data(json.dumps(event), str(event_path))
    # Simulate another runtime reading the event
    data = connector.read_data(str(event_path))
    event2 = json.loads(data)
    assert event2['type'] == 'cross_test'
    assert event2['payload']['msg'] == 'hello from python'

def test_python_emit_and_cpp_consume_via_connector(tmp_path):
    # Simulate Python emitting, C++ consuming (C++ simulated in Python for test)
    event = {'type': 'cpp_test', 'payload': {'msg': 'hello cpp'}}
    event_path = tmp_path / 'cpj_event.json'
    connector.exchange_data(json.dumps(event), str(event_path))
    # Simulate C++ runtime reading the event file
    with open(event_path, 'r') as f:
        data = f.read()
    event2 = json.loads(data)
    assert event2['type'] == 'cpp_test'
    assert event2['payload']['msg'] == 'hello cpp'

def test_cpp_emit_and_python_consume_via_connector(tmp_path):
    # Simulate C++ emitting (write file), Python consuming
    event = {'type': 'py_test', 'payload': {'msg': 'hello python'}}
    event_path = tmp_path / 'cpj_event.json'
    # Simulate C++ writing event file
    with open(event_path, 'w') as f:
        f.write(json.dumps(event))
    # Python reads via connector
    data = connector.read_data(str(event_path))
    event2 = json.loads(data)
    assert event2['type'] == 'py_test'
    assert event2['payload']['msg'] == 'hello python'
