#pragma once

#include <string>
#include <vector>
#include <functional>
#include <chrono>
#include <memory>
#include <map>

namespace cpj::test
{

    enum class TestLanguage
    {
        CPP,
        PYTHON,
        JAVA
    };

    enum class TestType
    {
        UNIT,
        INTEGRATION,
        PERFORMANCE,
        COMPATIBILITY
    };

    struct TestResult
    {
        bool passed;
        std::string message;
        double duration_ms;
        std::map<std::string, double> metrics;
    };

    class TestCase
    {
    public:
        TestCase(const std::string &name, TestType type, TestLanguage lang);
        virtual ~TestCase() = default;

        virtual TestResult run() = 0;
        virtual void setUp() {}
        virtual void tearDown() {}

        const std::string &getName() const { return name; }
        TestType getType() const { return type; }
        TestLanguage getLanguage() const { return language; }

    protected:
        std::string name;
        TestType type;
        TestLanguage language;
        std::chrono::high_resolution_clock::time_point startTime;
        std::chrono::high_resolution_clock::time_point endTime;
    };

    class TestSuite
    {
    public:
        explicit TestSuite(const std::string &name);
        void addTest(std::shared_ptr<TestCase> test);
        void runAll();
        void runByType(TestType type);
        void runByLanguage(TestLanguage lang);
        const std::vector<TestResult> &getResults() const;

    private:
        std::string name;
        std::vector<std::shared_ptr<TestCase>> tests;
        std::vector<TestResult> results;
    };

    class PerformanceMetrics
    {
    public:
        void start();
        void stop();
        void addMetric(const std::string &name, double value);
        std::map<std::string, double> getMetrics() const;
        double getDuration() const;

    private:
        std::chrono::high_resolution_clock::time_point startTime;
        std::chrono::high_resolution_clock::time_point endTime;
        std::map<std::string, double> metrics;
    };

    // Assertion utilities
    void assertEquals(const std::string &expected, const std::string &actual);
    void assertTrue(bool condition, const std::string &message = "");
    void assertFalse(bool condition, const std::string &message = "");
    void assertNull(const void *ptr, const std::string &message = "");
    void assertNotNull(const void *ptr, const std::string &message = "");

// Test registration macros
#define CPJ_TEST_CASE(name, type, lang)               \
    class name##Test : public cpj::test::TestCase     \
    {                                                 \
    public:                                           \
        name##Test() : TestCase(#name, type, lang) {} \
        TestResult run() override;                    \
    };                                                \
    TestResult name##Test::run()

#define CPJ_PERFORMANCE_TEST(name, lang) \
    CPJ_TEST_CASE(name, cpj::test::TestType::PERFORMANCE, lang)

#define CPJ_UNIT_TEST(name, lang) \
    CPJ_TEST_CASE(name, cpj::test::TestType::UNIT, lang)

#define CPJ_INTEGRATION_TEST(name, lang) \
    CPJ_TEST_CASE(name, cpj::test::TestType::INTEGRATION, lang)

} // namespace cpj::test
