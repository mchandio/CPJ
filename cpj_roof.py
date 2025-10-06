"""CPJ Roof System - Protection and Error Handling

The roof system provides comprehensive error handling and recovery mechanisms:
- RoofTile: Base class for error handlers
- RoofSection: Groups related error handlers
- WeatherGuard: Protection against external threats
- LeakPrevention: Memory and resource leak protection
- StructuralSupport: Type system and integrity checks
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Callable, Type
import traceback
import logging
from datetime import datetime

# Roof system severity levels
class RoofSeverity(Enum):
    MINOR = auto()  # Can be handled automatically
    MODERATE = auto()  # Requires attention but not critical 
    SEVERE = auto()  # Critical issue requiring immediate action
    CATASTROPHIC = auto()  # System cannot continue

class RoofMaterial(Enum):
    MEMORY = auto()  # Memory protection
    TYPE = auto()  # Type system protection
    RESOURCE = auto()  # Resource management
    SECURITY = auto()  # Security protection
    RUNTIME = auto()  # Runtime error protection

@dataclass
class RoofDamage:
    """Represents a problem detected by the roof system"""
    severity: RoofSeverity
    material: RoofMaterial
    message: str
    timestamp: datetime = field(default_factory=datetime.now)
    stack_trace: str = field(default_factory=lambda: traceback.format_exc())
    context: Dict[str, Any] = field(default_factory=dict)

@dataclass 
class RoofTile:
    """Base class for error handlers"""
    name: str
    material: RoofMaterial
    severity_threshold: RoofSeverity = RoofSeverity.MINOR
    auto_repair: bool = True
    
    def inspect(self) -> Optional[RoofDamage]:
        """Check for problems"""
        raise NotImplementedError
        
    def repair(self, damage: RoofDamage) -> bool:
        """Try to fix a detected problem"""
        raise NotImplementedError

@dataclass
class RoofSection:
    """A group of related error handlers"""
    name: str
    tiles: List[RoofTile] = field(default_factory=list)
    active: bool = True
    
    def add_tile(self, tile: RoofTile):
        """Add an error handler to this section"""
        self.tiles.append(tile)
    
    def inspect_all(self) -> List[RoofDamage]:
        """Check all tiles for problems"""
        damages = []
        if not self.active:
            return damages
            
        for tile in self.tiles:
            damage = tile.inspect()
            if damage:
                damages.append(damage)
                
        return damages
    
    def repair_all(self, damages: List[RoofDamage]) -> List[RoofDamage]:
        """Try to repair all detected problems"""
        remaining = []
        if not self.active:
            return damages
            
        for damage in damages:
            # Find tile responsible for this type of damage
            for tile in self.tiles:
                if tile.material == damage.material:
                    if not tile.repair(damage):
                        remaining.append(damage)
                    break
                    
        return remaining

class MemoryLeakTile(RoofTile):
    """Handles memory leak detection and cleanup"""
    def __init__(self, threshold_mb: float = 100):
        super().__init__(
            name="Memory Leak Guard",
            material=RoofMaterial.MEMORY,
            severity_threshold=RoofSeverity.MODERATE
        )
        self.threshold_mb = threshold_mb
        self.last_check = None
        self._leaked_objects = {}
    
    def inspect(self) -> Optional[RoofDamage]:
        """Check for memory leaks"""
        import psutil
        import gc
        
        process = psutil.Process()
        current_mem = process.memory_info().rss / (1024 * 1024)  # Convert to MB
        
        if self.last_check and (current_mem - self.last_check) > self.threshold_mb:
            gc.collect()  # Try collection first
            
            # If still above threshold, report damage
            if (current_mem - self.last_check) > self.threshold_mb:
                return RoofDamage(
                    severity=RoofSeverity.MODERATE,
                    material=RoofMaterial.MEMORY,
                    message=f"Memory leak detected: {current_mem - self.last_check:.2f}MB increase",
                    context={'current_mem': current_mem, 'last_check': self.last_check}
                )
        
        self.last_check = current_mem
        return None
    
    def repair(self, damage: RoofDamage) -> bool:
        """Try to fix memory leaks"""
        import gc
        gc.collect()  # Force garbage collection
        
        # Check if memory usage decreased
        current_mem = psutil.Process().memory_info().rss / (1024 * 1024)
        return current_mem < damage.context['current_mem']

class TypeGuardTile(RoofTile):
    """Enforces type system integrity"""
    def __init__(self):
        super().__init__(
            name="Type System Guard",
            material=RoofMaterial.TYPE,
            severity_threshold=RoofSeverity.SEVERE
        )
        self.type_violations = []
    
    def inspect(self) -> Optional[RoofDamage]:
        """Check for type violations"""
        if self.type_violations:
            violation = self.type_violations[0]
            return RoofDamage(
                severity=RoofSeverity.SEVERE,
                material=RoofMaterial.TYPE,
                message=f"Type violation: {violation}",
                context={'violation': violation}
            )
        return None
    
    def repair(self, damage: RoofDamage) -> bool:
        """Try to fix type violations"""
        # Remove the violation if it was handled
        if damage.context['violation'] in self.type_violations:
            self.type_violations.remove(damage.context['violation'])
            return True
        return False

class ResourceGuardTile(RoofTile):
    """Manages resource cleanup and protection"""
    def __init__(self):
        super().__init__(
            name="Resource Guard",
            material=RoofMaterial.RESOURCE,
            severity_threshold=RoofSeverity.MODERATE
        )
        self.open_resources = {}
    
    def track_resource(self, resource: Any, cleanup_func: Callable):
        """Register a resource for tracking"""
        self.open_resources[id(resource)] = (resource, cleanup_func)
    
    def release_resource(self, resource: Any):
        """Clean up a tracked resource"""
        res_id = id(resource)
        if res_id in self.open_resources:
            _, cleanup = self.open_resources[res_id]
            cleanup()
            del self.open_resources[res_id]
    
    def inspect(self) -> Optional[RoofDamage]:
        """Check for resource leaks"""
        if self.open_resources:
            return RoofDamage(
                severity=RoofSeverity.MODERATE,
                material=RoofMaterial.RESOURCE,
                message=f"Unclosed resources: {len(self.open_resources)}",
                context={'resources': list(self.open_resources.keys())}
            )
        return None
    
    def repair(self, damage: RoofDamage) -> bool:
        """Try to clean up leaked resources"""
        try:
            for res_id in damage.context['resources']:
                if res_id in self.open_resources:
                    self.release_resource(self.open_resources[res_id][0])
            return True
        except Exception:
            return False

class RuntimeGuardTile(RoofTile):
    """Handles runtime error protection"""
    def __init__(self):
        super().__init__(
            name="Runtime Guard",
            material=RoofMaterial.RUNTIME,
            severity_threshold=RoofSeverity.SEVERE
        )
        self.error_count = {}
        self.max_retries = 3
    
    def track_error(self, error_type: Type[Exception], context: str):
        """Track occurrence of an error"""
        key = (error_type, context)
        self.error_count[key] = self.error_count.get(key, 0) + 1
    
    def inspect(self) -> Optional[RoofDamage]:
        """Check for recurring errors"""
        for (error_type, context), count in self.error_count.items():
            if count >= self.max_retries:
                return RoofDamage(
                    severity=RoofSeverity.SEVERE,
                    material=RoofMaterial.RUNTIME,
                    message=f"Recurring {error_type.__name__} in {context}: {count} times",
                    context={
                        'error_type': error_type.__name__,
                        'context': context,
                        'count': count
                    }
                )
        return None
    
    def repair(self, damage: RoofDamage) -> bool:
        """Try to handle recurring errors"""
        # Reset error count if handling was successful
        key = (eval(damage.context['error_type']), damage.context['context'])
        if key in self.error_count:
            del self.error_count[key]
            return True
        return False