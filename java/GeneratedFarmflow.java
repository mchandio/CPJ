
// Auto-generated Java Swing from CPJ
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
// ...existing code...

public class GeneratedFarmflow extends JFrame {
    private Map<String, JTextField> fields = new HashMap<>();
    private JTextArea farmersArea = new JTextArea();
    private JTextField totalsField = new JTextField();

    public GeneratedFarmflow() {
        setTitle("CPJ Generated GUI: Farmflow");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        JPanel top = new JPanel();
        top.setLayout(new BoxLayout(top, BoxLayout.Y_AXIS));
        top.add(new JLabel("FarmFlow - Lightweight Desktop"));
        top.add(new JLabel("Add Farmer:"));
        top.add(new JLabel("Add Bill:"));
        top.add(new JLabel("Farmers List"));
        top.add(new JLabel("Totals"));
        JTextField tf_farmer_name = new JTextField(20);
        fields.put("farmer_name", tf_farmer_name);
        top.add(tf_farmer_name);
        JTextField tf_farmer_phone = new JTextField(20);
        fields.put("farmer_phone", tf_farmer_phone);
        top.add(tf_farmer_phone);
        JTextField tf_farmer_village = new JTextField(20);
        fields.put("farmer_village", tf_farmer_village);
        top.add(tf_farmer_village);
        JTextField tf_bill_date = new JTextField(20);
        fields.put("bill_date", tf_bill_date);
        top.add(tf_bill_date);
        JTextField tf_bill_farmer = new JTextField(20);
        fields.put("bill_farmer", tf_bill_farmer);
        top.add(tf_bill_farmer);
        JTextField tf_bill_crop = new JTextField(20);
        fields.put("bill_crop", tf_bill_crop);
        top.add(tf_bill_crop);
        JTextField tf_bill_weight = new JTextField(20);
        fields.put("bill_weight", tf_bill_weight);
        top.add(tf_bill_weight);
        JTextField tf_bill_rate = new JTextField(20);
        fields.put("bill_rate", tf_bill_rate);
        top.add(tf_bill_rate);
        JScrollPane sp_farmers_list = new JScrollPane(farmersArea);
        farmersArea.setEditable(false);
        farmersArea.setRows(8);
        top.add(sp_farmers_list);
        totalsField.setEditable(false);
        top.add(totalsField);
        fields.put("totals", totalsField);
        JPanel btnPanel = new JPanel(new FlowLayout(FlowLayout.LEFT));
        JButton btn_Add_Farmer = new JButton("Add Farmer");
        btn_Add_Farmer.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = fields.get("farmer_name").getText();
                String phone = fields.get("farmer_phone").getText();
                String village = fields.get("farmer_village").getText();
                if (name != null && name.length() > 0) {
                    farmersArea.append(name + " (" + phone + "), " + village + "\n");
                    updateTotals();
                    // notify python connector with simple JSON (best-effort)
                    try {
                        String json = "{\"name\":\"" + name + "\", \"phone\":\"" + phone + "\", \"village\":\""
                                + village + "\"}";
                        Runtime.getRuntime().exec(new String[] { "python3", "cpj_connector.py", "exchange_data",
                                "farmflow_data.json", json });
                    } catch (Exception ex) {
                        ex.printStackTrace();
                    }
                }
            }
        });
        btnPanel.add(btn_Add_Farmer);
        JButton btn_Add_Bill = new JButton("Add Bill");
        btn_Add_Bill.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String date = fields.get("bill_date").getText();
                String farmer = fields.get("bill_farmer").getText();
                String crop = fields.get("bill_crop").getText();
                String weight = fields.get("bill_weight").getText();
                String rate = fields.get("bill_rate").getText();
                farmersArea.append(
                        "BILL: " + date + " - " + farmer + " - " + crop + " - " + weight + "kg @" + rate + "\n");
                updateTotals();
            }
        });
        btnPanel.add(btn_Add_Bill);
        top.add(btnPanel);
        add(new JScrollPane(top), BorderLayout.CENTER);
    }

    private void updateTotals() {
        // simple totals = lines in farmersArea + bills (lines)
        int lines = farmersArea.getText().isEmpty() ? 0 : farmersArea.getLineCount();
        totalsField.setText(Integer.toString(lines));
    }

    // Programmatic helpers (EDT-safe)
    public void setField(final String name, final String value) {
        try {
            javax.swing.SwingUtilities.invokeAndWait(() -> {
                JTextField f = fields.get(name);
                if (f != null)
                    f.setText(value);
            });
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void clickButton(final String label) {
        try {
            javax.swing.SwingUtilities.invokeAndWait(() -> {
                for (Component c : ((JPanel) ((JScrollPane) getContentPane().getComponent(0)).getViewport().getView())
                        .getComponents()) {
                    if (c instanceof JPanel) {
                        for (Component b : ((JPanel) c).getComponents()) {
                            if (b instanceof JButton && ((JButton) b).getText().equals(label)) {
                                ((JButton) b).doClick();
                                return;
                            }
                        }
                    }
                }
            });
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public String getFieldText(final String name) {
        final String[] res = new String[1];
        try {
            javax.swing.SwingUtilities.invokeAndWait(() -> {
                JTextField f = fields.get(name);
                res[0] = (f != null) ? f.getText() : null;
            });
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return res[0];
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new GeneratedFarmflow().setVisible(true);
        });
    }
}
