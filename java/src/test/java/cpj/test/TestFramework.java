package cpj.test;


import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

public class TestFramework {
    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    public @interface Test {
    }

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    public @interface Before {
    }

    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    public @interface After {
    }

    public static class TestResult {
        public final String testName;
        public final boolean passed;
        public final String message;
        public final long duration;

        public TestResult(String testName, boolean passed, String message, long duration) {
            this.testName = testName;
            this.passed = passed;
            this.message = message;
            this.duration = duration;
        }
    }

    public static List<TestResult> runTests(Class<?> testClass) {
        List<TestResult> results = new ArrayList<>();
        Object instance;

        try {
            instance = testClass.getDeclaredConstructor().newInstance();
        } catch (Exception e) {
            throw new RuntimeException("Could not create test instance", e);
        }

        Method[] methods = testClass.getDeclaredMethods();
        Method beforeMethod = null;
        Method afterMethod = null;

        // Find setup and teardown methods
        for (Method method : methods) {
            if (method.isAnnotationPresent(Before.class)) {
                beforeMethod = method;
            } else if (method.isAnnotationPresent(After.class)) {
                afterMethod = method;
            }
        }

        // Run tests
        for (Method method : methods) {
            if (method.isAnnotationPresent(Test.class)) {
                TestResult result = runSingleTest(instance, method, beforeMethod, afterMethod);
                results.add(result);
            }
        }

        return results;
    }

    private static TestResult runSingleTest(Object instance, Method testMethod,
            Method beforeMethod, Method afterMethod) {
        try {
            if (beforeMethod != null) {
                beforeMethod.invoke(instance);
            }

            long startTime = System.nanoTime();
            testMethod.invoke(instance);
            long duration = System.nanoTime() - startTime;

            if (afterMethod != null) {
                afterMethod.invoke(instance);
            }

            return new TestResult(testMethod.getName(), true, "Test passed", duration);
        } catch (Exception e) {
            return new TestResult(testMethod.getName(), false, e.getMessage(), 0);
        }
    }

    public static void assertTrue(boolean condition) {
        if (!condition) {
            throw new AssertionError("Expected true but was false");
        }
    }

    public static void assertEquals(Object expected, Object actual) {
        if (!expected.equals(actual)) {
            throw new AssertionError("Expected " + expected + " but was " + actual);
        }
    }
}