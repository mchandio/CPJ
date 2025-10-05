package cpj.java;

import javax.swing.*;
import java.awt.*;
import cpj.ipc.EventBus;
import cpj.ipc.Event;
import java.util.HashMap;
import java.util.Map;

public class CPJJavaGUI {
    private static JFrame mainWindow;
    private static EventBus eventBus;
    private static Map<String, Component> components = new HashMap<>();

    public static void showMainWindow() {
        SwingUtilities.invokeLater(() -> {
            mainWindow = new JFrame("CPJ Application");
            mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            mainWindow.setLayout(new BorderLayout());
            mainWindow.setSize(400, 300);

            // Initialize event bus
            eventBus = EventBus.getInstance();

            // Set up main content panel
            JPanel contentPanel = new JPanel();
            contentPanel.setLayout(new BoxLayout(contentPanel, BoxLayout.Y_AXIS));
            mainWindow.add(contentPanel, BorderLayout.CENTER);

            mainWindow.setVisible(true);
        });
    }

    public static void addComponent(String id, Component component) {
        components.put(id, component);
        if (mainWindow != null) {
            SwingUtilities.invokeLater(() -> {
                Container contentPane = mainWindow.getContentPane();
                if (contentPane instanceof JPanel) {
                    JPanel panel = (JPanel) contentPane;
                    panel.add(component);
                    panel.revalidate();
                    panel.repaint();
                }
            });
        }
    }

    public static Component getComponent(String id) {
        return components.get(id);
    }

    public static void updateComponent(String id, String property, Object value) {
        Component component = components.get(id);
        if (component == null)
            return;

        SwingUtilities.invokeLater(() -> {
            if (component instanceof JLabel && property.equals("text")) {
                ((JLabel) component).setText((String) value);
            } else if (component instanceof JButton && property.equals("text")) {
                ((JButton) component).setText((String) value);
            }
            // Add more component type handling as needed
        });
    }

    public static void fireEvent(String eventType, String componentId, Map<String, Object> data) {
        if (eventBus != null) {
            try {
                Map<String, Object> eventData = new HashMap<>(data);
                eventData.put("componentId", componentId);
                Event event = new Event(eventType, eventData, "java", "all");
                eventBus.publish(event);
            } catch (Exception e) {
                System.err.println("Error firing event: " + e.getMessage());
            }
        }
    }
}