package cpj.ipc;

import java.util.Map;
import java.util.HashMap;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Represents an event in the CPJ system.
 * Events can be triggered from any language and handled by any language.
 */
public class Event {
    private final String name;
    private final Map<String, Object> data;
    private final String source;
    private final String target;

    @JsonCreator
    public Event(
            @JsonProperty("name") String name,
            @JsonProperty("data") Map<String, Object> data,
            @JsonProperty("source") String source,
            @JsonProperty("target") String target) {
        this.name = name;
        this.data = data != null ? data : new HashMap<>();
        this.source = source;
        this.target = target;
    }

    public String getName() {
        return name;
    }

    public Map<String, Object> getData() {
        return data;
    }

    public String getSource() {
        return source;
    }

    public String getTarget() {
        return target;
    }
}