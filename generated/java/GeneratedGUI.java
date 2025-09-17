import javax.swing.*;
import java.awt.*;

public class GeneratedGUI {
    public static void main(String[] args) {
        System.out.println("Generated GUI with 2 widgets");
        System.out.println("  x: int");
        System.out.println("  y: int");
        try {
            JFrame f = new JFrame("CPJ Generated GUI");
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            Container c = f.getContentPane();
            c.setLayout(new GridLayout(0,1));
            c.add(new JLabel("x: int"));
            c.add(new JLabel("y: int"));
        } catch (Throwable t) {
            System.err.println("GUI construction skipped: " + t.getMessage());
        }
    }
}
