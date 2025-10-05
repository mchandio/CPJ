package types;

import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.*;
import java.util.function.Function;

public class TypeSystem {
    public enum TypeCategory {
        PRIMITIVE,
        COLLECTION,
        OBJECT,
        FUNCTION,
        GENERIC
    }

    public enum PrimitiveTypeId {
        BOOL,
        INT8,
        INT16,
        INT32,
        INT64,
        UINT8,
        UINT16,
        UINT32,
        UINT64,
        FLOAT32,
        FLOAT64,
        STRING,
        VOID
    }

    public static class ConversionResult<T> {
        private final boolean success;
        private final T value;
        private final String error;

        public ConversionResult(boolean success, T value, String error) {
            this.success = success;
            this.value = value;
            this.error = error;
        }

        public boolean isSuccess() {
            return success;
        }

        public T getValue() {
            return value;
        }

        public String getError() {
            return error;
        }
    }

    public static abstract class TypeDescriptor<T> {
        protected final String name;
        protected final TypeCategory category;

        protected TypeDescriptor(String name, TypeCategory category) {
            this.name = name;
            this.category = category;
        }

        public String getName() {
            return name;
        }

        public TypeCategory getCategory() {
            return category;
        }

        public abstract String toString(T value);

        public abstract ConversionResult<T> fromString(String str);

        public abstract boolean equals(T lhs, T rhs);

        public abstract int hash(T value);

        public abstract String getCppTypeName();

        public abstract String getPythonTypeName();

        public abstract String getJavaTypeName();
    }

    public static class PrimitiveTypeDescriptor<T> extends TypeDescriptor<T> {
        private final PrimitiveTypeId typeId;
        private final Function<String, T> parser;
        private final Function<T, String> formatter;

        public PrimitiveTypeDescriptor(String name, PrimitiveTypeId typeId,
                Function<String, T> parser,
                Function<T, String> formatter) {
            super(name, TypeCategory.PRIMITIVE);
            this.typeId = typeId;
            this.parser = parser;
            this.formatter = formatter;
        }

        @Override
        public String toString(T value) {
            try {
                return formatter.apply(value);
            } catch (Exception e) {
                throw new RuntimeException("Type conversion error: " + e.getMessage());
            }
        }

        @Override
        public ConversionResult<T> fromString(String str) {
            try {
                T value = parser.apply(str);
                return new ConversionResult<>(true, value, "");
            } catch (Exception e) {
                return new ConversionResult<>(false, null,
                        "Conversion error: " + e.getMessage());
            }
        }

        @Override
        public boolean equals(T lhs, T rhs) {
            if (lhs == null || rhs == null) {
                return lhs == rhs;
            }

            if (typeId == PrimitiveTypeId.FLOAT32 || typeId == PrimitiveTypeId.FLOAT64) {
                double diff = ((Number) lhs).doubleValue() - ((Number) rhs).doubleValue();
                return Math.abs(diff) < 1e-6;
            }

            return lhs.equals(rhs);
        }

        @Override
        public int hash(T value) {
            return value != null ? value.hashCode() : 0;
        }

        @Override
        public String getCppTypeName() {
            switch (typeId) {
                case BOOL:
                    return "bool";
                case INT32:
                    return "int32_t";
                case INT64:
                    return "int64_t";
                case FLOAT32:
                    return "float";
                case FLOAT64:
                    return "double";
                case STRING:
                    return "std::string";
                default:
                    return "void";
            }
        }

        @Override
        public String getPythonTypeName() {
            switch (typeId) {
                case BOOL:
                    return "bool";
                case INT32:
                case INT64:
                    return "int";
                case FLOAT32:
                case FLOAT64:
                    return "float";
                case STRING:
                    return "str";
                default:
                    return "None";
            }
        }

        @Override
        public String getJavaTypeName() {
            switch (typeId) {
                case BOOL:
                    return "boolean";
                case INT32:
                    return "int";
                case INT64:
                    return "long";
                case FLOAT32:
                    return "float";
                case FLOAT64:
                    return "double";
                case STRING:
                    return "String";
                default:
                    return "void";
            }
        }
    }

    public static class CollectionTypeDescriptor<E, C extends Collection<E>>
            extends TypeDescriptor<C> {
        private final TypeDescriptor<E> elementType;
        private final Function<Collection<E>, C> collectionFactory;
        private static final ObjectMapper jsonMapper = new ObjectMapper();

        public CollectionTypeDescriptor(String name,
                TypeDescriptor<E> elementType,
                Function<Collection<E>, C> collectionFactory) {
            super(name, TypeCategory.COLLECTION);
            this.elementType = elementType;
            this.collectionFactory = collectionFactory;
        }

        @Override
        public String toString(C value) {
            try {
                List<String> elements = new ArrayList<>();
                for (E element : value) {
                    elements.add(elementType.toString(element));
                }
                return jsonMapper.writeValueAsString(elements);
            } catch (Exception e) {
                throw new RuntimeException("Collection conversion error: " + e.getMessage());
            }
        }

        @Override
        public ConversionResult<C> fromString(String str) {
            try {
                List<String> elements = jsonMapper.readValue(str,
                        jsonMapper.getTypeFactory().constructCollectionType(
                                List.class, String.class));

                List<E> converted = new ArrayList<>();
                for (String element : elements) {
                    ConversionResult<E> result = elementType.fromString(element);
                    if (!result.isSuccess()) {
                        return new ConversionResult<>(false, null,
                                "Element conversion failed: " + result.getError());
                    }
                    converted.add(result.getValue());
                }

                return new ConversionResult<>(true, collectionFactory.apply(converted), "");
            } catch (Exception e) {
                return new ConversionResult<>(false, null,
                        "Collection conversion error: " + e.getMessage());
            }
        }

        @Override
        public boolean equals(C lhs, C rhs) {
            if (lhs == null || rhs == null) {
                return lhs == rhs;
            }
            if (lhs.size() != rhs.size()) {
                return false;
            }

            Iterator<E> lhsIt = lhs.iterator();
            Iterator<E> rhsIt = rhs.iterator();
            while (lhsIt.hasNext()) {
                if (!elementType.equals(lhsIt.next(), rhsIt.next())) {
                    return false;
                }
            }
            return true;
        }

        @Override
        public int hash(C value) {
            if (value == null) {
                return 0;
            }

            int result = 1;
            for (E element : value) {
                result = 31 * result + elementType.hash(element);
            }
            return result;
        }

        @Override
        public String getCppTypeName() {
            return "std::vector<" + elementType.getCppTypeName() + ">";
        }

        @Override
        public String getPythonTypeName() {
            return "List[" + elementType.getPythonTypeName() + "]";
        }

        @Override
        public String getJavaTypeName() {
            return "List<" + elementType.getJavaTypeName() + ">";
        }
    }

    // Type registry singleton
    public static class TypeRegistry {
        private static final TypeRegistry instance = new TypeRegistry();
        private final Map<String, TypeDescriptor<?>> typesByName = new HashMap<>();

        private TypeRegistry() {
            // Initialize primitive types
            registerPrimitiveTypes();
        }

        public static TypeRegistry getInstance() {
            return instance;
        }

        public void registerType(TypeDescriptor<?> descriptor) {
            typesByName.put(descriptor.getName(), descriptor);
        }

        public TypeDescriptor<?> getType(String name) {
            TypeDescriptor<?> descriptor = typesByName.get(name);
            if (descriptor == null) {
                throw new IllegalArgumentException("Type not found: " + name);
            }
            return descriptor;
        }

        public boolean isTypeRegistered(String name) {
            return typesByName.containsKey(name);
        }

        private void registerPrimitiveTypes() {
            registerType(new PrimitiveTypeDescriptor<>("bool", PrimitiveTypeId.BOOL,
                    Boolean::parseBoolean, String::valueOf));
            registerType(new PrimitiveTypeDescriptor<>("int32", PrimitiveTypeId.INT32,
                    Integer::parseInt, String::valueOf));
            registerType(new PrimitiveTypeDescriptor<>("int64", PrimitiveTypeId.INT64,
                    Long::parseLong, String::valueOf));
            registerType(new PrimitiveTypeDescriptor<>("float32", PrimitiveTypeId.FLOAT32,
                    Float::parseFloat, String::valueOf));
            registerType(new PrimitiveTypeDescriptor<>("float64", PrimitiveTypeId.FLOAT64,
                    Double::parseDouble, String::valueOf));
            registerType(new PrimitiveTypeDescriptor<>("string", PrimitiveTypeId.STRING,
                    s -> s, s -> s));
        }
    }
}