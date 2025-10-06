// CPJJavaGUI.java
// Advanced GUI components for CPJ Java module

package cpj.java;

import javax.swing.*;
import java.awt.*;

public class CPJJavaGUI {
    public static void showMainWindow() {
        JFrame frame = new JFrame("CPJ Advanced Java GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 400);
        JPanel panel = new JPanel(new BorderLayout());
        JLabel label = new JLabel("Welcome to CPJ Tri-Language Compiler!", SwingConstants.CENTER);
        label.setFont(new Font("Arial", Font.BOLD, 20));
        panel.add(label, BorderLayout.NORTH);
        JTextArea outputArea = new JTextArea();
        outputArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(outputArea);
        panel.add(scrollPane, BorderLayout.CENTER);
        JButton runButton = new JButton("Run Integration Test");
        panel.add(runButton, BorderLayout.SOUTH);
        frame.getContentPane().add(panel);
        frame.setVisible(true);
        // Example: Show output from integration
        runButton.addActionListener(e -> outputArea.append("Integration test executed.\n"));
    }
}
