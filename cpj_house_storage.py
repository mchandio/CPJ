"""CPJ House Storage Features
Provides storage-related house features like cupboards and bins for data management.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, TypeVar, Generic
from enum import Enum, auto
from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node, NodeType
from cpj_enums import AccessLevel

T = TypeVar('T')

class StorageKind(Enum):
    """Types of storage features"""
    CUPBOARD = auto()  # Long-term structured storage (classes, modules)
    BIN = auto()       # Temporary storage (variables, buffers)
    SHELF = auto()     # Organized collections (arrays, lists)
    DRAWER = auto()    # Key-value storage (dictionaries, maps)
    CHEST = auto()     # Deep storage (serialization, persistence)

@dataclass
class StoragePolicy:
    """Configuration for storage behavior"""
    capacity: Optional[int] = None  # Max items (None = unlimited)
    overflow_policy: str = "reject"  # reject, resize, evict
    persistence: bool = False  # Whether to persist across sessions
    type_check: bool = True   # Enforce type checking
    thread_safe: bool = False # Thread safety guarantees

@dataclass
class StorageMetrics:
    """Metrics for storage utilization"""
    total_capacity: int = 0
    used_capacity: int = 0
    item_count: int = 0
    access_count: int = 0
    last_access: Optional[float] = None
    eviction_count: int = 0

@dataclass
class StorageItem(Generic[T]):
    """Individual item in storage"""
    key: str
    value: T
    type_info: WallSection
    created: float
    last_accessed: float
    access_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Cupboard(Node):
    """Long-term structured storage for classes and modules"""
    name: str = field(default="")
    kind: StorageKind = field(default=StorageKind.CUPBOARD)
    policy: StoragePolicy = field(default_factory=StoragePolicy)
    metrics: StorageMetrics = field(default_factory=StorageMetrics)
    _items: Dict[str, StorageItem] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)

    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.STORAGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.kind = kwargs.get('kind', StorageKind.CUPBOARD)
        self.policy = kwargs.get('policy', StoragePolicy())
        
    def store(self, key: str, value: Any, type_hint: Optional[str] = None) -> bool:
        """Store an item with optional type checking"""
        if self.policy.type_check and type_hint and self._type_system:
            wall = self._type_system.get_type(type_hint)
            if not wall:
                raise TypeError(f"Unknown type: {type_hint}")
        else:
            wall = WallSection(TypeKind.UNDEFINED, str(type(value).__name__))
            
        # Check capacity
        if self.policy.capacity and len(self._items) >= self.policy.capacity:
            if self.policy.overflow_policy == "reject":
                return False
            elif self.policy.overflow_policy == "evict":
                self._evict_oldest()
                
        from time import time
        item = StorageItem(
            key=key,
            value=value,
            type_info=wall,
            created=time(),
            last_accessed=time()
        )
        self._items[key] = item
        self._update_metrics("store")
        return True
        
    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve an item from storage"""
        item = self._items.get(key)
        if item:
            from time import time
            item.last_accessed = time()
            item.access_count += 1
            self._update_metrics("retrieve")
            return item.value
        return None
        
    def remove(self, key: str) -> bool:
        """Remove an item from storage"""
        if key in self._items:
            del self._items[key]
            self._update_metrics("remove")
            return True
        return False
        
    def list_items(self) -> List[str]:
        """List all stored item keys"""
        return list(self._items.keys())
        
    def get_info(self, key: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a stored item"""
        item = self._items.get(key)
        if item:
            return {
                'key': item.key,
                'type': item.type_info.name,
                'created': item.created,
                'last_accessed': item.last_accessed,
                'access_count': item.access_count,
                'metadata': item.metadata
            }
        return None
        
    def _evict_oldest(self) -> None:
        """Evict the least recently accessed item"""
        if not self._items:
            return
            
        oldest_key = min(
            self._items.keys(),
            key=lambda k: self._items[k].last_accessed
        )
        del self._items[oldest_key]
        self.metrics.eviction_count += 1
        
    def _update_metrics(self, operation: str) -> None:
        """Update storage metrics after an operation"""
        from time import time
        self.metrics.item_count = len(self._items)
        self.metrics.access_count += 1
        self.metrics.last_access = time()
        # Could add more sophisticated metrics based on operation type

@dataclass
class Bin(Node):
    """Temporary storage for variables and buffers"""
    name: str = field(default="")
    kind: StorageKind = field(default=StorageKind.BIN)
    policy: StoragePolicy = field(default_factory=lambda: StoragePolicy(
        persistence=False,
        overflow_policy="evict"
    ))
    metrics: StorageMetrics = field(default_factory=StorageMetrics)
    _items: Dict[str, StorageItem] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.STORAGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.policy = kwargs.get('policy', StoragePolicy(
            persistence=False,
            overflow_policy="evict"
        ))
        
    # Similar methods to Cupboard but with temporary storage semantics
    # Implementation follows same pattern but with focus on quick access/cleanup

@dataclass
class Shelf(Node):
    """Organized collections for arrays and lists"""
    name: str = field(default="")
    kind: StorageKind = field(default=StorageKind.SHELF)
    policy: StoragePolicy = field(default_factory=StoragePolicy)
    metrics: StorageMetrics = field(default_factory=StorageMetrics)
    _items: List[StorageItem] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.STORAGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.policy = kwargs.get('policy', StoragePolicy())
        
    def append(self, value: Any, type_hint: Optional[str] = None) -> bool:
        """Add an item to the end of the shelf"""
        if self.policy.type_check and type_hint and self._type_system:
            wall = self._type_system.get_type(type_hint)
            if not wall:
                raise TypeError(f"Unknown type: {type_hint}")
        else:
            wall = WallSection(TypeKind.UNDEFINED, str(type(value).__name__))
            
        from time import time
        item = StorageItem(
            key=str(len(self._items)),
            value=value,
            type_info=wall,
            created=time(),
            last_accessed=time()
        )
        self._items.append(item)
        self._update_metrics("append")
        return True
        
    def get(self, index: int) -> Optional[Any]:
        """Get item at index"""
        if 0 <= index < len(self._items):
            item = self._items[index]
            from time import time
            item.last_accessed = time()
            item.access_count += 1
            self._update_metrics("get")
            return item.value
        return None
        
    def set(self, index: int, value: Any, type_hint: Optional[str] = None) -> bool:
        """Set item at index"""
        if not (0 <= index < len(self._items)):
            return False
            
        if self.policy.type_check and type_hint and self._type_system:
            wall = self._type_system.get_type(type_hint)
            if not wall:
                raise TypeError(f"Unknown type: {type_hint}")
                
        from time import time
        self._items[index].value = value
        self._items[index].last_accessed = time()
        self._items[index].access_count += 1
        self._update_metrics("set")
        return True
        
    def _update_metrics(self, operation: str) -> None:
        """Update storage metrics after an operation"""
        from time import time
        self.metrics.item_count = len(self._items)
        self.metrics.access_count += 1
        self.metrics.last_access = time()

@dataclass
class Drawer(Node):
    """Key-value storage for dictionaries and maps"""
    name: str = field(default="")
    kind: StorageKind = field(default=StorageKind.DRAWER)
    policy: StoragePolicy = field(default_factory=StoragePolicy)
    metrics: StorageMetrics = field(default_factory=StorageMetrics)
    _items: Dict[str, StorageItem] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.STORAGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.policy = kwargs.get('policy', StoragePolicy())
        
    # Implementation similar to Cupboard but optimized for key-value operations

@dataclass
class Chest(Node):
    """Deep storage for serialization and persistence"""
    name: str = field(default="")
    kind: StorageKind = field(default=StorageKind.CHEST)
    policy: StoragePolicy = field(default_factory=lambda: StoragePolicy(
        persistence=True
    ))
    metrics: StorageMetrics = field(default_factory=StorageMetrics)
    _items: Dict[str, StorageItem] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    _storage_path: Optional[str] = field(default=None)
    
    def __init__(self, type_system: TypeSystem, storage_path: str, **kwargs):
        super().__init__(node_type=NodeType.STORAGE, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self._storage_path = storage_path
        self.policy = kwargs.get('policy', StoragePolicy(persistence=True))
        self._load_persistent_data()
        
    def _load_persistent_data(self):
        """Load persisted data from storage"""
        import json
        import os
        if self._storage_path and os.path.exists(self._storage_path):
            try:
                with open(self._storage_path, 'r') as f:
                    data = json.load(f)
                for key, item_data in data.items():
                    from time import time
                    self._items[key] = StorageItem(
                        key=key,
                        value=item_data['value'],
                        type_info=WallSection(
                            TypeKind.UNDEFINED,
                            item_data.get('type', 'any')
                        ),
                        created=item_data.get('created', time()),
                        last_accessed=item_data.get('last_accessed', time()),
                        metadata=item_data.get('metadata', {})
                    )
            except Exception as e:
                # Log error but continue with empty storage
                print(f"Error loading persistent data: {e}")
                
    def _save_persistent_data(self):
        """Save data to persistent storage"""
        if not self._storage_path:
            return
            
        import json
        data = {
            key: {
                'value': item.value,
                'type': item.type_info.name,
                'created': item.created,
                'last_accessed': item.last_accessed,
                'metadata': item.metadata
            }
            for key, item in self._items.items()
        }
        with open(self._storage_path, 'w') as f:
            json.dump(data, f)