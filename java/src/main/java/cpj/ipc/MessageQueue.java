package cpj.ipc;

import org.zeromq.SocketType;
import org.zeromq.ZMQ;
import org.zeromq.ZContext;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicBoolean;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

public class MessageQueue implements AutoCloseable {
    public enum Mode {
        PUBLISHER,
        SUBSCRIBER,
        REQUEST,
        REPLY
    }

    private final Mode mode;
    private final String address;
    private final ZContext context;
    private final ZMQ.Socket socket;
    private final BlockingQueue<String> messageQueue;
    private final AtomicBoolean running;
    private Thread receiveThread;
    private final ObjectMapper jsonMapper = new ObjectMapper();

    public MessageQueue(Mode mode, String address) {
        this.mode = mode;
        this.address = address;
        this.context = new ZContext();
        this.messageQueue = new LinkedBlockingQueue<>();
        this.running = new AtomicBoolean(false);

        switch (mode) {
            case PUBLISHER:
                socket = context.createSocket(SocketType.PUB);
                socket.bind(address);
                break;
            case SUBSCRIBER:
                socket = context.createSocket(SocketType.SUB);
                socket.connect(address);
                socket.subscribe("".getBytes());
                startReceiveThread();
                break;
            case REQUEST:
                socket = context.createSocket(SocketType.REQ);
                socket.connect(address);
                break;
            case REPLY:
                socket = context.createSocket(SocketType.REP);
                socket.bind(address);
                startReceiveThread();
                break;
            default:
                throw new IllegalArgumentException("Invalid mode: " + mode);
        }
    }

    public void publish(String message) {
        if (mode != Mode.PUBLISHER) {
            throw new IllegalStateException("Can only publish from PUBLISHER socket");
        }
        socket.send(message.getBytes(ZMQ.CHARSET));
    }

    public void publishObject(Object obj, String targetLang) throws Exception {
        if (mode != Mode.PUBLISHER) {
            throw new IllegalStateException("Can only publish from PUBLISHER socket");
        }
        String jsonStr = TypeMarshaller.marshal(obj, obj.getClass().getSimpleName(), targetLang);
        socket.send(jsonStr.getBytes(ZMQ.CHARSET));
    }

    public void send(String message) {
        if (mode != Mode.REQUEST) {
            throw new IllegalStateException("Can only send from REQUEST socket");
        }
        socket.send(message.getBytes(ZMQ.CHARSET));
    }

    public String receive() throws InterruptedException {
        return messageQueue.take();
    }

    public String receive(long timeout) throws InterruptedException {
        String message = messageQueue.poll(timeout, java.util.concurrent.TimeUnit.MILLISECONDS);
        return message;
    }

    public <T> T receiveObject(Class<T> type) throws Exception {
        String message = messageQueue.take();
        return TypeMarshaller.unmarshal(message, type);
    }

    public <T> T receiveObject(Class<T> type, long timeout) throws InterruptedException, JsonProcessingException {
        String message = receive(timeout);
        if (message == null)
            return null;
        return jsonMapper.readValue(message, type);
    }

    public boolean hasMessages() {
        return !messageQueue.isEmpty();
    }

    private void startReceiveThread() {
        running.set(true);
        receiveThread = new Thread(() -> {
            while (running.get()) {
                byte[] message = socket.recv(ZMQ.DONTWAIT);
                if (message != null) {
                    messageQueue.offer(new String(message, ZMQ.CHARSET));
                }
                try {
                    Thread.sleep(1);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                }
            }
        });
        receiveThread.setDaemon(true);
        receiveThread.start();
    }

    @Override
    public void close() {
        running.set(false);
        if (receiveThread != null) {
            System.out.println("Closing message queue at address: " + address);
            receiveThread.interrupt();
            try {
                receiveThread.join(1000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        socket.close();
        context.close();
    }

    public static void main(String[] args) {
        try {
            // Create publisher and subscriber
            MessageQueue publisher = new MessageQueue(Mode.PUBLISHER, "tcp://127.0.0.1:5556");
            MessageQueue subscriber = new MessageQueue(Mode.SUBSCRIBER, "tcp://127.0.0.1:5556");

            // Wait for connection to establish
            Thread.sleep(100);

            // Test pub/sub
            publisher.publish("Hello from Java ZeroMQ!");
            Thread.sleep(100); // Wait for message to be received

            String message = subscriber.receive(1000);
            System.out.println("Received: " + message);

            // Clean up
            publisher.close();
            subscriber.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}