// EventSchemaValidator.java
// Utility for validating event JSON objects against the CPJ unified schema using Jackson

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class EventSchemaValidator {
    private static final ObjectMapper mapper = new ObjectMapper();

    /**
     * Validates a JsonNode as a CPJ event. Throws IllegalArgumentException if invalid.
     */
    public static void validateEvent(JsonNode event) {
        if (!event.isObject()) throw new IllegalArgumentException("Event must be a JSON object");
        if (!event.has("id") || !event.get("id").isTextual())
            throw new IllegalArgumentException("Event missing required string field: id");
        if (!event.has("type") || !event.get("type").isTextual())
            throw new IllegalArgumentException("Event missing required string field: type");
        if (event.has("payload") && !event.get("payload").isObject() && !event.get("payload").isNull())
            throw new IllegalArgumentException("payload must be an object or null");
        if (event.has("reply_to") && !event.get("reply_to").isTextual())
            throw new IllegalArgumentException("reply_to must be a string");
        if (event.has("error") && !event.get("error").isTextual())
            throw new IllegalArgumentException("error must be a string");
        if (event.has("runtime") && !event.get("runtime").isTextual())
            throw new IllegalArgumentException("runtime must be a string");
        if (event.has("timestamp") && !event.get("timestamp").isNumber())
            throw new IllegalArgumentException("timestamp must be a number");
    }

    /**
     * Parse and validate a JSON string as a CPJ event.
     */
    public static void validateEvent(String json) throws Exception {
        JsonNode node = mapper.readTree(json);
        validateEvent(node);
    }
}
