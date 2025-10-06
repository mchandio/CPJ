"""Runtime management for security features."""

from typing import Dict, Any, Optional, List, Callable, Set
from cpj_type_system import TypeSystem
from cpj_house_security import (
    Lock, Alarm, Camera, Sensor, Guard,
    SecurityKind, SecurityLevel, SecurityPolicy,
    SecurityEvent
)

class SecurityManager:
    """Manages security features in the house"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._locks = {}
        self._alarms = {}
        self._cameras = {}
        self._sensors = {}
        self._guards = {}
        
    def create_lock(self, name: str, policy: Optional[SecurityPolicy] = None) -> Lock:
        """Create a new lock for access control"""
        lock = Lock(
            type_system=self._type_system,
            name=name,
            policy=policy or SecurityPolicy(
                SecurityLevel.PUBLIC,
                set(),
                set()
            )
        )
        self._locks[name] = lock
        return lock
        
    def create_alarm(self, name: str) -> Alarm:
        """Create a new alarm for error handling"""
        alarm = Alarm(
            type_system=self._type_system,
            name=name
        )
        self._alarms[name] = alarm
        return alarm
        
    def create_camera(self, name: str) -> Camera:
        """Create a new camera for monitoring"""
        camera = Camera(
            type_system=self._type_system,
            name=name
        )
        self._cameras[name] = camera
        return camera
        
    def create_sensor(self, name: str) -> Sensor:
        """Create a new sensor for event detection"""
        sensor = Sensor(
            type_system=self._type_system,
            name=name
        )
        self._sensors[name] = sensor
        return sensor
        
    def create_guard(self, name: str) -> Guard:
        """Create a new guard for policy enforcement"""
        guard = Guard(
            type_system=self._type_system,
            name=name
        )
        self._guards[name] = guard
        return guard
        
    def get_lock(self, name: str) -> Optional[Lock]:
        """Get a lock by name"""
        return self._locks.get(name)
        
    def get_alarm(self, name: str) -> Optional[Alarm]:
        """Get an alarm by name"""
        return self._alarms.get(name)
        
    def get_camera(self, name: str) -> Optional[Camera]:
        """Get a camera by name"""
        return self._cameras.get(name)
        
    def get_sensor(self, name: str) -> Optional[Sensor]:
        """Get a sensor by name"""
        return self._sensors.get(name)
        
    def get_guard(self, name: str) -> Optional[Guard]:
        """Get a guard by name"""
        return self._guards.get(name)
        
    def list_security_features(self) -> Dict[str, List[str]]:
        """List all security features by type"""
        return {
            'locks': list(self._locks.keys()),
            'alarms': list(self._alarms.keys()),
            'cameras': list(self._cameras.keys()),
            'sensors': list(self._sensors.keys()),
            'guards': list(self._guards.keys())
        }
        
    def create_security_policy(self,
                             level: SecurityLevel = SecurityLevel.PUBLIC,
                             allowed_sources: Optional[Set[str]] = None,
                             allowed_types: Optional[Set[str]] = None,
                             custom_checks: Optional[List[Callable[[Any], bool]]] = None,
                             max_attempts: int = 3,
                             timeout: Optional[float] = None,
                             audit_log: bool = True) -> SecurityPolicy:
        """Create a new security policy"""
        return SecurityPolicy(
            required_level=level,
            allowed_sources=allowed_sources or set(),
            allowed_types=allowed_types or set(),
            custom_checks=custom_checks or [],
            max_attempts=max_attempts,
            timeout=timeout,
            audit_log=audit_log
        )
        
    def trigger_alarm(self, alarm_name: str, event_type: str, source: str,
                     level: SecurityLevel = SecurityLevel.PUBLIC,
                     details: Optional[Dict[str, Any]] = None):
        """Trigger an alarm"""
        alarm = self.get_alarm(alarm_name)
        if alarm:
            alarm.trigger(event_type, source, level, details)
            
    def check_access(self, lock_name: str, source: str,
                    level: SecurityLevel = SecurityLevel.PUBLIC,
                    context: Optional[Dict[str, Any]] = None) -> bool:
        """Check access through a lock"""
        lock = self.get_lock(lock_name)
        if lock:
            return lock.request_access(source, level, context)
        return False
        
    def enforce_policy(self, guard_name: str, policy_name: str,
                      data: Any) -> bool:
        """Enforce a policy using a guard"""
        guard = self.get_guard(guard_name)
        if guard:
            return guard.enforce(policy_name, data)
        return True