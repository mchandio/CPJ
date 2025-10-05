#include <gtest/gtest.h>
#include "cpj/test_framework.h"

using namespace cpj::test;

// Test the TestCase class
TEST(TestFrameworkTest, TestCaseBasics) {
    bool testRan = false;
    TestCase tc("sample_test", [&testRan]() { testRan = true; });
    
    ASSERT_FALSE(tc.passed());
    ASSERT_EQ(tc.getName(), "sample_test");
    
    tc.run();
    ASSERT_TRUE(tc.passed());
    ASSERT_TRUE(testRan);
    ASSERT_GT(tc.getDuration(), 0.0);
}

// Test the TestSuite class
TEST(TestFrameworkTest, TestSuiteBasics) {
    TestSuite suite("sample_suite");
    int counter = 0;
    
    suite.addTest("test1", [&counter]() { counter++; });
    suite.addTest("test2", [&counter]() { counter++; });
    
    ASSERT_EQ(suite.getTotalTests(), 2);
    suite.run();
    ASSERT_EQ(counter, 2);
    ASSERT_EQ(suite.getPassedTests(), 2);
}

// Test assertions
TEST(TestFrameworkTest, Assertions) {
    ASSERT_NO_THROW(assertEquals("test", "test", "Strings should match"));
    ASSERT_THROW(assertEquals("test", "fail", "Strings should not match"), std::runtime_error);
    
    ASSERT_NO_THROW(assertTrue(true, "Should be true"));
    ASSERT_THROW(assertTrue(false, "Should fail"), std::runtime_error);
}

// Test benchmarking
TEST(TestFrameworkTest, Benchmarking) {
    Benchmark bench("sample_benchmark");
    
    bench.start();
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    bench.stop();
    
    double elapsed = bench.getElapsedTime();
    ASSERT_GT(elapsed, 0.09);  // Allow for some timing variance
    ASSERT_LT(elapsed, 0.2);   // Upper bound check
}

// Test cross-language execution
TEST(TestFrameworkTest, CrossLanguageExecution) {
    ASSERT_NO_THROW(CrossLanguageTest::runPythonTest("print('Hello from Python')"));
    ASSERT_NO_THROW(CrossLanguageTest::runJavaTest("System.out.println(\"Hello from Java\");"));
    ASSERT_NO_THROW(CrossLanguageTest::runCppTest("std::cout << \"Hello from C++\" << std::endl;"));
}