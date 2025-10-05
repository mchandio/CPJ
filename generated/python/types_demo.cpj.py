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
widgets['x'] = _WidgetVar()
# Entry widget placeholder for x
widgets['y'] = _WidgetVar()
# Entry widget placeholder for y
# GUI line: # per-field override
widgets['c'] = _WidgetVar()
widget_types['c'] = 'str'
# Entry widget placeholder for c
def _on_click_0():
    # generated handler for button Run
    __var_c = widgets.get('c').get()
    try:
        if isinstance(__var_c, str):
            if __var_c.isdigit(): __var_c = int(__var_c)
            else:
                try:
                    __var_c = float(__var_c)
                except: pass
    except Exception:
        _data.setdefault('_coercion_errors', []).append('c')
    __var_count = widgets.get('count').get()
    try:
        if isinstance(__var_count, str):
            if __var_count.isdigit(): __var_count = int(__var_count)
            else:
                try:
                    __var_count = float(__var_count)
                except: pass
    except Exception:
        _data.setdefault('_coercion_errors', []).append('count')
    __var_flag = widgets.get('flag').get()
    try:
        if isinstance(__var_flag, str):
            if __var_flag.isdigit(): __var_flag = int(__var_flag)
            else:
                try:
                    __var_flag = float(__var_flag)
                except: pass
    except Exception:
        _data.setdefault('_coercion_errors', []).append('flag')
    show(__var_count, __var_flag, __var_c)
widgets['btn0'] = tkinter.Button(text='Run')
# wire button Run -> _on_click_0
widgets['btn0'].configure(command=_on_click_0)
# GUI show() called - runtime would start mainloop
