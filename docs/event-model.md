
# CPJ Event Model & Runtime API

This document describes the event model for wiring CPJ GUI and system events to handlers across Python, Java, and C++.

## Objectives
- Handlers receive a mapping/dictionary of widget values and event metadata.
- Events are delivered synchronously by default; async option for long-running handlers.
- Error propagation for handler exceptions and coercion errors.


## Event JSON Schema
```json
{
	"type": "string",           // Event type (e.g., "button.click")
	"payload": { ... },           // JSON-serializable data
	"source": "string",         // (optional) Originating runtime/language
	"target": "string",         // (optional) Target handler or language
	"timestamp": "number",      // (optional) Event creation time (epoch ms)
	"id": "string",             // (optional) Unique event id (for replies)
	"reply_to": "string",       // (optional) Event id this is replying to
	"error": {                   // (optional) Error object if handler failed
		"type": "string",         // Error type/class
		"message": "string",      // Error message
		"traceback": "string"     // (optional) Traceback or details
	},
	"result": { ... }            // (optional) Handler return value (JSON)
}
```



## Delivery Semantics
- **Synchronous:** Handler is invoked immediately, result is returned in `result` field.
- **Asynchronous:** Event is queued and handled later (event loop or thread). Replies use `id`/`reply_to`.
- **Broadcast:** Event is delivered to all registered handlers.
- **Directed:** Event is delivered to a specific handler or runtime (via `target`).

## Error/Reply Semantics
- If a handler raises, the reply event includes an `error` object.
- Replies to events use the `id`/`reply_to` fields for correlation.

## Async/Event Queue Support
- Each runtime should support an event queue for async delivery.
- Events can be polled or pushed from the orchestrator/connector.


## Cross-Runtime Invocation
- Events are serialized as JSON and routed via the CPJ connector (Python orchestrator).
- Each runtime (C++, Python, Java) exposes a minimal API:
  - `emit_event(event)` — send event to orchestrator
  - `on_event(type, handler)` — register handler for event type
- The orchestrator dispatches events to the correct runtime(s) and handler(s).

## Minimal Runtime API

### Python
```python
def emit_event(event: dict):
	"""Send event to orchestrator (or local handler)."""
	...

def on_event(event_type: str, handler):
	"""Register handler for event type."""
	...
```

### C++ (pseudo)
```cpp
void emit_event(const Event& event); // Send event to orchestrator
void on_event(const std::string& type, std::function<void(const Event&)> handler); // Register handler
```

## Event Lifecycle
1. User action triggers widget event.
2. Runtime gathers widget data, applies coercion rules.
3. Runtime emits event (local or cross-runtime).
4. Handler returns a result or raises an exception; runtime logs and optionally surfaces the exception to the GUI.

## Interop Concerns
- When handlers are implemented across runtimes (e.g., Java GUI calling Python handler), use JSON over stdin/stdout or the connector module for structured exchange.
- For low-latency or high-throughput, design an RPC ABI (future work).

## Example (Python)
```python
from cpj_runtime import emit_event, on_event

def on_button_click(event):
	print("Button clicked!", event['payload'])

on_event('button.click', on_button_click)

# Somewhere else
emit_event({'type': 'button.click', 'payload': {'id': 'ok'}})
```

## Open Questions
- Should event delivery be strictly ordered? (Current: best-effort FIFO)
- How are errors/returns propagated across runtimes? (Current: error/result fields in reply event)
- Should events support reply/ack semantics? (Current: yes, via id/reply_to)

## Next Steps
- Implement error/reply support in all runtimes
- Add async/event queue support in Python, C++, Java
- Expand integration tests for cross-runtime event delivery and error propagation

Minimal runtime API (Python)

- `cpj_runtime.gather_widget_data(widget_map, types_map) -> dict` — returns coerced values + `_coercion_errors` if any
- `cpj_runtime.invoke_handler(fn, data) -> result` — calls the handler function with the data mapping

Event lifecycle

1. User action triggers widget event.
2. Runtime gathers widget data, applies coercion rules.
3. Runtime invokes handler (within same process or via connector to other runtime).
4. Handler returns a result or raises an exception; runtime logs and optionally surfaces the exception to the GUI.

Interop concerns

- When handlers are implemented across runtimes (e.g., Java GUI calling Python handler), use JSON over stdin/stdout or use the connector module for structured exchange.
- For low-latency or high-throughput, design an RPC ABI (future work).
