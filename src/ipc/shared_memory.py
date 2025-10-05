"""
CPJ IPC Module - Python Bindings for Shared Memory
"""
import mmap
import os
import struct
from typing import Optional, Any
import json

class SharedMemory:
    def __init__(self, name: str, size: int, create: bool = False):
        self.name = name
        self.size = size
        
        if create:
            self.fd = os.open(f"/dev/shm/{name}", os.O_CREAT | os.O_RDWR, 0o666)
            os.truncate(self.fd, size)
        else:
            self.fd = os.open(f"/dev/shm/{name}", os.O_RDWR)
            
        self.mmap = mmap.mmap(self.fd, size)
    
    def __del__(self):
        if hasattr(self, 'mmap'):
            self.mmap.close()
        if hasattr(self, 'fd'):
            os.close(self.fd)
    
    def write(self, data: bytes, offset: int = 0) -> None:
        """Write bytes to shared memory at specified offset"""
        self.mmap[offset:offset + len(data)] = data
    
    def read(self, size: int, offset: int = 0) -> bytes:
        """Read bytes from shared memory at specified offset"""
        return bytes(self.mmap[offset:offset + size])
    
    def write_json(self, data: Any, offset: int = 0) -> None:
        """Write JSON-serializable data to shared memory"""
        json_bytes = json.dumps(data).encode('utf-8')
        # Write size prefix followed by data
        self.write(struct.pack('!I', len(json_bytes)), offset)
        self.write(json_bytes, offset + 4)
    
    def read_json(self, offset: int = 0) -> Any:
        """Read JSON data from shared memory"""
        size = struct.unpack('!I', self.read(4, offset))[0]
        json_bytes = self.read(size, offset + 4)
        return json.loads(json_bytes.decode('utf-8'))

# Example usage
if __name__ == '__main__':
    # Create shared memory
    shm = SharedMemory("test", 1024, create=True)
    
    # Write and read basic data
    test_data = b"Hello from Python!"
    shm.write(test_data)
    read_data = shm.read(len(test_data))
    print(f"Basic data test: {read_data.decode()}")
    
    # Write and read JSON data
    test_json = {
        "message": "Hello",
        "data": [1, 2, 3],
        "nested": {"key": "value"}
    }
    shm.write_json(test_json)
    read_json = shm.read_json()
    print(f"JSON data test: {read_json}")