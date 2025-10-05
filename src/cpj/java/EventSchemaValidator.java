package cpj.java;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.IOException;

public class EventSchemaValidator {
    private static final ObjectMapper mapper = new ObjectMapper();

    /**
     * Validates that the event data follows the schema
     */
    public static void validateEvent(JsonNode event) {
        if (!event.has("type")) {
            throw new IllegalArgumentException("Event must have a type");
        }
        if (!event.has("payload")) {
            throw new IllegalArgumentException("Event must have a payload");
        }
    }

    /**
     * Validates JSON string against schema
     */
    public static boolean validateJSON(String json) {
        try {
            JsonNode node = mapper.readTree(json);
            validateEvent(node);
            return true;
        } catch (IOException | IllegalArgumentException e) {
            System.err.println("Validation failed: " + e.getMessage());
            return false;
        }
    }
}