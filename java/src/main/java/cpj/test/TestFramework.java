package cpj.test;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Supplier;

public class TestFramework {
    public static class TestCase {
        private String name;
        private Runnable testFunc;
        private boolean passed;
        private double duration;

        public TestCase(String name, Runnable testFunc) {
            this.name = name;
            this.testFunc = testFunc;
        }

        public void run() {
            long startTime = System.nanoTime();
            try {
                testFunc.run();
                passed = true;
            } catch (Exception e) {
                System.err.println("Test " + name + " failed: " + e.getMessage());
                passed = false;
            }
            duration = (System.nanoTime() - startTime) / 1_000_000_000.0;
        }

        public String getName() {
            return name;
        }

        public boolean isPassed() {
            return passed;
        }

        public double getDuration() {
            return duration;
        }
    }

    public static class TestSuite {
        private String name;
        private List<TestCase> tests = new ArrayList<>();

        public TestSuite(String name) {
            this.name = name;
        }

        public void addTest(String name, Runnable testFunc) {
            tests.add(new TestCase(name, testFunc));
        }

        public void run() {
            System.out.println("Running test suite: " + name);
            for (TestCase test : tests) {
                System.out.print("  Running test: " + test.getName() + "... ");
                test.run();
                System.out.println(
                        (test.isPassed() ? "PASSED" : "FAILED") +
                                " (" + test.getDuration() + "s)");
            }
        }

        public int getTotalTests() {
            return tests.size();
        }

        public long getPassedTests() {
            return tests.stream().filter(TestCase::isPassed).count();
        }
    }

    public static class Assertions {
        public static void assertEquals(Object expected, Object actual, String message) {
            if (!expected.equals(actual)) {
                throw new AssertionError(
                        message + " Expected: " + expected + ", but got: " + actual);
            }
        }

        public static void assertTrue(boolean condition, String message) {
            if (!condition) {
                throw new AssertionError(message);
            }
        }

        public static void assertFalse(boolean condition, String message) {
            assertTrue(!condition, message);
        }

        public static void assertNull(Object obj, String message) {
            if (obj != null) {
                throw new AssertionError(message);
            }
        }

        public static void assertNotNull(Object obj, String message) {
            if (obj == null) {
                throw new AssertionError(message);
            }
        }
    }

    public static class Benchmark {
        private String name;
        private long startTime;
        private long endTime;
        private boolean running;

        public Benchmark(String name) {
            this.name = name;
        }

        public void start() {
            startTime = System.nanoTime();
            running = true;
        }

        public void stop() {
            if (!running) {
                throw new IllegalStateException("Benchmark not started");
            }
            endTime = System.nanoTime();
            running = false;
        }

        public double getElapsedTime() {
            if (running) {
                throw new IllegalStateException("Benchmark still running");
            }
            return (endTime - startTime) / 1_000_000_000.0;
        }
    }
}