package cpj.gui;

import cpj.ipc.Event;
import cpj.ipc.EventBus;
import javax.swing.*;
import java.util.HashMap;
import java.util.Map;

public class CPJButton extends JButton {
    private final String componentId;
    private final EventBus eventBus;

    public CPJButton(String text, String componentId) {
        super(text);
        this.componentId = componentId;
        this.eventBus = EventBus.getInstance();

        addActionListener(e -> {
            Map<String, Object> data = new HashMap<>();
            data.put("componentId", componentId);
            data.put("text", getText());

            try {
                Event event = new Event("button_click", data, "java", "all");
                eventBus.publish(event);
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        });
    }

    public void onEvent(String eventName, Runnable handler) {
        eventBus.subscribe(eventName, componentId, event -> {
            if (event.getData().get("componentId").equals(componentId)) {
                SwingUtilities.invokeLater(handler);
            }
        });
    }

    @Override
    public void removeNotify() {
        super.removeNotify();
        eventBus.unsubscribe("button_click", componentId);
    }
}