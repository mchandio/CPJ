package cpj.java;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import java.util.Map;

public class EventSchemaValidator {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void validateEvent(Map<String, Object> event) throws Exception {
        if (!event.containsKey("type")) {
            throw new IllegalArgumentException("Event must have a 'type' field");
        }
        if (!event.containsKey("data")) {
            throw new IllegalArgumentException("Event must have a 'data' field");
        }

        // Validate based on event type
        String type = (String) event.get("type");
        switch (type) {
            case "button_click":
                validateButtonClickEvent(event);
                break;
            case "text_change":
                validateTextChangeEvent(event);
                break;
            // Add more event type validations as needed
            default:
                throw new IllegalArgumentException("Unknown event type: " + type);
        }
    }

    private static void validateButtonClickEvent(Map<String, Object> event) {
        Map<String, Object> data = (Map<String, Object>) event.get("data");
        if (!data.containsKey("buttonId")) {
            throw new IllegalArgumentException("Button click event must have a 'buttonId' field");
        }
    }

    private static void validateTextChangeEvent(Map<String, Object> event) {
        Map<String, Object> data = (Map<String, Object>) event.get("data");
        if (!data.containsKey("componentId")) {
            throw new IllegalArgumentException("Text change event must have a 'componentId' field");
        }
        if (!data.containsKey("text")) {
            throw new IllegalArgumentException("Text change event must have a 'text' field");
        }
    }
}