"""
CPJ Standard Library - Collections Module
Implements core collection types that work seamlessly across C++, Python, and Java
"""

from typing import TypeVar, Generic, List, Dict, Set
import json
from dataclasses import dataclass

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

@dataclass
class CPJCollection(Generic[T]):
    """Base class for all CPJ collections with cross-language support"""
    _data: List[T]
    _type: str

    def to_json(self) -> str:
        """Convert to JSON for cross-language transfer"""
        return json.dumps({
            "type": self._type,
            "data": self._data
        })

    @classmethod
    def from_json(cls, json_str: str) -> 'CPJCollection[T]':
        """Create collection from JSON (used by C++ and Java runtimes)"""
        data = json.loads(json_str)
        return cls(data["data"], data["type"])

class CPJList(CPJCollection[T]):
    """List implementation that works across all three languages"""
    def __init__(self, items: List[T] = None):
        super().__init__(items or [], "list")

    def append(self, item: T) -> None:
        self._data.append(item)

    def extend(self, other: 'CPJList[T]') -> None:
        self._data.extend(other._data)

    def map(self, fn) -> 'CPJList[T]':
        """Higher-order function support"""
        return CPJList([fn(x) for x in self._data])

    def filter(self, pred) -> 'CPJList[T]':
        return CPJList([x for x in self._data if pred(x)])

class CPJDict(CPJCollection[Dict[K, V]]):
    """Dictionary implementation with cross-language support"""
    def __init__(self, items: Dict[K, V] = None):
        super().__init__(items or {}, "dict")

    def set(self, key: K, value: V) -> None:
        self._data[key] = value

    def get(self, key: K, default: V = None) -> V:
        return self._data.get(key, default)

class CPJSet(CPJCollection[T]):
    """Set implementation that works in all three languages"""
    def __init__(self, items: Set[T] = None):
        super().__init__(set(items or []), "set")

    def add(self, item: T) -> None:
        self._data.add(item)

    def remove(self, item: T) -> None:
        self._data.remove(item)

    def union(self, other: 'CPJSet[T]') -> 'CPJSet[T]':
        return CPJSet(self._data.union(other._data))

# Example usage in Python:
def example():
    # Create a list
    numbers = CPJList([1, 2, 3, 4, 5])
    
    # Map and filter operations
    doubled = numbers.map(lambda x: x * 2)
    evens = doubled.filter(lambda x: x % 2 == 0)
    
    # Convert to JSON for C++ or Java
    json_data = evens.to_json()
    
    # Create from JSON (simulating C++ or Java sending data)
    received = CPJList[int].from_json(json_data)
    
    # Dictionary example
    points = CPJDict[str, tuple]()
    points.set("origin", (0, 0))
    points.set("end", (100, 100))
    
    # Set operations
    set1 = CPJSet([1, 2, 3])
    set2 = CPJSet([3, 4, 5])
    union = set1.union(set2)
    
    return {
        "list": received._data,
        "dict": points._data,
        "set": union._data
    }