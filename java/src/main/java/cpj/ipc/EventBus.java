package cpj.ipc;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Consumer;

/**
 * Event bus implementation for CPJ.
 * Handles event dispatch between components and languages.
 */
public class EventBus {
    private static final EventBus instance = new EventBus();
    private final MessageQueue messageQueue;
    private final Map<String, Map<String, Consumer<Event>>> handlers = new ConcurrentHashMap<>();
    private final String language;

    private EventBus() {
        // Start in subscriber mode to receive events
        messageQueue = new MessageQueue(MessageQueue.Mode.SUBSCRIBER, "tcp://localhost:5557");
        language = "java"; // This instance is for Java components
        startEventLoop();
    }

    public static EventBus getInstance() {
        return instance;
    }

    public void publish(Event event) throws Exception {
        MessageQueue publisher = new MessageQueue(MessageQueue.Mode.PUBLISHER, "tcp://localhost:5557");
        try {
            publisher.publishObject(event, event.getTarget());
        } finally {
            publisher.close();
        }
    }

    public void subscribe(String eventName, String handlerId, Consumer<Event> handler) {
        handlers.computeIfAbsent(eventName, k -> new ConcurrentHashMap<>())
                .put(handlerId, handler);
    }

    public void unsubscribe(String eventName, String handlerId) {
        Map<String, Consumer<Event>> eventHandlers = handlers.get(eventName);
        if (eventHandlers != null) {
            eventHandlers.remove(handlerId);
            if (eventHandlers.isEmpty()) {
                handlers.remove(eventName);
            }
        }
    }

    private void startEventLoop() {
        Thread eventThread = new Thread(() -> {
            while (true) {
                try {
                    Event event = messageQueue.receiveObject(Event.class);
                    if (event != null && (event.getTarget().equals(language) || event.getTarget().equals("all"))) {
                        Map<String, Consumer<Event>> eventHandlers = handlers.get(event.getName());
                        if (eventHandlers != null) {
                            eventHandlers.values().forEach(handler -> handler.accept(event));
                        }
                    }
                } catch (Exception e) {
                    System.err.println("Error processing event: " + e.getMessage());
                }
            }
        });
        eventThread.setDaemon(true);
        eventThread.start();
    }
}