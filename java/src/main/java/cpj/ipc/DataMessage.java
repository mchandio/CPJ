package cpj.ipc;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Represents a typed message for inter-process communication.
 * Supports basic data types and structured data serialization.
 */
public class DataMessage<T> {
    private final String type;
    private final T data;

    @JsonCreator
    public DataMessage(
            @JsonProperty("type") String type,
            @JsonProperty("data") T data) {
        this.type = type;
        this.data = data;
    }

    public String getType() {
        return type;
    }

    public T getData() {
        return data;
    }

    @Override
    public String toString() {
        return String.format("DataMessage{type='%s', data=%s}", type, data);
    }
}