def show(a, b, c):
    print('a=', a, type(a))
    print('b=', b, type(b))
    print('c=', c, type(c))
import tkinter

class _WidgetVar:
    def __init__(self, value=''):
        self._v = value
    def set(self, v):
        self._v = v
    def get(self):
        return self._v

# widgets container for GUI elements
widgets = {}
widget_types = {}
_data = {}

def invoke_or_emit_event(cb):
    # helper to call callbacks; in emitted tests we call handlers directly
    cb()

# GUI line: # token-style types
widget_types['count'] = 'int'
widget_types['flag'] = 'bool'
widgets['count'] = _WidgetVar()
# Entry widget placeholder for count
widgets['flag'] = _WidgetVar()
# Entry widget placeholder for flag
# GUI line: # multi-line dict-style types
widget_types['x'] = 'int'
widget_types['y'] = 'float'
