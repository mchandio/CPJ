package cpj.runtime;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import cpj.ipc.MessageQueue;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.UUID;

/**
 * Memory management system for cross-language object tracking.
 * Implements reference counting for objects shared between C++, Python, and
 * Java.
 */
public class MemoryManager {
    private static final MemoryManager instance = new MemoryManager();
    private final Map<String, TrackedObject> objects = new ConcurrentHashMap<>();

    private MemoryManager() {
    }

    public static MemoryManager getInstance() {
        return instance;
    }

    public String trackObject(Object obj, String sourceLanguage) {
        String id = UUID.randomUUID().toString();
        objects.put(id, new TrackedObject(obj, sourceLanguage));
        return id;
    }

    public void incrementRef(String objectId) {
        TrackedObject obj = objects.get(objectId);
        if (obj != null) {
            obj.incrementRef();
        }
    }

    public void decrementRef(String objectId) {
        TrackedObject obj = objects.get(objectId);
        if (obj != null && obj.decrementRef() == 0) {
            objects.remove(objectId);
            // If object is from another language, notify its runtime to cleanup
            if (!obj.sourceLanguage.equals("java")) {
                notifyForeignRuntime(objectId, obj.sourceLanguage);
            }
        }
    }

    private void notifyForeignRuntime(String objectId, String language) {
        try {
            switch (language) {
                case "python":
                    // Notify Python runtime via MessageQueue
                    try (MessageQueue queue = new MessageQueue(MessageQueue.Mode.REQUEST, "tcp://localhost:5558")) {
                        Map<String, Object> data = Map.of(
                                "type", "cleanup",
                                "objectId", objectId);
                        queue.publishObject(data, "python");
                    }
                    break;
                case "cpp":
                    // Notify C++ runtime via MessageQueue
                    try (MessageQueue queue = new MessageQueue(MessageQueue.Mode.REQUEST, "tcp://localhost:5559")) {
                        Map<String, Object> data = Map.of(
                                "type", "cleanup",
                                "objectId", objectId);
                        queue.publishObject(data, "cpp");
                    }
                    break;
            }
        } catch (Exception e) {
            System.err.println("Error notifying foreign runtime: " + e.getMessage());
        }
    }

    private static class TrackedObject {
        final Object object;
        final String sourceLanguage;
        final AtomicInteger refCount;

        TrackedObject(Object object, String sourceLanguage) {
            this.object = object;
            this.sourceLanguage = sourceLanguage;
            this.refCount = new AtomicInteger(1);
        }

        int incrementRef() {
            return refCount.incrementAndGet();
        }

        int decrementRef() {
            return refCount.decrementAndGet();
        }
    }
}