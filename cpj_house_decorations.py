"""CPJ House Decoration System

Provides decorative features for the CPJ house metaphor, including:
- Theme management
- Decoration types and styles
- Event handling for decoration changes
- Import/export capabilities
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar, Union
import json

# Type hints
T = TypeVar('T')
DecorationEventHandler = Callable[['DecorationEvent'], None]

# --- Decoration Events ---

class DecorationEventType(Enum):
    """Types of decoration events that can be emitted."""
    THEME_CHANGED = auto()
    DECORATION_APPLIED = auto()

class DecorationEvent:
    def __init__(self, event_type: DecorationEventType, payload: Any = None):
        self.event_type = event_type
        self.payload = payload

class DecorationEventManager:
    """Manages decoration-related events and listeners."""
    def __init__(self):
        self._listeners: Dict[DecorationEventType, List[Callable[[DecorationEvent], None]]] = {}

    def subscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]) -> None:
        """Subscribe to a decoration event."""
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def unsubscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]) -> None:
        """Unsubscribe from a decoration event."""
        if event_type in self._listeners and callback in self._listeners[event_type]:
            self._listeners[event_type].remove(callback)

    def emit(self, event: DecorationEvent) -> None:
        """Emit a decoration event to all subscribers."""
        for callback in self._listeners.get(event.event_type, []):
            try:
                callback(event)
            except Exception as e:
                print(f'Warning: Event handler failed: {e}')

    def clear(self) -> None:
        """Remove all event listeners."""
        self._listeners.clear()

# --- Decoration Types ---

class DecorationKind(str, Enum):
    """Types of decorations that can be applied."""
    COLOR = 'COLOR'
    STYLE = 'STYLE'
    PATTERN = 'PATTERN'
    ANIMATION = 'ANIMATION'
    INDICATOR = 'INDICATOR'

class DecorationTarget(str, Enum):
    """Features that can be decorated."""
    WINDOW = 'WINDOW'  # The window feature's decorations
    DOOR = 'DOOR'      # The door feature's decorations
    WALL = 'WALL'      # Wall decorations
    ROOF = 'ROOF'      # Roof decorations
    FLOOR = 'FLOOR'    # Floor decorations
    ROOM = 'ROOM'      # Room-level decorations
    HOUSE = 'HOUSE'    # House-level decorations
    LIGHT = 'LIGHT'    # Light feature's decorations

@dataclass
class DecorationStyle:
    """Style configuration for decorations"""
    font_family: str = "monospace"
    font_size: int = 12
    bold: bool = False
    italic: bool = False
    underline: bool = False
    strikethrough: bool = False

@dataclass
class ColorScheme:
    """Color configuration for syntax and visual elements"""
    background: str = "#FFFFFF"
    foreground: str = "#000000"
    accent: str = "#4A90E2"
    error: str = "#FF0000"
    warning: str = "#FFA500"
    success: str = "#00FF00"
    info: str = "#0000FF"
    syntax_colors: Dict[str, str] = field(default_factory=lambda: {
        "keyword": "#0000FF",
        "string": "#008000",
        "number": "#FF0000",
        "comment": "#808080",
        "type": "#800080",
        "function": "#000080",
        "variable": "#000000"
    })

@dataclass
class Decoration:
    """Individual decoration instance"""
    kind: DecorationKind
    target: DecorationTarget
    style: Optional[DecorationStyle] = None
    color: Optional[str] = None
    pattern: Optional[str] = None
    animation: Optional[Dict[str, Any]] = None
    priority: int = 0
    enabled: bool = True

    def as_dict(self) -> Dict[str, Any]:
        """Convert decoration to dictionary representation."""
        return {
            'kind': self.kind.value,
            'target': self.target.value,
            'style': vars(self.style) if self.style else None,
            'color': self.color,
            'pattern': self.pattern,
            'animation': self.animation,
            'priority': self.priority,
            'enabled': self.enabled
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Decoration':
        """Create a decoration from a dictionary representation."""
        try:
            kind = DecorationKind(str(data['kind']))
            target = DecorationTarget(str(data['target']))
            style_data = data.get('style')
            style = DecorationStyle(**style_data) if style_data else None
            
            return cls(
                kind=kind,
                target=target,
                style=style,
                color=data.get('color'),
                pattern=data.get('pattern'),
                animation=data.get('animation'),
                priority=data.get('priority', 0),
                enabled=data.get('enabled', True)
            )
        except (KeyError, ValueError) as e:
            raise ValueError(f'Invalid decoration data: {e}')

@dataclass
class Theme:
    """Represents a collection of decorations that can be applied together."""
    name: str
    decorations: List[Decoration] = field(default_factory=list)
    _listeners: Dict[int, List[Callable[[DecorationEvent], None]]] = field(default_factory=dict)

    def add_decoration(self, decoration: Decoration) -> None:
        """Add a decoration to the theme."""
        self.decorations.append(decoration)

    def remove_decoration(self, decoration: Decoration) -> None:
        """Remove a decoration from the theme."""
        if decoration in self.decorations:
            self.decorations.remove(decoration)

    def get_decorations_for_target(self, target: DecorationTarget) -> List[Decoration]:
        """Get all decorations for a specific target."""
        return [d for d in self.decorations if d.target == target]

    def as_dict(self) -> Dict[str, Any]:
        """Convert theme to dictionary representation."""
        return {
            'name': self.name,
            'decorations': [d.as_dict() for d in self.decorations]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Theme':
        """Create theme from dictionary representation."""
        if not isinstance(data, dict):
            raise ValueError('Data must be a dictionary')
        if 'name' not in data:
            raise ValueError('Theme data must include a name')

        theme = cls(name=data['name'])
        for d in data.get('decorations', []):
            try:
                theme.decorations.append(Decoration.from_dict(d))
            except (KeyError, ValueError, AttributeError) as e:
                print(f'Warning: Skipping invalid decoration: {e}')
        return theme

    def subscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]) -> None:
        """Subscribe to theme events."""
        if event_type.value not in self._listeners:
            self._listeners[event_type.value] = []
        self._listeners[event_type.value].append(callback)

    def unsubscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]) -> None:
        """Unsubscribe from theme events."""
        if event_type.value in self._listeners and callback in self._listeners[event_type.value]:
            self._listeners[event_type.value].remove(callback)

    def emit(self, event: DecorationEvent) -> None:
        """Emit a theme event."""
        for callback in self._listeners.get(event.event_type.value, []):
            callback(event)

class ThemeManager:
    """Manages themes and their application to house elements."""
    
    def __init__(self):
        self.themes: Dict[str, Theme] = {}
        self.active_theme: Optional[Theme] = None
        self.event_manager = DecorationEventManager()

    def add_theme(self, theme: Theme) -> None:
        """Add a theme to the manager."""
        self.themes[theme.name] = theme
        if not self.active_theme:
            self.active_theme = theme
            self.event_manager.emit(DecorationEvent(DecorationEventType.THEME_CHANGED, theme))

    def set_active_theme(self, name: str) -> None:
        """Set the active theme."""
        if name in self.themes:
            self.active_theme = self.themes[name]
            self.event_manager.emit(DecorationEvent(DecorationEventType.THEME_CHANGED, self.active_theme))

    def get_active_theme(self) -> Optional[Theme]:
        """Get the currently active theme."""
        return self.active_theme

    def export_theme(self, name: str, path: Path) -> None:
        """Export a theme to a JSON file."""
        if name not in self.themes:
            raise ValueError(f'Theme {name} does not exist')
            
        try:
            with open(path, 'w') as f:
                json.dump(self.themes[name].as_dict(), f, indent=2)
        except IOError as e:
            raise IOError(f'Failed to export theme: {e}')

    def import_theme(self, path: Path) -> None:
        """Import a theme from a JSON file."""
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                theme = Theme.from_dict(data)
                self.add_theme(theme)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f'Failed to import theme: {e}')

    def list_themes(self) -> List[str]:
        """Get a list of all theme names."""
        return list(self.themes.keys())
        
    def get_theme(self, name: str) -> Optional[Theme]:
        """Get a specific theme by name."""
        return self.themes.get(name)

    def apply_theme(self, target: Union[DecorationTarget, str]) -> List[Decoration]:
        """Return decorations for a given target, sorted by priority."""
        if not self.active_theme:
            return []
            
        try:
            # Convert target to DecorationTarget if string
            if isinstance(target, str):
                try:
                    target = DecorationTarget(target.upper())
                except ValueError:
                    raise ValueError(f'Invalid target: {target}')
            elif not isinstance(target, DecorationTarget):
                raise TypeError('Target must be a string or DecorationTarget')
            
            # Get decorations for target and sort by priority
            decorations = sorted(
                [d for d in self.active_theme.decorations if d.target == target and d.enabled],
                key=lambda d: d.priority,
                reverse=True
            )
            
            # Emit event for applied decorations
            self.event_manager.emit(DecorationEvent(DecorationEventType.DECORATION_APPLIED, decorations))
            return decorations
            
        except Exception as e:
            print(f'Warning: Failed to apply theme to target {target}: {e}')
            return []
