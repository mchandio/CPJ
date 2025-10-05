"""
CPJ IPC Module - Python Named Pipe Implementation
"""
import os
import stat
import select
import time
from typing import Optional, List

class NamedPipe:
    def __init__(self, name: str, is_writer: bool):
        self.name = name
        self.is_writer = is_writer
        
        # Create the named pipe if it doesn't exist
        try:
            os.mkfifo(name, 0o666)
        except FileExistsError:
            pass
            
        # Open the pipe
        mode = "wb" if is_writer else "rb"
        flags = os.O_WRONLY | os.O_NONBLOCK if is_writer else os.O_RDONLY | os.O_NONBLOCK
        self.fd = os.open(name, flags)
        self.pipe = os.fdopen(self.fd, mode)
    
    def __del__(self):
        if hasattr(self, 'pipe'):
            self.pipe.close()
        if hasattr(self, 'fd'):
            os.close(self.fd)
        if self.is_writer:
            try:
                os.unlink(self.name)
            except FileNotFoundError:
                pass
    
    def write(self, data: bytes) -> None:
        """Write data to the pipe"""
        if not self.is_writer:
            raise RuntimeError("Pipe not opened for writing")
            
        total_written = 0
        while total_written < len(data):
            try:
                written = os.write(self.fd, data[total_written:])
                if written > 0:
                    total_written += written
            except BlockingIOError:
                # Pipe is full, wait a bit and retry
                time.sleep(0.001)  # 1ms
    
    def read(self, max_size: int = 4096) -> bytes:
        """Read data from the pipe"""
        if self.is_writer:
            raise RuntimeError("Pipe not opened for reading")
            
        try:
            return os.read(self.fd, max_size)
        except BlockingIOError:
            return b""
    
    def has_data(self) -> bool:
        """Check if pipe has data available"""
        if self.is_writer:
            raise RuntimeError("Cannot check for data on write-only pipe")
            
        r, _, _ = select.select([self.fd], [], [], 0)
        return bool(r)

# Example usage
if __name__ == '__main__':
    # Create writer and reader pipes
    writer = NamedPipe("/tmp/test_pipe", True)
    reader = NamedPipe("/tmp/test_pipe", False)
    
    # Test basic communication
    test_data = b"Hello through the pipe!"
    writer.write(test_data)
    
    # Wait for data and read
    while not reader.has_data():
        time.sleep(0.001)
    
    received = reader.read()
    print(f"Received: {received.decode()}")