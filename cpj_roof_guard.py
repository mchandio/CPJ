"""CPJ Roof Guard Exception System

Specialized exceptions for the roof protection system that provide detailed
error information and recovery suggestions.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type
from datetime import datetime
from cpj_roof import RoofDamage, RoofSeverity, RoofMaterial

class RoofException(Exception):
    """Base exception for all roof-related errors"""
    def __init__(self, damage: RoofDamage):
        self.damage = damage
        super().__init__(str(damage.message))

class MemoryLeakError(RoofException):
    """Raised when memory leaks are detected"""
    def __init__(self, damage: RoofDamage):
        super().__init__(damage)
        self.current_mem = damage.context.get('current_mem')
        self.last_check = damage.context.get('last_check')
    
    def __str__(self):
        return (f"Memory leak detected: {self.current_mem - self.last_check:.2f}MB increase. "
                f"Current: {self.current_mem:.2f}MB, Last: {self.last_check:.2f}MB")

class TypeViolationError(RoofException):
    """Raised when type system integrity is violated"""
    def __init__(self, damage: RoofDamage):
        super().__init__(damage)
        self.violation = damage.context.get('violation')
    
    def __str__(self):
        return f"Type system violation: {self.violation}"

class ResourceLeakError(RoofException):
    """Raised when resources are not properly cleaned up"""
    def __init__(self, damage: RoofDamage):
        super().__init__(damage)
        self.resources = damage.context.get('resources', [])
    
    def __str__(self):
        return f"Resource leak detected: {len(self.resources)} unclosed resources"

class RecurringRuntimeError(RoofException):
    """Raised when the same runtime error occurs repeatedly"""
    def __init__(self, damage: RoofDamage):
        super().__init__(damage)
        self.error_type = damage.context.get('error_type')
        self.error_context = damage.context.get('context')
        self.count = damage.context.get('count')
    
    def __str__(self):
        return (f"Recurring {self.error_type} in {self.error_context}: "
                f"occurred {self.count} times")

class StructuralIntegrityError(RoofException):
    """Raised when house structure is compromised"""
    def __init__(self, damage: RoofDamage, affected_areas: List[str]):
        super().__init__(damage)
        self.affected_areas = affected_areas
    
    def __str__(self):
        return (f"Structural integrity compromised in: "
                f"{', '.join(self.affected_areas)}")

class WeatherDamageError(RoofException):
    """Raised when external factors cause system issues"""
    def __init__(self, damage: RoofDamage, weather_condition: str):
        super().__init__(damage)
        self.weather_condition = weather_condition
    
    def __str__(self):
        return f"System affected by {self.weather_condition}"

def map_damage_to_exception(damage: RoofDamage) -> Type[RoofException]:
    """Maps roof damage to appropriate exception type"""
    mapping = {
        RoofMaterial.MEMORY: MemoryLeakError,
        RoofMaterial.TYPE: TypeViolationError,
        RoofMaterial.RESOURCE: ResourceLeakError,
        RoofMaterial.RUNTIME: RecurringRuntimeError,
    }
    return mapping.get(damage.material, RoofException)

def raise_roof_error(damage: RoofDamage):
    """Raises appropriate exception for roof damage"""
    exception_class = map_damage_to_exception(damage)
    raise exception_class(damage)