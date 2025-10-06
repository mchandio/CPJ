package cpj.ipc;

import java.io.*;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Paths;

public class NamedPipe implements AutoCloseable {
    private final String name;
    private final boolean isWriter;
    private final RandomAccessFile file;
    private final FileChannel channel;

    public NamedPipe(String name, boolean isWriter) throws IOException {
        this.name = name;
        this.isWriter = isWriter;

        // Create the named pipe using native command
        try {
            ProcessBuilder pb = new ProcessBuilder("mkfifo", "-m", "666", name);
            Process p = pb.start();
            p.waitFor();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new IOException("Failed to create named pipe", e);
        }

        // Open the pipe
        String mode = isWriter ? "rw" : "r";
        file = new RandomAccessFile(name, mode);
        channel = file.getChannel();
    }

    public void write(byte[] data) throws IOException {
        if (!isWriter) {
            throw new IllegalStateException("Pipe not opened for writing");
        }

        ByteBuffer buffer = ByteBuffer.wrap(data);
        int totalWritten = 0;

        while (totalWritten < data.length) {
            try {
                int written = channel.write(buffer);
                if (written > 0) {
                    totalWritten += written;
                } else {
                    // Pipe is full, wait a bit and retry
                    try {
                        Thread.sleep(1);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                        throw new IOException("Write interrupted", e);
                    }
                }
            } catch (IOException e) {
                if (e.getMessage().contains("Resource temporarily unavailable")) {
                    // Pipe is full, wait and retry
                    try {
                        Thread.sleep(1);
                    } catch (InterruptedException ie) {
                        Thread.currentThread().interrupt();
                        throw new IOException("Write interrupted", ie);
                    }
                    continue;
                }
                throw e;
            }
        }
    }

    public byte[] read(int maxSize) throws IOException {
        if (isWriter) {
            throw new IllegalStateException("Pipe not opened for reading");
        }

        ByteBuffer buffer = ByteBuffer.allocate(maxSize);
        int bytesRead = channel.read(buffer);

        if (bytesRead < 0) {
            return new byte[0];
        }

        byte[] data = new byte[bytesRead];
        buffer.flip();
        buffer.get(data);
        return data;
    }

    public boolean hasData() throws IOException {
        if (isWriter) {
            throw new IllegalStateException("Cannot check for data on write-only pipe");
        }

        // Try to read 1 byte to check for data
        ByteBuffer probe = ByteBuffer.allocate(1);
        int available = channel.read(probe);

        if (available > 0) {
            // Put the byte back (not ideal but works for now)
            probe.flip();
            channel.position(channel.position() - 1);
            return true;
        }

        return false;
    }

    @Override
    public void close() throws Exception {
        channel.close();
        file.close();

        if (isWriter) {
            Files.deleteIfExists(Paths.get(name));
        }
    }

    public static void main(String[] args) {
        try {
            // Create writer and reader pipes
            NamedPipe writer = new NamedPipe("/tmp/test_pipe_java", true);
            NamedPipe reader = new NamedPipe("/tmp/test_pipe_java", false);

            // Test basic communication
            String testMessage = "Hello through Java pipe!";
            writer.write(testMessage.getBytes());

            // Wait for data and read
            while (!reader.hasData()) {
                Thread.sleep(1);
            }

            byte[] received = reader.read(1024);
            System.out.println("Received: " + new String(received));

            writer.close();
            reader.close();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}