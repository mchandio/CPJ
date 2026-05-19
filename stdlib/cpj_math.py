"""
CPJ Math Module
Provides mathematical functions for the CPJ programming language
"""

import math


class Math:
    """Mathematical functions and constants"""

    # Constants
    PI = math.pi
    E = math.e
    TAU = math.tau
    INF = math.inf
    NAN = math.nan

    # Basic operations
    @staticmethod
    def abs(x):
        """Return absolute value"""
        return abs(x)

    @staticmethod
    def ceil(x):
        """Return ceiling of x"""
        return math.ceil(x)

    @staticmethod
    def floor(x):
        """Return floor of x"""
        return math.floor(x)

    @staticmethod
    def round(x, digits=0):
        """Round to given number of digits"""
        return round(x, digits)

    @staticmethod
    def trunc(x):
        """Truncate x to integer"""
        return math.trunc(x)

    # Power and logarithmic
    @staticmethod
    def sqrt(x):
        """Return square root"""
        return math.sqrt(x)

    @staticmethod
    def pow(x, y):
        """Return x raised to power y"""
        return math.pow(x, y)

    @staticmethod
    def exp(x):
        """Return e raised to power x"""
        return math.exp(x)

    @staticmethod
    def log(x, base=math.e):
        """Return logarithm of x to given base"""
        return math.log(x, base)

    @staticmethod
    def log10(x):
        """Return base-10 logarithm"""
        return math.log10(x)

    @staticmethod
    def log2(x):
        """Return base-2 logarithm"""
        return math.log2(x)

    # Trigonometric functions
    @staticmethod
    def sin(x):
        """Return sine of x (in radians)"""
        return math.sin(x)

    @staticmethod
    def cos(x):
        """Return cosine of x (in radians)"""
        return math.cos(x)

    @staticmethod
    def tan(x):
        """Return tangent of x (in radians)"""
        return math.tan(x)

    @staticmethod
    def asin(x):
        """Return arc sine of x (in radians)"""
        return math.asin(x)

    @staticmethod
    def acos(x):
        """Return arc cosine of x (in radians)"""
        return math.acos(x)

    @staticmethod
    def atan(x):
        """Return arc tangent of x (in radians)"""
        return math.atan(x)

    @staticmethod
    def atan2(y, x):
        """Return atan(y/x) in radians"""
        return math.atan2(y, x)

    # Hyperbolic functions
    @staticmethod
    def sinh(x):
        """Return hyperbolic sine"""
        return math.sinh(x)

    @staticmethod
    def cosh(x):
        """Return hyperbolic cosine"""
        return math.cosh(x)

    @staticmethod
    def tanh(x):
        """Return hyperbolic tangent"""
        return math.tanh(x)

    # Angular conversion
    @staticmethod
    def degrees(x):
        """Convert radians to degrees"""
        return math.degrees(x)

    @staticmethod
    def radians(x):
        """Convert degrees to radians"""
        return math.radians(x)

    # Special functions
    @staticmethod
    def factorial(x):
        """Return factorial of x"""
        return math.factorial(x)

    @staticmethod
    def gcd(a, b):
        """Return greatest common divisor"""
        return math.gcd(a, b)

    @staticmethod
    def lcm(a, b):
        """Return least common multiple"""
        return math.lcm(a, b)

    # Comparison
    @staticmethod
    def max(*args):
        """Return maximum value"""
        return max(args)

    @staticmethod
    def min(*args):
        """Return minimum value"""
        return min(args)

    @staticmethod
    def sum(iterable):
        """Return sum of iterable"""
        return sum(iterable)

    # Floating point operations
    @staticmethod
    def isnan(x):
        """Check if x is NaN"""
        return math.isnan(x)

    @staticmethod
    def isinf(x):
        """Check if x is infinite"""
        return math.isinf(x)

    @staticmethod
    def isfinite(x):
        """Check if x is finite"""
        return math.isfinite(x)

    @staticmethod
    def copysign(x, y):
        """Return x with sign of y"""
        return math.copysign(x, y)

    # Statistical functions
    @staticmethod
    def mean(numbers):
        """Calculate arithmetic mean"""
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers):
        """Calculate median"""
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        if n % 2 == 0:
            return (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
        else:
            return sorted_nums[n//2]

    @staticmethod
    def variance(numbers):
        """Calculate variance"""
        m = Math.mean(numbers)
        return sum((x - m) ** 2 for x in numbers) / len(numbers)

    @staticmethod
    def stddev(numbers):
        """Calculate standard deviation"""
        return Math.sqrt(Math.variance(numbers))
