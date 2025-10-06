"""Runtime execution support for house features including Windows, Doors, Lights, and Storage."""

import logging
import inspect
from datetime import datetime
from typing import Any, Dict, List, Optional
from cpj_enums import AccessLevel
from cpj_type_system import WallSection, TypeSystem
from cpj_house_storage_runtime import StorageManager

class WindowManager:
    """Manages debug/inspection windows"""
    
    def __init__(self):
        self._inspectable_values = {}
        self._access_levels = {}
    
    def register_inspectable(self, name: str, value: Any, access_level: AccessLevel = AccessLevel.PUBLIC):
        """Register a value that can be inspected through a window"""
        self._inspectable_values[name] = value
        self._access_levels[name] = access_level
    
    def inspect(self, target: str, caller_access: AccessLevel = AccessLevel.PUBLIC) -> Optional[Dict[str, Any]]:
        """Inspect a value through a window"""
        if target not in self._inspectable_values:
            return None
            
        required_access = self._access_levels[target]
        if (caller_access == AccessLevel.PRIVATE or 
            (caller_access == AccessLevel.PROTECTED and required_access == AccessLevel.PRIVATE)):
            return None
            
        value = self._inspectable_values[target]
        result = {
            'value': str(value),
            'type': type(value).__name__,
            'timestamp': datetime.now().isoformat()
        }
        
        if inspect.isfunction(value):
            result['signature'] = str(inspect.signature(value))
            # Add docstring if available
            doc = inspect.getdoc(value)
            if doc:
                result['docstring'] = doc
            
        return result

class DoorManager:
    """Manages access control between rooms/functions"""
    
    def __init__(self):
        self._doors = {}
        self._caller_history = {}
    
    def register_door(self, name: str, source: str, target: str, 
                     access_level: AccessLevel = AccessLevel.PRIVATE,
                     allowed_types: Optional[List[WallSection]] = None):
        """Register a new door between rooms"""
        self._doors[name] = {
            'source': source,
            'target': target,
            'access_level': access_level,
            'allowed_types': allowed_types or []
        }
    
    def request_access(self, door_name: str, caller: str, args: List[Any], 
                      caller_access: AccessLevel = AccessLevel.PUBLIC) -> bool:
        """Request access through a door"""
        if door_name not in self._doors:
            return False
            
        door = self._doors[door_name]
        if caller != door['source']:
            return False
            
        # Check access level
        if (caller_access == AccessLevel.PUBLIC and door['access_level'] != AccessLevel.PUBLIC or
            caller_access == AccessLevel.PROTECTED and door['access_level'] == AccessLevel.PRIVATE):
            return False
            
        # Record access attempt
        self._caller_history.setdefault(door_name, []).append({
            'caller': caller,
            'timestamp': datetime.now().isoformat(),
            'args': [str(arg) for arg in args],
            'granted': True
        })
        
        return True

class LightManager:
    """Manages output and logging"""
    
    def __init__(self):
        self._lights = {}
        self.logger = logging.getLogger('cpj.lights')
        self._setup_logger()
    
    def _setup_logger(self):
        """Set up logging configuration"""
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def register_light(self, name: str, level: str = 'info', format: str = '{message}'):
        """Register a new light for output"""
        self._lights[name] = {
            'level': level,
            'format': format,
            'history': []
        }
    
    def emit(self, light_name: str, message: str, **kwargs):
        """Emit a message through a light"""
        if light_name not in self._lights:
            return
            
        light = self._lights[light_name]
        formatted = light['format'].format(message=message, **kwargs)
        
        # Log using appropriate level
        level = light['level'].lower()
        if level == 'debug':
            self.logger.debug(formatted)
        elif level == 'warning':
            self.logger.warning(formatted)
        elif level == 'error':
            self.logger.error(formatted)
        else:
            self.logger.info(formatted)
            
        # Record message
        light['history'].append({
            'message': formatted,
            'timestamp': datetime.now().isoformat()
        })