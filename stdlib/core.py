# CPJ Standard Library

from typing import Any, Generic, TypeVar
import functools
import threading

T = TypeVar('T')

class Collections:
    """Standard collection utilities for CPJ"""
    
    @staticmethod
    def synchronized(func):
        """Decorator for thread-safe methods"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with threading.Lock():
                return func(*args, **kwargs)
        return wrapper

class Optional(Generic[T]):
    """Optional type for null safety"""
    def __init__(self, value: T = None):
        self._value = value
    
    def get(self) -> T:
        if self._value is None:
            raise ValueError("Optional value is None")
        return self._value
    
    def is_present(self) -> bool:
        return self._value is not None

class Result(Generic[T]):
    """Result type for error handling"""
    def __init__(self, value: T = None, error: Exception = None):
        self._value = value
        self._error = error
    
    def is_success(self) -> bool:
        return self._error is None
    
    def get_value(self) -> T:
        if self._error:
            raise self._error
        return self._value