package cpj.java;

import javax.swing.*;
import java.awt.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.io.FileWriter;

public class GeneratedGUI {
    public static void main(String[] args) {
        System.out.println("Generated GUI with 12 widgets:");
        System.out.println("  types count:int flag:bool");
        System.out.println("  addTextField(\"count\")");
        System.out.println("  addTextField('flag')");
        System.out.println("  types {");
        System.out.println("  \"x\": \"int\",");
        System.out.println("  'y': 'float'");
        System.out.println("  }");
        System.out.println("  addTextField(\"x\")");
        System.out.println("  addTextField(\"y\")");
        System.out.println("  addTextField(\"c\", \"str\")");
        System.out.println("  addButton(\"Run\", show(count, flag, c))");
        System.out.println("  show()");
        try {
            JFrame f = new JFrame("CPJ Generated GUI");
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            Container c = f.getContentPane();
            c.setLayout(new GridLayout(0,1));
            c.add(new JLabel("types count:int flag:bool"));
            JTextField tf1 = new JTextField(20);
            tf1.setName("count");
            c.add(tf1);
            JTextField tf2 = new JTextField(20);
            c.add(tf2);
            c.add(new JLabel("types {"));
            c.add(new JLabel("\"x\": \"int\","));
            c.add(new JLabel("'y': 'float'"));
            c.add(new JLabel("}"));
            JTextField tf7 = new JTextField(20);
            tf7.setName("x");
            c.add(tf7);
            JTextField tf8 = new JTextField(20);
            tf8.setName("y");
            c.add(tf8);
            JTextField tf9 = new JTextField(20);
            tf9.setName("c\", \"str");
            c.add(tf9);
            JButton b10 = new JButton("Run");
            b10.addActionListener(new java.awt.event.ActionListener() {
                public void actionPerformed(java.awt.event.ActionEvent e) {
                    try {
                        ObjectMapper mapper = new ObjectMapper();
                        ObjectNode event = mapper.createObjectNode();
                        event.put("id", java.util.UUID.randomUUID().toString());
                        event.put("type", "button_click");
                        ObjectNode payload = mapper.createObjectNode();
                        payload.put("button", "Run");
                        event.set("payload", payload);
                        event.put("runtime", "java");
                        event.put("timestamp", System.currentTimeMillis() / 1000.0);
                        // Validate event schema
                        EventSchemaValidator.validateEvent(event);
                        try (FileWriter fw = new FileWriter("/tmp/cpj_event.json")) {
                            fw.write(event.toString());
                        }
                    } catch (Throwable ex) {
                        ex.printStackTrace();
                    }
                }
            });
            c.add(b10);
            f.pack();
            f.setVisible(true);
        } catch (Throwable t) {
            System.out.println("GUI construction skipped: " + t.getMessage());
        }
    }
}
