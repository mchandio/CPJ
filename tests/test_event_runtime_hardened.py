import python.cpj_event_runtime as er
import uuid

def test_event_error_and_reply():
    results = []
    def handler(event):
        if event['payload']['fail']:
            raise ValueError('fail!')
        return {'ok': True}
    er.on_event('reply_test', handler)
    # Success case
    event = {'type': 'reply_test', 'payload': {'fail': False}}
    reply = er.emit_event(event)
    assert 'result' in reply and reply['result'] == {'ok': True}
    # Error case
    event2 = {'type': 'reply_test', 'payload': {'fail': True}}
    reply2 = er.emit_event(event2)
    assert 'error' in reply2 and reply2['error']['type'] == 'ValueError'

def test_event_async_queue():
    # Register handler that just echoes
    def handler(event):
        return event['payload']
    er.on_event('async_test', handler)
    # Emit async event
    event = {'type': 'async_test', 'payload': {'msg': 'hi'}}
    er.emit_event(event, sync=False)
    # Poll event queue
    queued = er.poll_event(timeout=1)
    assert queued is not None and queued['type'] == 'async_test'
