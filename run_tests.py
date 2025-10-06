"""
Test runner for the CPJ language test suite.
"""
import unittest
import sys
import os
from typing import List, Tuple
import time

def run_test_suite() -> Tuple[int, int, List[str]]:
    """Run all CPJ language tests and return results"""
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Prepare result collection
    results = []
    class TestResult(unittest.TestResult):
        def addError(self, test, err):
            results.append(f"Error in {test}: {err}")
            super().addError(test, err)
            
        def addFailure(self, test, err):
            results.append(f"Failure in {test}: {err}")
            super().addFailure(test, err)
    
    # Run tests
    result = TestResult()
    start_time = time.time()
    suite.run(result)
    end_time = time.time()
    
    # Calculate statistics
    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests
    
    # Print summary
    print("\n=== CPJ Language Test Results ===")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    if results:
        print("\nFailures and Errors:")
        for r in results:
            print(f"- {r}")
            
    return total_tests, failed_tests, results

def main():
    """Main entry point for test runner"""
    total, failed, results = run_test_suite()
    
    # Set exit code based on test results
    if failed > 0:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()