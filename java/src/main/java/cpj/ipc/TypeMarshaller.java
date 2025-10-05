package cpj.ipc;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.util.Map;
import java.util.HashMap;

/**
 * Handles type conversion and marshalling between CPJ's supported languages
 * (C++, Python, Java).
 */
public class TypeMarshaller {
    private static final ObjectMapper mapper = new ObjectMapper();

    // Type mapping between languages
    private static final Map<String, Map<String, String>> typeMap = new HashMap<>();

    static {
        // Java to C++ type mapping
        Map<String, String> javaToCpp = new HashMap<>();
        javaToCpp.put("int", "int32_t");
        javaToCpp.put("long", "int64_t");
        javaToCpp.put("double", "double");
        javaToCpp.put("boolean", "bool");
        javaToCpp.put("String", "std::string");
        typeMap.put("cpp", javaToCpp);

        // Java to Python type mapping
        Map<String, String> javaToPython = new HashMap<>();
        javaToPython.put("int", "int");
        javaToPython.put("long", "int");
        javaToPython.put("double", "float");
        javaToPython.put("boolean", "bool");
        javaToPython.put("String", "str");
        typeMap.put("python", javaToPython);
    }

    /**
     * Wraps data with type information for cross-language marshalling.
     */
    public static String marshal(Object obj, String sourceType, String targetLang) throws Exception {
        ObjectNode wrapper = mapper.createObjectNode();
        wrapper.put("type", getTargetType(sourceType, targetLang));
        wrapper.set("data", mapper.valueToTree(obj));
        return mapper.writeValueAsString(wrapper);
    }

    /**
     * Extracts typed data from a marshalled string.
     */
    public static <T> T unmarshal(String json, Class<T> targetClass) throws Exception {
        JsonNode root = mapper.readTree(json);
        String type = root.get("type").asText();
        JsonNode data = root.get("data");
        return mapper.treeToValue(data, targetClass);
    }

    /**
     * Maps a type from one language to another.
     */
    private static String getTargetType(String sourceType, String targetLang) {
        Map<String, String> langMap = typeMap.get(targetLang);
        if (langMap == null) {
            throw new IllegalArgumentException("Unsupported target language: " + targetLang);
        }
        String targetType = langMap.get(sourceType);
        if (targetType == null) {
            throw new IllegalArgumentException(
                    String.format("No mapping for type '%s' to language '%s'", sourceType, targetLang));
        }
        return targetType;
    }

    /**
     * Registers a custom type mapping between languages.
     */
    public static void registerTypeMapping(String sourceLang, String sourceType,
            String targetLang, String targetType) {
        typeMap.computeIfAbsent(targetLang, k -> new HashMap<>())
                .put(sourceType, targetType);
    }
}