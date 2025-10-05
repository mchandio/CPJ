"""
CPJ IPC Module - Python ZeroMQ Integration
"""
import zmq
import threading
import queue
import time
from enum import Enum
from typing import Optional, Union

class MessageQueueMode(Enum):
    PUBLISHER = 1
    SUBSCRIBER = 2
    REQUEST = 3
    REPLY = 4

class MessageQueue:
    def __init__(self, mode: MessageQueueMode, address: str):
        self.mode = mode
        self.address = address
        self.context = zmq.Context()
        self.message_queue = queue.Queue()
        self.running = False
        
        if mode == MessageQueueMode.PUBLISHER:
            self.socket = self.context.socket(zmq.PUB)
            self.socket.bind(address)
        elif mode == MessageQueueMode.SUBSCRIBER:
            self.socket = self.context.socket(zmq.SUB)
            self.socket.connect(address)
            self.socket.setsockopt_string(zmq.SUBSCRIBE, '')
            self._start_receive_thread()
        elif mode == MessageQueueMode.REQUEST:
            self.socket = self.context.socket(zmq.REQ)
            self.socket.connect(address)
        elif mode == MessageQueueMode.REPLY:
            self.socket = self.context.socket(zmq.REP)
            self.socket.bind(address)
            self._start_receive_thread()
    
    def __del__(self):
        self.close()
    
    def close(self):
        """Clean up resources"""
        if hasattr(self, 'running') and self.running:
            self.running = False
            if hasattr(self, 'receive_thread'):
                self.receive_thread.join()
        if hasattr(self, 'socket'):
            self.socket.close()
        if hasattr(self, 'context'):
            self.context.term()
    
    def publish(self, message: Union[str, bytes]):
        """Publish a message (PUBLISHER mode only)"""
        if self.mode != MessageQueueMode.PUBLISHER:
            raise RuntimeError("Can only publish from PUBLISHER socket")
        
        if isinstance(message, str):
            message = message.encode('utf-8')
        self.socket.send(message)
    
    def send(self, message: Union[str, bytes]):
        """Send a message (REQUEST mode only)"""
        if self.mode != MessageQueueMode.REQUEST:
            raise RuntimeError("Can only send from REQUEST socket")
        
        if isinstance(message, str):
            message = message.encode('utf-8')
        self.socket.send(message)
    
    def receive(self, timeout: Optional[float] = None) -> str:
        """Receive a message"""
        try:
            message = self.message_queue.get(timeout=timeout)
            if isinstance(message, bytes):
                return message.decode('utf-8')
            return message
        except queue.Empty:
            return None
    
    def has_messages(self) -> bool:
        """Check if there are messages available"""
        return not self.message_queue.empty()
    
    def _start_receive_thread(self):
        """Start the background receiving thread"""
        self.running = True
        self.receive_thread = threading.Thread(target=self._receive_loop)
        self.receive_thread.daemon = True
        self.receive_thread.start()
    
    def _receive_loop(self):
        """Background thread for receiving messages"""
        while self.running:
            try:
                if self.socket.poll(timeout=100, flags=zmq.POLLIN):
                    message = self.socket.recv()
                    self.message_queue.put(message)
            except zmq.ZMQError:
                if not self.running:
                    break
                time.sleep(0.001)

# Example usage
if __name__ == '__main__':
    import time
    
    # Create publisher and subscriber
    publisher = MessageQueue(MessageQueueMode.PUBLISHER, "tcp://127.0.0.1:5555")
    subscriber = MessageQueue(MessageQueueMode.SUBSCRIBER, "tcp://127.0.0.1:5555")
    
    # Wait for connection to establish
    time.sleep(0.1)
    
    # Test pub/sub
    publisher.publish("Hello ZeroMQ!")
    time.sleep(0.1)  # Wait for message to be received
    
    message = subscriber.receive()
    print(f"Received: {message}")
    
    # Clean up
    publisher.close()
    subscriber.close()