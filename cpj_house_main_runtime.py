"""Main runtime class for the house architecture."""

from typing import Optional, Dict, Any, List, Set, Awaitable, Callable, Tuple
from cpj_enums import AccessLevel
from cpj_type_system import TypeSystem
from cpj_house_storage_runtime import StorageManager
from cpj_house_knowledge_runtime import KnowledgeManager
from cpj_house_rest_runtime import RestManager
from cpj_house_utility_runtime import UtilityManager
from cpj_house_security_runtime import SecurityManager
from cpj_house_decoration_runtime import DecorationRuntime
from cpj_house_ai_runtime import HouseAISystem
from cpj_house_runtime import WindowManager, DoorManager, LightManager

class HouseRuntime:
    """Coordinates all house feature managers and provides central runtime support."""
    
    def __init__(self, type_system: Optional[TypeSystem] = None):
        """Initialize house runtime with managers for all features."""
        # Initialize type system if not provided
        self.type_system = type_system or TypeSystem()
        
        # Initialize feature managers
        self.windows = WindowManager()
        self.doors = DoorManager()
        self.lights = LightManager()
        self.storage = StorageManager(self.type_system)
        self.knowledge = KnowledgeManager(self.type_system)
        self.rest = RestManager(self.type_system)
        self.utility = UtilityManager(self.type_system)
        self.security = SecurityManager(self.type_system)
        self.decorations = DecorationRuntime(self.type_system)
        self.ai = HouseAISystem(self)
        
    def get_feature_managers(self) -> Dict[str, Any]:
        """Get all active feature managers."""
        return {
            'windows': self.windows,
            'doors': self.doors,
            'lights': self.lights,
            'storage': self.storage,
            'knowledge': self.knowledge,
            'rest': self.rest,
            'utility': self.utility,
            'security': self.security,
            'decorations': self.decorations,
            'ai': self.ai
        }
        
    def setup_basic_features(self):
        """Set up basic house features with default configurations."""
        # Set up standard lights
        self.lights.register_light('info', level='info')
        self.lights.register_light('debug', level='debug')
        self.lights.register_light('warning', level='warning')
        self.lights.register_light('error', level='error')
        
        # Create standard storage features
        self.storage.create_cupboard('global_scope', policy=None)  # For module-level storage
        self.storage.create_bin('temp_vars', policy=None)  # For temporary variables
        self.storage.create_drawer('config', policy=None)  # For configuration storage
        
        # Create standard knowledge features
        self.knowledge.create_library('main')  # Main documentation library
        self.knowledge.create_catalog('index')  # Documentation index
        self.knowledge.create_reference('api')  # API reference documentation
        
        # Create standard rest features
        self.rest.create_bed('main_suspend')  # Main process suspension
        self.rest.create_chair('async_ops')   # Async operations
        self.rest.create_bench('workers')     # Parallel processing
        
        # Create standard utility features
        self.utility.create_table('main_workspace')  # Main workspace organization
        self.utility.create_desk('main_context')    # Main context management
        self.utility.create_workbench('tools')      # Tool management
        self.utility.create_cabinet('resources')    # Resource management
        
        # Create standard security features
        self.security.create_alarm('error_handler')  # Error handling system
        self.security.create_camera('system_monitor')  # System monitoring
        self.security.create_sensor('event_detector')  # Event detection
        self.security.create_guard('policy_enforcer')  # Policy enforcement
        
        # Create standard decoration features
        self.decorations.create_style('code_style',
            font_family='Consolas',
            font_size=14,
            bold=False
        )
        self.decorations.create_style('header_style',
            font_family='Arial',
            font_size=16,
            bold=True
        )
        self.decorations.create_color_scheme('modern',
            background="#282C34",
            foreground="#ABB2BF",
            accent="#61AFEF",
            error="#E06C75",
            warning="#E5C07B",
            success="#98C379"
        )
        
    def emit(self, message: str, level: str = 'info', **kwargs):
        """Emit a message through the appropriate light."""
        self.lights.emit(level, message, **kwargs)
        
    def inspect(self, target: str, caller_access: AccessLevel = AccessLevel.PUBLIC) -> Optional[Dict[str, Any]]:
        """Inspect a value through a window."""
        return self.windows.inspect(target, caller_access)
        
    def access(self, door: str, caller: str, args: list, caller_access: AccessLevel = AccessLevel.PUBLIC) -> bool:
        """Request access through a door."""
        return self.doors.request_access(door, caller, args, caller_access)
        
    def store(self, storage: str, key: str, value: Any, type_hint: Optional[str] = None) -> bool:
        """Store a value in the specified storage feature."""
        storage_feature = self.storage.get_storage(storage)
        if storage_feature:
            return storage_feature.store(key, value, type_hint)
        return False
        
    def retrieve(self, storage: str, key: str) -> Optional[Any]:
        """Retrieve a value from the specified storage feature."""
        storage_feature = self.storage.get_storage(storage)
        if storage_feature:
            return storage_feature.retrieve(key)
        return None