from typing import Callable, List, Optional
import unittest
import time

class CPJTestCase:
    def __init__(self, name: str, test_func: Callable[[], None]):
        self.name = name
        self.test_func = test_func
        self.passed = False
        self.duration = 0.0

    def run(self) -> None:
        start_time = time.time()
        try:
            self.test_func()
            self.passed = True
        except Exception as e:
            print(f"Test {self.name} failed: {str(e)}")
            self.passed = False
        finally:
            self.duration = time.time() - start_time

class CPJTestSuite:
    def __init__(self, name: str):
        self.name = name
        self.tests: List[CPJTestCase] = []

    def add_test(self, name: str, test_func: Callable[[], None]) -> None:
        self.tests.append(CPJTestCase(name, test_func))

    def run(self) -> None:
        print(f"Running test suite: {self.name}")
        for test in self.tests:
            print(f"  Running test: {test.name}... ", end="")
            test.run()
            status = "PASSED" if test.passed else "FAILED"
            print(f"{status} ({test.duration:.3f}s)")

    @property
    def total_tests(self) -> int:
        return len(self.tests)

    @property
    def passed_tests(self) -> int:
        return sum(1 for test in self.tests if test.passed)

class CPJTestRunner:
    def __init__(self):
        self.suites: List[CPJTestSuite] = []

    def add_suite(self, suite: CPJTestSuite) -> None:
        self.suites.append(suite)

    def run_all(self) -> None:
        total_tests = 0
        passed_tests = 0
        total_time = 0.0

        for suite in self.suites:
            suite_start = time.time()
            suite.run()
            suite_time = time.time() - suite_start
            total_time += suite_time
            total_tests += suite.total_tests
            passed_tests += suite.passed_tests

        print("\nTest Summary:")
        print(f"Total Suites: {len(self.suites)}")
        print(f"Total Tests: {total_tests}")
        print(f"Passed Tests: {passed_tests}")
        print(f"Failed Tests: {total_tests - passed_tests}")
        print(f"Total Time: {total_time:.3f}s")

class CPJAssertions:
    @staticmethod
    def assert_equals(expected: any, actual: any, message: Optional[str] = None) -> None:
        assert expected == actual, message or f"Expected {expected}, but got {actual}"

    @staticmethod
    def assert_true(condition: bool, message: Optional[str] = None) -> None:
        assert condition, message or "Expected True"

    @staticmethod
    def assert_false(condition: bool, message: Optional[str] = None) -> None:
        assert not condition, message or "Expected False"

    @staticmethod
    def assert_none(value: any, message: Optional[str] = None) -> None:
        assert value is None, message or f"Expected None, but got {value}"

    @staticmethod
    def assert_not_none(value: any, message: Optional[str] = None) -> None:
        assert value is not None, message or "Expected not None"

class CPJBenchmark:
    def __init__(self, name: str):
        self.name = name
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None

    def start(self) -> None:
        self.start_time = time.time()

    def stop(self) -> None:
        if self.start_time is None:
            raise RuntimeError("Benchmark not started")
        self.end_time = time.time()

    def get_elapsed_time(self) -> float:
        if self.start_time is None or self.end_time is None:
            raise RuntimeError("Benchmark not complete")
        return self.end_time - self.start_time