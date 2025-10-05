from tools.type_checker import TypeChecker

def test_type_checker_ok():
    src = '''
def show(a, b):
    pass
GUI {
    types a:int b:bool
    addTextField("a")
    addTextField("b")
    addButton("Run", show(a, b))
}
'''
    checker = TypeChecker(src)
    errors = checker.check()
    assert not errors, f"Unexpected errors: {errors}"

def test_type_checker_missing_widget():
    src = '''
def show(a, b):
    pass
GUI {
    types a:int
    addTextField("a")
    addButton("Run", show(a, b))
}
'''
    checker = TypeChecker(src)
    errors = checker.check()
    assert any("not declared as widget" in e for e in errors)

def test_type_checker_arg_count():
    src = '''
def show(a, b):
    pass
GUI {
    types a:int b:bool
    addTextField("a")
    addTextField("b")
    addButton("Run", show(a))
}
'''
    checker = TypeChecker(src)
    errors = checker.check()
    assert any("expects 2 args" in e for e in errors)
