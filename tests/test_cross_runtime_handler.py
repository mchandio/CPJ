import os
import json
import uuid
import python.cpj_event_runtime as er
import cpj_connector as connector

def test_cross_runtime_handler_invocation(tmp_path, monkeypatch):
    # Simulate Python emitting, C++ (simulated) handling, Python receiving reply
    event = {'type': 'cross_handler', 'payload': {'msg': 'from py'}}
    event_file = tmp_path / 'cpj_event.json'
    reply_file = tmp_path / 'cpj_event_reply.json'
    # Patch connector to use tmp_path
    monkeypatch.setattr(connector, 'EVENT_FILE', str(event_file))
    monkeypatch.setattr(connector, 'REPLY_FILE', str(reply_file))
    # Simulate C++ runtime polling for event and replying
    def cpp_runtime_sim():
        # Wait for event file
        for _ in range(20):
            if event_file.exists():
                with open(event_file, 'r') as f:
                    ev = json.load(f)
                # Simulate handler
                reply = {'reply_to': ev['id'], 'result': {'msg': 'handled by cpp'}}
                with open(reply_file, 'w') as f:
                    f.write(json.dumps(reply))
                os.remove(event_file)
                return True
            import time; time.sleep(0.05)
        return False
    # Start handler in background
    import threading
    t = threading.Thread(target=cpp_runtime_sim)
    t.start()
    # Python emits event and waits for reply
    reply = connector.forward_event_to_runtime(event, runtime='cpp', wait_reply=True, timeout=2)
    t.join()
    assert 'result' in reply and reply['result']['msg'] == 'handled by cpp'
