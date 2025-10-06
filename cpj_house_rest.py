"""CPJ House Rest Features
Provides rest-related features like beds and chairs for process suspension and async operations.
"""

import asyncio
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Callable, Awaitable, TypeVar, Generic
from enum import Enum, auto
from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node, NodeType
from cpj_enums import AccessLevel

T = TypeVar('T')

class RestKind(Enum):
    """Types of rest features"""
    BED = auto()         # Long-term process suspension
    CHAIR = auto()       # Short-term async wait
    COUCH = auto()       # Cooperative multitasking
    HAMMOCK = auto()     # Lazy evaluation
    BENCH = auto()       # Parallel processing wait

@dataclass
class SuspensionState:
    """State of a suspended process"""
    process_id: str
    start_time: float
    wake_time: Optional[float] = None
    priority: int = 0
    context: Dict[str, Any] = field(default_factory=dict)
    callbacks: List[Callable[[], None]] = field(default_factory=list)

@dataclass
class AsyncTask(Generic[T]):
    """Asynchronous task wrapper"""
    name: str
    coroutine: Awaitable[T]
    created: float
    status: str = "pending"
    result: Optional[T] = None
    error: Optional[Exception] = None

@dataclass
class Bed(Node):
    """Long-term process suspension"""
    name: str = field(default="")
    kind: RestKind = field(default=RestKind.BED)
    capacity: int = field(default=10)
    _suspended: Dict[str, SuspensionState] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.REST, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.capacity = kwargs.get('capacity', 10)
        
    async def suspend(self, process_id: str, duration: Optional[float] = None,
                     context: Optional[Dict[str, Any]] = None,
                     priority: int = 0) -> bool:
        """Suspend a process for a given duration"""
        if len(self._suspended) >= self.capacity:
            return False
            
        from time import time
        state = SuspensionState(
            process_id=process_id,
            start_time=time(),
            wake_time=time() + duration if duration else None,
            priority=priority,
            context=context or {}
        )
        self._suspended[process_id] = state
        
        if duration:
            await asyncio.sleep(duration)
            await self.wake(process_id)
            
        return True
        
    async def wake(self, process_id: str) -> Optional[Dict[str, Any]]:
        """Wake a suspended process"""
        state = self._suspended.get(process_id)
        if not state:
            return None
            
        # Execute callbacks
        for callback in state.callbacks:
            try:
                callback()
            except Exception as e:
                print(f"Callback error for {process_id}: {e}")
                
        # Remove from suspended state
        del self._suspended[process_id]
        return state.context
        
    def add_wake_callback(self, process_id: str, callback: Callable[[], None]) -> bool:
        """Add a callback to be executed when process wakes"""
        state = self._suspended.get(process_id)
        if state:
            state.callbacks.append(callback)
            return True
        return False
        
    def get_suspended(self) -> List[str]:
        """Get list of suspended process IDs"""
        return list(self._suspended.keys())

@dataclass
class Chair(Node):
    """Short-term async operation management"""
    name: str = field(default="")
    kind: RestKind = field(default=RestKind.CHAIR)
    max_concurrent: int = field(default=5)
    _tasks: Dict[str, AsyncTask] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.REST, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.max_concurrent = kwargs.get('max_concurrent', 5)
        
    async def execute(self, name: str, coroutine: Awaitable[T]) -> AsyncTask[T]:
        """Execute an async task"""
        from time import time
        task = AsyncTask(
            name=name,
            coroutine=coroutine,
            created=time()
        )
        self._tasks[name] = task
        
        try:
            # Ensure we don't exceed max_concurrent
            while sum(1 for t in self._tasks.values() if t.status == "running") >= self.max_concurrent:
                await asyncio.sleep(0.1)
                
            task.status = "running"
            task.result = await coroutine
            task.status = "completed"
        except Exception as e:
            task.status = "failed"
            task.error = e
            
        return task
        
    def get_task(self, name: str) -> Optional[AsyncTask]:
        """Get task by name"""
        return self._tasks.get(name)
        
    def list_tasks(self) -> List[str]:
        """List all task names"""
        return list(self._tasks.keys())
        
    def get_active_tasks(self) -> List[str]:
        """Get names of currently running tasks"""
        return [name for name, task in self._tasks.items()
                if task.status == "running"]

@dataclass
class Couch(Node):
    """Cooperative multitasking support"""
    name: str = field(default="")
    kind: RestKind = field(default=RestKind.COUCH)
    _coroutines: List[Awaitable] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.REST, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_coroutine(self, coroutine: Awaitable):
        """Add a coroutine to the cooperative multitasking pool"""
        self._coroutines.append(coroutine)
        
    async def run_all(self):
        """Run all coroutines cooperatively"""
        if self._coroutines:
            await asyncio.gather(*self._coroutines)
            self._coroutines = []

@dataclass
class Hammock(Node):
    """Lazy evaluation support"""
    name: str = field(default="")
    kind: RestKind = field(default=RestKind.HAMMOCK)
    _pending: Dict[str, Callable[[], T]] = field(default_factory=dict)
    _cached: Dict[str, T] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.REST, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def register(self, name: str, func: Callable[[], T]):
        """Register a function for lazy evaluation"""
        self._pending[name] = func
        
    def evaluate(self, name: str) -> Optional[T]:
        """Evaluate and cache a registered function"""
        if name in self._cached:
            return self._cached[name]
            
        if name in self._pending:
            result = self._pending[name]()
            self._cached[name] = result
            return result
            
        return None
        
    def invalidate(self, name: str):
        """Invalidate cached result"""
        self._cached.pop(name, None)

@dataclass
class Bench(Node):
    """Parallel processing coordination"""
    name: str = field(default="")
    kind: RestKind = field(default=RestKind.BENCH)
    workers: int = field(default=4)
    _queue: asyncio.Queue = field(default_factory=asyncio.Queue)
    _results: Dict[str, Any] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.REST, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.workers = kwargs.get('workers', 4)
        
    async def process_parallel(self, tasks: List[Tuple[str, Callable]]):
        """Process tasks in parallel"""
        # Create worker tasks
        workers = [
            asyncio.create_task(self._worker())
            for _ in range(self.workers)
        ]
        
        # Add tasks to queue
        for task_id, func in tasks:
            await self._queue.put((task_id, func))
            
        # Add sentinel values to stop workers
        for _ in range(self.workers):
            await self._queue.put((None, None))
            
        # Wait for all workers to complete
        await asyncio.gather(*workers)
        
    async def _worker(self):
        """Worker process for parallel execution"""
        while True:
            task_id, func = await self._queue.get()
            if task_id is None:  # Check for sentinel
                break
                
            try:
                result = await func() if asyncio.iscoroutinefunction(func) else func()
                self._results[task_id] = {
                    'status': 'completed',
                    'result': result
                }
            except Exception as e:
                self._results[task_id] = {
                    'status': 'failed',
                    'error': str(e)
                }
            finally:
                self._queue.task_done()
                
    def get_result(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get result for a specific task"""
        return self._results.get(task_id)