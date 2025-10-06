#!/usr/bin/env python3
"""
CPJ Test Runner

This script runs all CPJ tests and generates a comprehensive test report.
"""
import unittest
import sys
import os
from pathlib import Path
import time
import json
from typing import Dict, List, Any

def collect_tests() -> unittest.TestSuite:
    """Collect all test cases from test directory"""
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    return loader.discover(start_dir, pattern='test_*.py')

class CPJTestResult(unittest.TestResult):
    """Custom test result class for detailed reporting"""
    def __init__(self):
        super().__init__()
        self.successes: List[str] = []
        self.start_time = 0.0
        self.times: Dict[str, float] = {}

    def startTest(self, test):
        self.start_time = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        elapsed = time.time() - self.start_time
        test_name = self.get_test_name(test)
        self.successes.append(test_name)
        self.times[test_name] = elapsed
        super().addSuccess(test)

    def addError(self, test, err):
        elapsed = time.time() - self.start_time
        test_name = self.get_test_name(test)
        self.times[test_name] = elapsed
        super().addError(test, err)

    def addFailure(self, test, err):
        elapsed = time.time() - self.start_time
        test_name = self.get_test_name(test)
        self.times[test_name] = elapsed
        super().addFailure(test, err)

    @staticmethod
    def get_test_name(test) -> str:
        return f"{test.__class__.__name__}.{test._testMethodName}"

def generate_report(result: CPJTestResult) -> Dict[str, Any]:
    """Generate a detailed test report"""
    report = {
        "summary": {
            "total": result.testsRun,
            "passed": len(result.successes),
            "failed": len(result.failures),
            "errors": len(result.errors),
            "skipped": len(result.skipped)
        },
        "tests": {
            "passed": result.successes,
            "failed": [(self.get_test_name(test), err) for test, err in result.failures],
            "errors": [(self.get_test_name(test), err) for test, err in result.errors],
            "skipped": [self.get_test_name(test) for test in result.skipped]
        },
        "timing": {
            "total": sum(result.times.values()),
            "average": sum(result.times.values()) / len(result.times) if result.times else 0,
            "by_test": result.times
        }
    }
    return report

def save_report(report: Dict[str, Any], output_file: str):
    """Save test report to a file"""
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)

def print_report_summary(report: Dict[str, Any]):
    """Print a summary of the test results"""
    summary = report["summary"]
    print("\nCPJ Test Results Summary")
    print("=" * 50)
    print(f"Total Tests: {summary['total']}")
    print(f"Passed: {summary['passed']}")
    print(f"Failed: {summary['failed']}")
    print(f"Errors: {summary['errors']}")
    print(f"Skipped: {summary['skipped']}")
    print("\nTiming Information")
    print("-" * 50)
    print(f"Total Time: {report['timing']['total']:.2f}s")
    print(f"Average Time: {report['timing']['average']:.2f}s")

def main():
    # Collect and run tests
    suite = collect_tests()
    result = CPJTestResult()
    suite.run(result)
    
    # Generate and save report
    report = generate_report(result)
    save_report(report, "test_report.json")
    print_report_summary(report)
    
    # Return appropriate exit code
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(main())