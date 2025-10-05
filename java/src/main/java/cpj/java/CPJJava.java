package cpj.java;

import java.io.File;

public class CPJJava {
    public static void runCompiledFile(String sourceFile) {
        try {
            String className = new File(sourceFile).getName().replace(".java", "");

            // Ensure the bin directory exists
            new File("bin").mkdirs();

            // Compile the generated Java file
            if (!CPJJavaUtils.compileJava(sourceFile)) {
                System.err.println("Failed to compile Java file: " + sourceFile);
                return;
            }

            // Run the compiled class
            if (!CPJJavaUtils.runJava(className)) {
                System.err.println("Failed to run Java class: " + className);
                return;
            }

            // Show GUI window if this is a GUI application
            if (className.startsWith("Generated") || className.endsWith("GUI")) {
                CPJJavaGUI.showMainWindow();
            }
        } catch (Exception e) {
            System.err.println("Error running Java file: " + e.getMessage());
            e.printStackTrace();
        }
    }
}