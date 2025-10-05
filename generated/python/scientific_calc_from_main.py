class Calculator:
    def add(self, a: int, b: int):
        return (a + b)
    def sub(self, a: int, b: int):
        return (a - b)
    def mul(self, a: int, b: int):
        return (a * b)
    def div(self, a: int, b: int):
        if (b == 0):
            print('Error: Division by zero')
            return 0
        return (a // b)
    def abs(self, x: int):
        return abs(x)
    def max(self, a: int, b: int):
        return max(a, b)
    def min(self, a: int, b: int):
        return min(a, b)
def main():
    calc = Calculator()
    print('Scientific Calculator Demo')
    print(('add(5, 3) = ' + str(calc.add(5, 3))))
    print(('sub(10, 4) = ' + str(calc.sub(10, 4))))
    print(('mul(6, 7) = ' + str(calc.mul(6, 7))))
    print(('div(20, 4) = ' + str(calc.div(20, 4))))
    print(('abs(-42) = ' + str(calc.abs((-42)))))
    print(('max(8, 15) = ' + str(calc.max(8, 15))))
    print(('min(8, 15) = ' + str(calc.min(8, 15))))

if __name__ == '__main__':
    main()
