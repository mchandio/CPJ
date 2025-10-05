import unittest
from typing import Any, Callable, List, Optional
import time

class CPJTestCase(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.start_time: float = 0.0
        self.end_time: float = 0.0

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        self.end_time = time.time()

    def getDuration(self) -> float:
        return self.end_time - self.start_time

class CPJTestRunner:
    @staticmethod
    def run(test_cases: List[CPJTestCase]) -> None:
        suite = unittest.TestSuite()
        for test_case in test_cases:
            suite.addTest(test_case)
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)

def cpj_test(func: Callable) -> Callable:
    """Decorator for CPJ test functions"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper