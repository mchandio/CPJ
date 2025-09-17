print('Hello, CPJ World!')
def greet(name):
    print(('Hello ' + name))
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

# label: addLabel("Hi from CPJ")
widgets['name'] = _WidgetVar()
# Entry widget placeholder for name
def _on_click_0():
    # generated handler for button Greet
    pass
widgets['btn0'] = tkinter.Button(text='Greet')
# wire button Greet -> _on_click_0
widgets['btn0'].configure(command=_on_click_0)
# GUI show() called - runtime would start mainloop
