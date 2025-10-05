#include "test_framework.h"
#include <stdexcept>
#include <iostream>
#include <algorithm>

namespace cpj::test
{

    // TestCase implementation
    TestCase::TestCase(const std::string &n, TestType t, TestLanguage l)
        : name(n), type(t), language(l) {}

    // TestSuite implementation
    TestSuite::TestSuite(const std::string &n) : name(n) {}

    void TestSuite::addTest(std::shared_ptr<TestCase> test)
    {
        tests.push_back(test);
    }

    void TestSuite::runAll()
    {
        results.clear();
        for (const auto &test : tests)
        {
            std::cout << "Running test: " << test->getName() << "..." << std::endl;
            try
            {
                test->setUp();
                TestResult result = test->run();
                test->tearDown();
                results.push_back(result);
                std::cout << (result.passed ? "PASSED" : "FAILED") << ": "
                          << test->getName() << " (" << result.duration_ms << "ms)"
                          << std::endl;
                if (!result.message.empty())
                {
                    std::cout << "Message: " << result.message << std::endl;
                }
            }
            catch (const std::exception &e)
            {
                results.push_back({false, e.what(), 0.0});
                std::cout << "ERROR: " << test->getName() << " - " << e.what() << std::endl;
            }
        }
    }

    void TestSuite::runByType(TestType type)
    {
        auto filtered = tests;
        filtered.erase(
            std::remove_if(filtered.begin(), filtered.end(),
                           [type](const auto &test)
                           { return test->getType() != type; }),
            filtered.end());
        tests.swap(filtered);
        runAll();
        tests.swap(filtered);
    }

    void TestSuite::runByLanguage(TestLanguage lang)
    {
        auto filtered = tests;
        filtered.erase(
            std::remove_if(filtered.begin(), filtered.end(),
                           [lang](const auto &test)
                           { return test->getLanguage() != lang; }),
            filtered.end());
        tests.swap(filtered);
        runAll();
        tests.swap(filtered);
    }

    const std::vector<TestResult> &TestSuite::getResults() const
    {
        return results;
    }

    // PerformanceMetrics implementation
    void PerformanceMetrics::start()
    {
        startTime = std::chrono::high_resolution_clock::now();
    }

    void PerformanceMetrics::stop()
    {
        endTime = std::chrono::high_resolution_clock::now();
    }

    void PerformanceMetrics::addMetric(const std::string &name, double value)
    {
        metrics[name] = value;
    }

    std::map<std::string, double> PerformanceMetrics::getMetrics() const
    {
        return metrics;
    }

    double PerformanceMetrics::getDuration() const
    {
        return std::chrono::duration_cast<std::chrono::milliseconds>(
                   endTime - startTime)
            .count();
    }

    // Assertion implementations
    void assertEquals(const std::string &expected, const std::string &actual)
    {
        if (expected != actual)
        {
            throw std::runtime_error("Assertion failed: expected '" + expected +
                                     "' but got '" + actual + "'");
        }
    }

    void assertTrue(bool condition, const std::string &message)
    {
        if (!condition)
        {
            throw std::runtime_error("Assertion failed: " + message);
        }
    }

    void assertFalse(bool condition, const std::string &message)
    {
        if (condition)
        {
            throw std::runtime_error("Assertion failed: " + message);
        }
    }

    void assertNull(const void *ptr, const std::string &message)
    {
        if (ptr != nullptr)
        {
            throw std::runtime_error("Assertion failed: expected null but got non-null pointer. " + message);
        }
    }

    void assertNotNull(const void *ptr, const std::string &message)
    {
        if (ptr == nullptr)
        {
            throw std::runtime_error("Assertion failed: expected non-null but got null pointer. " + message);
        }
    }

} // namespace cpj::test
