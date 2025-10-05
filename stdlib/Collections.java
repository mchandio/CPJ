package stdlib;

import java.util.*;
import java.util.function.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.type.TypeReference;

public class Collections {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static class Collection<T> {
        protected String type;
        protected Object data;

        protected Collection(String type, Object data) {
            this.type = type;
            this.data = data;
        }

        public String toJson() throws Exception {
            Map<String, Object> json = new HashMap<>();
            json.put("type", type);
            json.put("data", data);
            return mapper.writeValueAsString(json);
        }
    }

    public static class CPJList<T> extends Collection<T> {
        private List<T> items;

        public CPJList() {
            super("list", new ArrayList<T>());
            this.items = new ArrayList<>();
        }

        public CPJList(List<T> items) {
            super("list", items);
            this.items = items;
        }

        public static <T> CPJList<T> fromJson(String jsonStr) throws Exception {
            Map<String, Object> json = mapper.readValue(jsonStr, new TypeReference<Map<String, Object>>() {
            });
            if (!"list".equals(json.get("type"))) {
                throw new IllegalArgumentException("Invalid collection type");
            }
            List<T> items = mapper.convertValue(json.get("data"), new TypeReference<List<T>>() {
            });
            return new CPJList<>(items);
        }

        public void append(T item) {
            items.add(item);
        }

        public <R> CPJList<R> map(Function<T, R> func) {
            List<R> result = new ArrayList<>();
            for (T item : items) {
                result.add(func.apply(item));
            }
            return new CPJList<>(result);
        }

        public CPJList<T> filter(Predicate<T> pred) {
            List<T> result = new ArrayList<>();
            for (T item : items) {
                if (pred.test(item)) {
                    result.add(item);
                }
            }
            return new CPJList<>(result);
        }
    }

    public static class CPJDict<K, V> extends Collection<Map.Entry<K, V>> {
        private Map<K, V> items;

        public CPJDict() {
            super("dict", new HashMap<K, V>());
            this.items = new HashMap<>();
        }

        public static <K, V> CPJDict<K, V> fromJson(String jsonStr) throws Exception {
            Map<String, Object> json = mapper.readValue(jsonStr, new TypeReference<Map<String, Object>>() {
            });
            if (!"dict".equals(json.get("type"))) {
                throw new IllegalArgumentException("Invalid collection type");
            }
            Map<K, V> items = mapper.convertValue(json.get("data"), new TypeReference<Map<K, V>>() {
            });
            CPJDict<K, V> result = new CPJDict<>();
            items.forEach(result::set);
            return result;
        }

        public void set(K key, V value) {
            items.put(key, value);
        }

        public V get(K key, V defaultValue) {
            return items.getOrDefault(key, defaultValue);
        }
    }

    public static class CPJSet<T> extends Collection<T> {
        private Set<T> items;

        public CPJSet() {
            super("set", new HashSet<T>());
            this.items = new HashSet<>();
        }

        public CPJSet(Set<T> items) {
            super("set", items);
            this.items = items;
        }

        public static <T> CPJSet<T> fromJson(String jsonStr) throws Exception {
            Map<String, Object> json = mapper.readValue(jsonStr, new TypeReference<Map<String, Object>>() {
            });
            if (!"set".equals(json.get("type"))) {
                throw new IllegalArgumentException("Invalid collection type");
            }
            List<T> list = mapper.convertValue(json.get("data"), new TypeReference<List<T>>() {
            });
            return new CPJSet<>(new HashSet<>(list));
        }

        public void add(T item) {
            items.add(item);
        }

        public void remove(T item) {
            items.remove(item);
        }

        public CPJSet<T> union(CPJSet<T> other) {
            Set<T> result = new HashSet<>(items);
            result.addAll(other.items);
            return new CPJSet<>(result);
        }
    }

    // Example usage
    public static void main(String[] args) throws Exception {
        // Create a list
        CPJList<Integer> numbers = new CPJList<>();
        numbers.append(1);
        numbers.append(2);
        numbers.append(3);

        // Map and filter operations
        CPJList<Integer> doubled = numbers.map(x -> x * 2);
        CPJList<Integer> evens = doubled.filter(x -> x % 2 == 0);

        // Convert to JSON
        String json = evens.toJson();
        System.out.println("JSON: " + json);

        // Create from JSON
        CPJList<Integer> received = CPJList.fromJson(json);

        // Dictionary example
        CPJDict<String, int[]> points = new CPJDict<>();
        points.set("origin", new int[] { 0, 0 });
        points.set("end", new int[] { 100, 100 });

        // Set operations
        CPJSet<Integer> set1 = new CPJSet<>();
        set1.add(1);
        set1.add(2);
        set1.add(3);

        CPJSet<Integer> set2 = new CPJSet<>();
        set2.add(3);
        set2.add(4);
        set2.add(5);

        CPJSet<Integer> union = set1.union(set2);
    }
}