package cpj.java;

import javax.tools.*;
import java.io.File;
import java.util.Arrays;

public class CPJJavaUtils {
    public static boolean compileJava(String sourceFile) {
        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<>();
        StandardJavaFileManager fileManager = compiler.getStandardFileManager(diagnostics, null, null);

        Iterable<? extends JavaFileObject> compilationUnits = fileManager
                .getJavaFileObjectsFromStrings(Arrays.asList(sourceFile));

        JavaCompiler.CompilationTask task = compiler.getTask(
                null,
                fileManager,
                diagnostics,
                Arrays.asList("-d", "bin"), // Output to bin directory
                null,
                compilationUnits);

        boolean success = task.call();

        if (!success) {
            System.err.println("Compilation failed:");
            diagnostics.getDiagnostics().forEach(diagnostic -> {
                System.err.format("Error on line %d in %s%n",
                        diagnostic.getLineNumber(),
                        diagnostic.getSource().toUri());
            });
        }

        return success;
    }

    public static boolean runJava(String className) {
        try {
            ProcessBuilder pb = new ProcessBuilder(
                    "java",
                    "-cp", "bin", // Add bin directory to classpath
                    className);
            pb.inheritIO();
            Process process = pb.start();
            return process.waitFor() == 0;
        } catch (Exception e) {
            System.err.println("Error running Java class: " + e.getMessage());
            return false;
        }
    }
}