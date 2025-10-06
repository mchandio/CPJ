"""CPJ Roof Recovery System

Implements recovery strategies for different types of roof damage and system errors.
Provides automatic and manual recovery options with fallback mechanisms.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Callable, Type
from datetime import datetime
import gc
import logging
import traceback
from contextlib import contextmanager

from cpj_roof import RoofDamage, RoofSeverity, RoofMaterial
from cpj_roof_guard import RoofException, map_damage_to_exception

@dataclass
class RecoveryStrategy:
    """Base class for recovery strategies"""
    name: str
    target_material: RoofMaterial
    max_attempts: int = 3
    cooldown_seconds: float = 60.0
    
    def can_handle(self, damage: RoofDamage) -> bool:
        """Check if this strategy can handle the given damage"""
        return damage.material == self.target_material
    
    def attempt_recovery(self, damage: RoofDamage) -> bool:
        """Try to recover from the damage"""
        raise NotImplementedError

class MemoryRecovery(RecoveryStrategy):
    """Recovery strategy for memory issues"""
    def __init__(self):
        super().__init__(
            name="Memory Recovery",
            target_material=RoofMaterial.MEMORY,
            max_attempts=5
        )
        self._last_collection = None
    
    def attempt_recovery(self, damage: RoofDamage) -> bool:
        """Try to recover from memory issues"""
        # Force garbage collection
        gc.collect()
        
        # Check if memory improved
        import psutil
        current_mem = psutil.Process().memory_info().rss / (1024 * 1024)
        if current_mem < damage.context['current_mem']:
            return True
            
        # If GC didn't help, try more aggressive memory cleanup
        gc.collect(2)  # Full collection
        import sys
        sys.modules.clear()  # Clear module cache
        
        current_mem = psutil.Process().memory_info().rss / (1024 * 1024)
        return current_mem < damage.context['current_mem']

class TypeRecovery(RecoveryStrategy):
    """Recovery strategy for type system issues"""
    def __init__(self):
        super().__init__(
            name="Type Recovery",
            target_material=RoofMaterial.TYPE
        )
        self.type_fixes = {}
    
    def register_fix(self, type_name: str, fix_func: Callable):
        """Register a fix function for a specific type"""
        self.type_fixes[type_name] = fix_func
    
    def attempt_recovery(self, damage: RoofDamage) -> bool:
        """Try to recover from type violations"""
        violation = damage.context['violation']
        if isinstance(violation, str) and violation in self.type_fixes:
            try:
                self.type_fixes[violation]()
                return True
            except Exception:
                return False
        return False

class ResourceRecovery(RecoveryStrategy):
    """Recovery strategy for resource leaks"""
    def __init__(self):
        super().__init__(
            name="Resource Recovery",
            target_material=RoofMaterial.RESOURCE
        )
    
    def attempt_recovery(self, damage: RoofDamage) -> bool:
        """Try to recover from resource leaks"""
        success = True
        for res_id in damage.context['resources']:
            try:
                # Try standard file closing
                if hasattr(res_id, 'close'):
                    res_id.close()
                # Try context manager exit
                elif hasattr(res_id, '__exit__'):
                    res_id.__exit__(None, None, None)
                else:
                    success = False
            except Exception:
                success = False
        return success

class RuntimeRecovery(RecoveryStrategy):
    """Recovery strategy for runtime errors"""
    def __init__(self):
        super().__init__(
            name="Runtime Recovery",
            target_material=RoofMaterial.RUNTIME
        )
        self.fallbacks = {}
    
    def register_fallback(self, error_type: str, fallback: Callable):
        """Register a fallback handler for an error type"""
        self.fallbacks[error_type] = fallback
    
    def attempt_recovery(self, damage: RoofDamage) -> bool:
        """Try to recover from runtime errors"""
        error_type = damage.context['error_type']
        if error_type in self.fallbacks:
            try:
                self.fallbacks[error_type]()
                return True
            except Exception:
                return False
        return False

@contextmanager
def recovery_context(strategy: RecoveryStrategy):
    """Context manager for automatic recovery"""
    try:
        yield
    except RoofException as e:
        if strategy.can_handle(e.damage):
            if strategy.attempt_recovery(e.damage):
                # Recovery succeeded, continue
                pass
            else:
                # Recovery failed, re-raise
                raise

class RoofRecoveryManager:
    """Manages recovery strategies for different types of damage"""
    def __init__(self):
        self.strategies: Dict[RoofMaterial, List[RecoveryStrategy]] = {}
        self.setup_default_strategies()
        
    def setup_default_strategies(self):
        """Initialize default recovery strategies"""
        self.register_strategy(MemoryRecovery())
        self.register_strategy(TypeRecovery())
        self.register_strategy(ResourceRecovery())
        self.register_strategy(RuntimeRecovery())
    
    def register_strategy(self, strategy: RecoveryStrategy):
        """Register a new recovery strategy"""
        if strategy.target_material not in self.strategies:
            self.strategies[strategy.target_material] = []
        self.strategies[strategy.target_material].append(strategy)
    
    def get_strategies(self, damage: RoofDamage) -> List[RecoveryStrategy]:
        """Get all strategies that can handle the damage"""
        return [
            s for s in self.strategies.get(damage.material, [])
            if s.can_handle(damage)
        ]
    
    def attempt_recovery(self, damage: RoofDamage) -> bool:
        """Try all applicable strategies to recover from damage"""
        strategies = self.get_strategies(damage)
        if not strategies:
            return False
            
        for strategy in strategies:
            if strategy.attempt_recovery(damage):
                return True
        return False