from python import cpj_event_runtime as er

def test_event_emit_and_handle():
    results = []
    def handler(event):
        results.append(event['payload']['msg'])
    er.on_event('test', handler)
    er.emit_event({'type': 'test', 'payload': {'msg': 'hello'}})
    assert results == ['hello']
