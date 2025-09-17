"""Runtime helpers for CPJ-emitted Python code.

Provides small utilities to gather widget data and to invoke a function or
fall back to writing a simple event when no handler is available.
"""
import json
from typing import Any, Iterable, Optional


def gather_widget_data(widgets, widget_types=None) -> dict:
    """Collect values from a widgets mapping.

    Tries to call `.get()` on the widget value, otherwise calls the value
    if callable, otherwise stores None on error.
    """
    data = {}
    try:
        for k, v in widgets.items():
            val = None
            try:
                val = v.get()
            except Exception:
                try:
                    val = v()
                except Exception:
                    val = None
            # if there is a declared type for the widget, coerce accordingly
            declared = None
            try:
                if widget_types and k in widget_types:
                    declared = widget_types[k]
            except Exception:
                declared = None
            if declared:
                coerced = None
                try:
                    coerced = coerce_value_as(val, declared)
                except Exception:
                    coerced = coerce_value(val)
                    # attach an error marker for the widget indicating coercion failed
                    data.setdefault('_coercion_errors', {})
                    data['_coercion_errors'][k] = f"failed to coerce {val!r} as {declared}"
                data[k] = coerced
            else:
                data[k] = coerce_value(val)
    except Exception:
        # defensive: return what we have
        pass
    return data


def coerce_value(v):
    """Try to coerce string-like values into int, float or bool where appropriate.

    - If v is already not a string, return it as-is.
    - If v.lower() in ('true','false'), return boolean.
    - Else try int then float conversion; on failure return original string.
    """
    if v is None:
        return None
    if not isinstance(v, str):
        return v
    s = v.strip()
    if not s:
        return s
    low = s.lower()
    if low == 'true':
        return True
    if low == 'false':
        return False
    # try int
    try:
        return int(s)
    except Exception:
        pass
    try:
        return float(s)
    except Exception:
        pass
    return s


def coerce_value_as(v, declared: str):
    """Coerce v according to declared type name (e.g. 'int', 'float', 'bool', 'str')."""
    if declared is None:
        return coerce_value(v)
    dt = declared.strip().lower()
    if dt in ('str', 'string'):
        return None if v is None else str(v)
    if dt in ('int', 'integer'):
        try:
            return int(v)
        except Exception:
            try:
                return int(float(v))
            except Exception:
                # raise so caller can detect failure if desired
                raise
    if dt in ('float', 'double'):
        try:
            return float(v)
        except Exception:
            return coerce_value(v)
    if dt in ('bool', 'boolean'):
        if v is None:
            return False
        if isinstance(v, bool):
            return v
        s = str(v).strip().lower()
        if s in ('true', '1', 'yes', 'y'):
            return True
        if s in ('false', '0', 'no', 'n'):
            return False
        return bool(s)
    # unknown type: fallback
    return coerce_value(v)


def invoke_or_emit_event(fn: Optional[callable], args: Optional[Iterable[Any]], data: dict, button_text: Optional[str] = None):
    """Try to invoke `fn` with args or with `data`, fallback to writing an event file.

    - If `args` is an iterable, call fn(*args).
    - Otherwise, first try fn(data), then fn(), catching TypeError.
    - If fn is not callable or calls fail in a way we can't handle, write a small
      JSON event to /tmp/cpj_event.json containing the button text.
    """
    if callable(fn):
        try:
            if args is not None:
                # args is an iterable of evaluated arguments
                return fn(*args)
            # try passing the whole data mapping first
            try:
                return fn(data)
            except TypeError:
                return fn()
        except Exception as e:
            # surface errors but fall through to event write
            try:
                with open('/tmp/cpj_event.json', 'w') as f:
                    json.dump({'type': 'button_call_error', 'error': str(e), 'button': button_text}, f)
            except Exception:
                pass
            return None

    # not callable: write simple event fallback
    try:
        with open('/tmp/cpj_event.json', 'w') as f:
            json.dump({'type': 'button_click', 'button': button_text}, f)
    except Exception:
        pass
    return None
