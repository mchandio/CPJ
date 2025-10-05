package cpj.java;

import cpj.java.utils.CPJJavaUtils;

public class CPJJava {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java CPJJava <source_file.java>");
            return;
        }
        String sourceFile = args[0];
        String className = sourceFile.replace(".java", "");
        try {
            if (!CPJJavaUtils.compileJava(sourceFile)) {
                throw new Exception("Compilation failed.");
            }
            System.out.println("Compilation successful. Running program...");
            if (!CPJJavaUtils.runJava(className)) {
                throw new Exception("Execution failed.");
            }
            // Advanced GUI
            CPJJavaGUI.showMainWindow();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}