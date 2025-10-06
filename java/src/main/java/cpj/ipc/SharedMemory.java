package cpj.ipc;

import java.io.RandomAccessFile;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.StandardCharsets;
import com.fasterxml.jackson.databind.ObjectMapper;

public class SharedMemory implements AutoCloseable {
    private final RandomAccessFile file;
    private final MappedByteBuffer buffer;
    private final ObjectMapper jsonMapper;
    private final String name;
    private final long size;

    public SharedMemory(String name, long size, boolean create) throws Exception {
        this.name = name;
        this.size = size;
        this.jsonMapper = new ObjectMapper();

        // Open or create shared memory file
        file = new RandomAccessFile("/dev/shm/" + name, "rw");
        if (create) {
            file.setLength(size);
        }

        // Map the file into memory
        buffer = file.getChannel().map(
                FileChannel.MapMode.READ_WRITE, 0, size);
    }

    public void write(byte[] data, int offset) {
        buffer.position(offset);
        buffer.put(data);
    }

    public byte[] read(int size, int offset) {
        buffer.position(offset);
        byte[] data = new byte[size];
        buffer.get(data);
        return data;
    }

    public void writeJson(Object data, int offset) throws Exception {
        byte[] jsonBytes = jsonMapper.writeValueAsBytes(data);
        // Write size prefix followed by JSON data
        buffer.position(offset);
        buffer.putInt(jsonBytes.length);
        buffer.put(jsonBytes);
    }

    public <T> T readJson(Class<T> valueType, int offset) throws Exception {
        buffer.position(offset);
        int size = buffer.getInt();
        byte[] jsonBytes = new byte[size];
        buffer.get(jsonBytes);
        return jsonMapper.readValue(jsonBytes, valueType);
    }

    @Override
    public void close() throws Exception {
        file.close();
    }

    public static void main(String[] args) {
        try (SharedMemory shm = new SharedMemory("test", 1024, true)) {
            // Test basic data
            byte[] testData = "Hello from Java!".getBytes(StandardCharsets.UTF_8);
            shm.write(testData, 0);
            byte[] readData = shm.read(testData.length, 0);
            System.out.println("Basic data test: " + new String(readData));

            // Test JSON data
            TestData testJson = new TestData();
            testJson.message = "Hello";
            testJson.numbers = new int[] { 1, 2, 3 };

            shm.writeJson(testJson, 0);
            TestData readJson = shm.readJson(TestData.class, 0);
            System.out.println("JSON data test: " + readJson);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Test class for JSON serialization
    public static class TestData {
        public String message;
        public int[] numbers;

        @Override
        public String toString() {
            return String.format("TestData{message='%s', numbers=%s}",
                    message, java.util.Arrays.toString(numbers));
        }
    }
}