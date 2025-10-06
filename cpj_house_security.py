"""CPJ House Security Features
Provides security features like locks and alarms for access control and error handling.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Callable
from enum import Enum, auto
from cpj_type_system import TypeSystem, TypeKind, WallSection
from cpj_parser2 import Node, NodeType
from cpj_enums import AccessLevel
import traceback
from datetime import datetime

class SecurityKind(Enum):
    """Types of security features"""
    LOCK = auto()        # Access control
    ALARM = auto()       # Error handling
    CAMERA = auto()      # Monitoring
    SENSOR = auto()      # Event detection
    GUARD = auto()       # Policy enforcement

class SecurityLevel(Enum):
    """Security clearance levels"""
    PUBLIC = auto()      # Anyone can access
    RESTRICTED = auto()  # Limited access
    CONFIDENTIAL = auto()# Need to know
    SECRET = auto()      # High security
    TOP_SECRET = auto()  # Maximum security

@dataclass
class SecurityEvent:
    """Security-related event information"""
    event_type: str
    timestamp: float
    source: str
    level: SecurityLevel
    details: Dict[str, Any]
    stack_trace: Optional[str] = None

@dataclass
class SecurityPolicy:
    """Security policy configuration"""
    required_level: SecurityLevel
    allowed_sources: Set[str]
    allowed_types: Set[str]
    custom_checks: List[Callable[[Any], bool]] = field(default_factory=list)
    max_attempts: int = 3
    timeout: Optional[float] = None
    audit_log: bool = True

@dataclass
class Lock(Node):
    """Access control mechanism"""
    name: str = field(default="")
    kind: SecurityKind = field(default=SecurityKind.LOCK)
    policy: SecurityPolicy = field(default_factory=lambda: SecurityPolicy(
        SecurityLevel.PUBLIC, set(), set()
    ))
    _locked: bool = field(default=True)
    _access_log: List[SecurityEvent] = field(default_factory=list)
    _failed_attempts: Dict[str, int] = field(default_factory=dict)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.SECURITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        self.policy = kwargs.get('policy', SecurityPolicy(
            SecurityLevel.PUBLIC, set(), set()
        ))
        
    def request_access(self, source: str, level: SecurityLevel,
                      context: Optional[Dict[str, Any]] = None) -> bool:
        """Request access through the lock"""
        event = SecurityEvent(
            event_type="access_request",
            timestamp=datetime.now().timestamp(),
            source=source,
            level=level,
            details=context or {}
        )
        
        # Check failed attempts
        if (self.policy.max_attempts and 
            self._failed_attempts.get(source, 0) >= self.policy.max_attempts):
            event.details['reason'] = "max_attempts_exceeded"
            self._log_event(event)
            return False
            
        # Check security level
        if level.value < self.policy.required_level.value:
            self._record_failure(source)
            event.details['reason'] = "insufficient_clearance"
            self._log_event(event)
            return False
            
        # Check source
        if self.policy.allowed_sources and source not in self.policy.allowed_sources:
            self._record_failure(source)
            event.details['reason'] = "unauthorized_source"
            self._log_event(event)
            return False
            
        # Run custom checks
        if context and self.policy.custom_checks:
            for check in self.policy.custom_checks:
                if not check(context):
                    self._record_failure(source)
                    event.details['reason'] = "failed_custom_check"
                    self._log_event(event)
                    return False
                    
        # Grant access
        event.details['status'] = "granted"
        self._log_event(event)
        return True
        
    def _record_failure(self, source: str):
        """Record a failed access attempt"""
        self._failed_attempts[source] = self._failed_attempts.get(source, 0) + 1
        
    def _log_event(self, event: SecurityEvent):
        """Log a security event"""
        if self.policy.audit_log:
            self._access_log.append(event)
            
    def reset_attempts(self, source: str):
        """Reset failed attempts counter"""
        self._failed_attempts.pop(source, None)
        
    def get_access_log(self) -> List[SecurityEvent]:
        """Get the access log"""
        return self._access_log.copy()

@dataclass
class Alarm(Node):
    """Error handling and notification"""
    name: str = field(default="")
    kind: SecurityKind = field(default=SecurityKind.ALARM)
    _handlers: Dict[str, List[Callable[[SecurityEvent], None]]] = field(default_factory=dict)
    _events: List[SecurityEvent] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.SECURITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def register_handler(self, event_type: str, handler: Callable[[SecurityEvent], None]):
        """Register an event handler"""
        self._handlers.setdefault(event_type, []).append(handler)
        
    def trigger(self, event_type: str, source: str,
                level: SecurityLevel = SecurityLevel.PUBLIC,
                details: Optional[Dict[str, Any]] = None):
        """Trigger the alarm"""
        event = SecurityEvent(
            event_type=event_type,
            timestamp=datetime.now().timestamp(),
            source=source,
            level=level,
            details=details or {},
            stack_trace=traceback.format_stack()
        )
        self._events.append(event)
        
        # Execute handlers
        for handler in self._handlers.get(event_type, []):
            try:
                handler(event)
            except Exception as e:
                print(f"Handler error: {e}")
                
    def get_events(self, event_type: Optional[str] = None) -> List[SecurityEvent]:
        """Get recorded events"""
        if event_type:
            return [e for e in self._events if e.event_type == event_type]
        return self._events.copy()

@dataclass
class Camera(Node):
    """System monitoring"""
    name: str = field(default="")
    kind: SecurityKind = field(default=SecurityKind.CAMERA)
    _watchers: Dict[str, List[Callable[[Dict[str, Any]], None]]] = field(default_factory=dict)
    _snapshots: List[Dict[str, Any]] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.SECURITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def watch(self, target: str, callback: Callable[[Dict[str, Any]], None]):
        """Start watching a target"""
        self._watchers.setdefault(target, []).append(callback)
        
    def snapshot(self, target: str, data: Dict[str, Any]):
        """Take a snapshot of target state"""
        snapshot = {
            'target': target,
            'timestamp': datetime.now().timestamp(),
            'data': data
        }
        self._snapshots.append(snapshot)
        
        # Notify watchers
        for watcher in self._watchers.get(target, []):
            try:
                watcher(data)
            except Exception as e:
                print(f"Watcher error: {e}")
                
    def get_snapshots(self, target: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get recorded snapshots"""
        if target:
            return [s for s in self._snapshots if s['target'] == target]
        return self._snapshots.copy()

@dataclass
class Sensor(Node):
    """Event detection"""
    name: str = field(default="")
    kind: SecurityKind = field(default=SecurityKind.SENSOR)
    _triggers: Dict[str, List[Callable[[Dict[str, Any]], bool]]] = field(default_factory=dict)
    _callbacks: Dict[str, List[Callable[[Dict[str, Any]], None]]] = field(default_factory=dict)
    _history: List[Dict[str, Any]] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.SECURITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_trigger(self, event_type: str, condition: Callable[[Dict[str, Any]], bool]):
        """Add an event trigger condition"""
        self._triggers.setdefault(event_type, []).append(condition)
        
    def add_callback(self, event_type: str, callback: Callable[[Dict[str, Any]], None]):
        """Add an event callback"""
        self._callbacks.setdefault(event_type, []).append(callback)
        
    def check(self, event_type: str, data: Dict[str, Any]) -> bool:
        """Check if event conditions are met"""
        triggers = self._triggers.get(event_type, [])
        if not triggers:
            return False
            
        # Check all triggers
        triggered = any(trigger(data) for trigger in triggers)
        if triggered:
            self._record_event(event_type, data)
            # Execute callbacks
            for callback in self._callbacks.get(event_type, []):
                try:
                    callback(data)
                except Exception as e:
                    print(f"Callback error: {e}")
                    
        return triggered
        
    def _record_event(self, event_type: str, data: Dict[str, Any]):
        """Record a triggered event"""
        event = {
            'type': event_type,
            'timestamp': datetime.now().timestamp(),
            'data': data
        }
        self._history.append(event)
        
    def get_history(self, event_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get event history"""
        if event_type:
            return [e for e in self._history if e['type'] == event_type]
        return self._history.copy()

@dataclass
class Guard(Node):
    """Policy enforcement"""
    name: str = field(default="")
    kind: SecurityKind = field(default=SecurityKind.GUARD)
    _policies: Dict[str, List[Callable[[Any], bool]]] = field(default_factory=dict)
    _violations: List[Dict[str, Any]] = field(default_factory=list)
    _type_system: Optional[TypeSystem] = field(default=None, init=False)
    
    def __init__(self, type_system: TypeSystem, **kwargs):
        super().__init__(node_type=NodeType.SECURITY, **kwargs)
        self._type_system = type_system
        self.name = kwargs.get('name', '')
        
    def add_policy(self, name: str, check: Callable[[Any], bool]):
        """Add a policy check"""
        self._policies.setdefault(name, []).append(check)
        
    def enforce(self, policy_name: str, data: Any) -> bool:
        """Enforce a policy"""
        if policy_name not in self._policies:
            return True
            
        violations = []
        for check in self._policies[policy_name]:
            try:
                if not check(data):
                    violations.append({
                        'policy': policy_name,
                        'timestamp': datetime.now().timestamp(),
                        'data': data
                    })
            except Exception as e:
                violations.append({
                    'policy': policy_name,
                    'timestamp': datetime.now().timestamp(),
                    'data': data,
                    'error': str(e)
                })
                
        if violations:
            self._violations.extend(violations)
            return False
        return True
        
    def get_violations(self, policy_name: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get policy violations"""
        if policy_name:
            return [v for v in self._violations if v['policy'] == policy_name]
        return self._violations.copy()