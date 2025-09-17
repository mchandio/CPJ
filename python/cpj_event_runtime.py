
# Enhanced CPJ event runtime API (Python)
import threading
import queue
import time
import uuid


_event_handlers = {}
_event_queue = queue.Queue()
_event_results = {}  # id -> result or error

def emit_event(event: dict, sync=True, wait_timeout=5):
    """Send event to all registered handlers for event['type']. If sync, wait for reply/result."""
    if 'id' not in event:
        event['id'] = str(uuid.uuid4())
    if sync:
        # Synchronous: call handlers directly, collect result/error
        handlers = _event_handlers.get(event['type'], [])
        reply = {'reply_to': event['id']}
        try:
            results = [h(event) for h in handlers]
            reply['result'] = results[0] if len(results) == 1 else results
        except Exception as e:
            reply['error'] = {'type': type(e).__name__, 'message': str(e)}
        _event_results[event['id']] = reply
        return reply
    else:
        # Async: put event in queue, return immediately
        _event_queue.put(event)
        return {'queued': True, 'id': event['id']}

def on_event(event_type: str, handler):
    """Register a handler for event type."""
    _event_handlers.setdefault(event_type, []).append(handler)

def poll_event(timeout=0.1):
    """Poll the event queue for the next event (async delivery)."""
    try:
        return _event_queue.get(timeout=timeout)
    except queue.Empty:
        return None

def get_event_result(event_id):
    """Get the result or error for a previously emitted event (by id)."""
    return _event_results.get(event_id)
