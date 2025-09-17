# Fallback emitted Python
def print_line(s):
    print(s)

class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            print_line("Error: Division by zero")
            return 0
        return a // b
    def abs(self, x):
        return abs(x)
    def max(self, a, b):
        return max(a, b)
    def min(self, a, b):
        return min(a, b)
def main():
    calc = Calculator()
    print_line("Scientific Calculator Demo")
    print_line("add(5, 3) = " + str(calc.add(5, 3)))
    print_line("sub(10, 4) = " + str(calc.sub(10, 4)))
    print_line("mul(6, 7) = " + str(calc.mul(6, 7)))
    print_line("div(20, 4) = " + str(calc.div(20, 4)))
    print_line("abs(-42) = " + str(calc.abs(-42)))
    print_line("max(8, 15) = " + str(calc.max(8, 15)))
    print_line("min(8, 15) = " + str(calc.min(8, 15)))
main()
