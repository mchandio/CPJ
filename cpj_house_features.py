from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union, Set, cast, Literal, TypeAlias
from cpj_type_system import WallSection, TypeSystem, TypeKind
from cpj_parser2 import Node, NodeType as NodeType2
from cpj_enums import NodeType
from enum import Enum, auto
from cpj_house_decorations import (
    Decoration, DecorationTarget as DecorTarget, DecorationEventType,
    DecorationEvent, ThemeManager
)
from collections.abc import Iterable

# Create our own wrapped types to handle type compatibility
DecorationTarget: TypeAlias = DecorTarget

FeatureTarget = Literal['WINDOW', 'DOOR', 'LIGHT']

# Helper functions to convert types
def _target(s: str) -> str:
    """Convert target name to string for theme manager"""
    # Strings work in apply_theme since it handles them internally
    return s

def _cast_node_type(s: str) -> NodeType2:
    """Convert string to parser NodeType"""
    return cast(NodeType2, NodeType[s])

class AccessLevel(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()

@dataclass
class Window(Node):
    """A window allows inspection of internal state"""
    target: str = field(default="")  # What we're inspecting (variable, state, etc.)
    access_level: AccessLevel = field(default=AccessLevel.PUBLIC)
    decorations: Set[Decoration] = field(default_factory=set)
    _theme_manager: Optional[ThemeManager] = field(default=None, init=False)
    
    def apply_decorations(self, theme_manager: ThemeManager) -> None:
        """Apply decorations from theme manager"""
        self._theme_manager = theme_manager
        decorations = theme_manager.apply_theme('WINDOW')  # Use string directly, handled by ThemeManager
        self.decorations.clear()
        for d in decorations:
            self.decorations.add(cast(Decoration, d))
        
    def _on_theme_changed(self, event: DecorationEvent) -> None:
        """Handle theme change events"""
        if self._theme_manager:
            decorations = self._theme_manager.apply_theme('WINDOW')
            self.decorations.clear()
            for d in decorations:
                self.decorations.add(cast(Decoration, d))
    
    def __init__(self, **kwargs):
        super().__init__(node_type=_cast_node_type('WINDOW'), **kwargs)
        self.target = kwargs.get('target', "")
        self.access_level = kwargs.get('access_level', AccessLevel.PUBLIC)
    
    def inspect(self) -> Dict[str, Any]:
        """Get the current state/value of what we're inspecting"""
        # Implementation will be in runtime
        return {}

@dataclass 
class Door(Node):
    """A door controls access between rooms/functions"""
    source_room: str = field(default="")
    target_room: str = field(default="")
    access_level: AccessLevel = field(default=AccessLevel.PRIVATE)
    allowed_types: List[WallSection] = field(default_factory=list)
    decorations: Set[Decoration] = field(default_factory=set)
    _theme_manager: Optional[ThemeManager] = field(default=None, init=False)
    
    def apply_decorations(self, theme_manager: ThemeManager) -> None:
        """Apply decorations from theme manager"""
        self._theme_manager = theme_manager
        decorations = theme_manager.apply_theme('DOOR')
        self.decorations.clear()
        for d in decorations:
            self.decorations.add(cast(Decoration, d))
        
    def _on_theme_changed(self, event: DecorationEvent) -> None:
        """Handle theme change events"""
        if self._theme_manager:
            decorations = self._theme_manager.apply_theme('DOOR')
            self.decorations.clear()
            for d in decorations:
                self.decorations.add(cast(Decoration, d))
    
    def __init__(self, **kwargs):
        super().__init__(node_type=_cast_node_type('DOOR'), **kwargs)
        self.source_room = kwargs.get('source_room', "")
        self.target_room = kwargs.get('target_room', "")
        self.access_level = kwargs.get('access_level', AccessLevel.PRIVATE)
        self.allowed_types = kwargs.get('allowed_types', [])
    
    def check_access(self, caller: str, args: List[Any]) -> bool:
        """Check if access is allowed through this door"""
        # Implementation will be in runtime
        return True

@dataclass
class Light(Node):
    """A light handles output and logging"""
    level: str = field(default="info")  # info, warning, error, debug
    format: str = field(default="{message}")
    decorations: Set[Decoration] = field(default_factory=set)
    _theme_manager: Optional[ThemeManager] = field(default=None, init=False)
    
    def apply_decorations(self, theme_manager: ThemeManager) -> None:
        """Apply decorations from theme manager"""
        self._theme_manager = theme_manager
        decorations = theme_manager.apply_theme('LIGHT')
        self.decorations.clear()
        for d in decorations:
            self.decorations.add(cast(Decoration, d))
        
    def _on_theme_changed(self, event: DecorationEvent) -> None:
        """Handle theme change events"""
        if self._theme_manager:
            decorations = self._theme_manager.apply_theme('LIGHT')
            self.decorations.clear()
            for d in decorations:
                self.decorations.add(cast(Decoration, d))
    
    def __init__(self, **kwargs):
        super().__init__(node_type=_cast_node_type('LIGHT'), **kwargs)
        self.level = kwargs.get('level', "info")
        self.format = kwargs.get('format', "{message}")
    
    def emit(self, message: str, **kwargs) -> None:
        """Emit a message with the configured format and level"""
        # Implementation will be in runtime
        pass

class HouseFeatureDecorator:
    """Manages decorations for all house features"""
    def __init__(self):
        self.theme_manager = ThemeManager()
        self.features: List[Union[Window, Door, Light]] = []
        
        # Set up event listeners
        self.theme_manager.event_manager.subscribe(
            DecorationEventType.THEME_CHANGED,
            self._on_theme_changed
        )
    
    def register_feature(self, feature: Union[Window, Door, Light]) -> None:
        """Register a feature for decoration management"""
        self.features.append(feature)
        feature.apply_decorations(self.theme_manager)
    
    def _on_theme_changed(self, event: DecorationEvent) -> None:
        """Propagate theme changes to all registered features"""
        for feature in self.features:
            feature._on_theme_changed(event)
    
    def apply_theme_to_all(self, theme_name: str) -> None:
        """Apply a theme to all registered features"""
        self.theme_manager.set_active_theme(theme_name)