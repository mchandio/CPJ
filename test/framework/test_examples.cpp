#include "test_framework.h"
#include <thread>
#include <chrono>

using namespace cpj::test;

// Example unit test for C++
CPJ_UNIT_TEST(SimpleAddition, TestLanguage::CPP)
{
    int result = 2 + 2;
    assertTrue(result == 4, "2 + 2 should equal 4");
    return {true, "Addition test passed", 0.0};
}

// Example performance test
CPJ_PERFORMANCE_TEST(ArraySortPerformance, TestLanguage::CPP)
{
    PerformanceMetrics metrics;
    std::vector<int> numbers(1000000);

    // Setup test data
    for (size_t i = 0; i < numbers.size(); ++i)
    {
        numbers[i] = rand() % 1000000;
    }

    metrics.start();
    std::sort(numbers.begin(), numbers.end());
    metrics.stop();

    metrics.addMetric("array_size", numbers.size());
    metrics.addMetric("sort_time_ms", metrics.getDuration());

    return {true, "Performance test completed", metrics.getDuration(), metrics.getMetrics()};
}

// Example integration test
CPJ_INTEGRATION_TEST(CrossLanguageCall, TestLanguage::CPP)
{
    // Test C++ calling Python
    bool pythonCallSuccessful = true; // Replace with actual Python call
    assertTrue(pythonCallSuccessful, "C++ to Python call failed");

    // Test C++ calling Java
    bool javaCallSuccessful = true; // Replace with actual Java call
    assertTrue(javaCallSuccessful, "C++ to Java call failed");

    return {true, "Cross-language integration test passed", 0.0};
}

int main()
{
    TestSuite suite("CPJ Core Tests");

    // Add tests to suite
    suite.addTest(std::make_shared<SimpleAdditionTest>());
    suite.addTest(std::make_shared<ArraySortPerformanceTest>());
    suite.addTest(std::make_shared<CrossLanguageCallTest>());

    // Run all tests
    suite.runAll();

    // Run specific test types
    std::cout << "\nRunning only performance tests:" << std::endl;
    suite.runByType(TestType::PERFORMANCE);

    // Run tests for specific language
    std::cout << "\nRunning only C++ tests:" << std::endl;
    suite.runByLanguage(TestLanguage::CPP);

    return 0;
}