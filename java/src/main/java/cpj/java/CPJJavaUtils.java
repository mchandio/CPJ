// CPJJavaUtils.java
// Utility class for Java compilation and execution

package cpj.java;

import java.io.*;
import java.util.HashMap;

public class CPJJavaUtils {
    public static boolean compileJava(String sourceFile) {
        try {
            ProcessBuilder pb = new ProcessBuilder("javac", sourceFile);
            pb.redirectErrorStream(true);
            Process compile = pb.start();
            try (BufferedReader r = new BufferedReader(new InputStreamReader(compile.getInputStream()))) {
                String line;
                while ((line = r.readLine()) != null) {
                    System.out.println(line);
                }
            }
            int rc = compile.waitFor();
            return rc == 0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }

    public static boolean runJava(String className) {
        try {
            ProcessBuilder pb = new ProcessBuilder("java", className);
            pb.redirectErrorStream(true);
            Process run = pb.start();
            try (BufferedReader r = new BufferedReader(new InputStreamReader(run.getInputStream()))) {
                String line;
                while ((line = r.readLine()) != null) {
                    System.out.println(line);
                }
            }
            int rc = run.waitFor();
            return rc == 0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}
