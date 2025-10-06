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

from __future__ import annotations

# --- Decoration Events ---
from enum import Enum, auto
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

# Forward declarations for type hints
T = TypeVar('T')
DecorationEventHandler = Callable[['DecorationEvent'], None]

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

    def subscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def unsubscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]):
        if event_type in self._listeners:
            self._listeners[event_type].remove(callback)

    def emit(self, event: DecorationEvent):
        for callback in self._listeners.get(event.event_type, []):
            callback(event)

# Integrate event manager with ThemeManager
class ThemeManager:
    def __init__(self):
        self.themes: Dict[str, Theme] = {}
        self.active_theme: Optional[Theme] = None
        self.event_manager = DecorationEventManager()

    def add_theme(self, theme: Theme):
        self.themes[theme.name] = theme
        if not self.active_theme:
            self.active_theme = theme
            self.event_manager.emit(DecorationEvent(DecorationEventType.THEME_CHANGED, theme))

    def set_active_theme(self, name: str):
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
                    target = getattr(DecorationTarget, target.upper())
                except AttributeError:
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

class DecorationStyle(str, Enum):
    """Visual styles that can be applied."""
    BOLD = 'BOLD'
    ITALIC = 'ITALIC'
    UNDERLINE = 'UNDERLINE'
    STRIKETHROUGH = 'STRIKETHROUGH'
    NORMAL = 'NORMAL'

@dataclass
class Decoration:
    """A single decoration that can be applied to a target."""
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
            'kind': self.kind.name,  # Using name instead of value for enum compatibility
            'target': self.target.name,
            'style': self.style.name if self.style else None,
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
            kind = DecorationKind[str(data['kind'])]
            target = DecorationTarget[str(data['target'])]
            style = DecorationStyle[str(data['style'])] if data.get('style') else None
            
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
        )

@dataclass
class Theme:
    """Represents a collection of decorations that can be applied together."""
    name: str
    decorations: List[Decoration] = field(default_factory=list)

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

        decorations = []
        for d in data.get('decorations', []):
            try:
                decorations.append(Decoration.from_dict(d))
            except (KeyError, ValueError, AttributeError) as e:
                print(f'Warning: Skipping invalid decoration: {e}')

        return cls(
            name=data['name'],
            decorations=decorations
        )



    def subscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]):
        key = event_type.value
        if key not in self._listeners:
            self._listeners[key] = []
        self._listeners[key].append(callback)

    def unsubscribe(self, event_type: DecorationEventType, callback: Callable[[DecorationEvent], None]):
        key = event_type.value
        if key in self._listeners:
            self._listeners[key].remove(callback)

    def emit(self, event: DecorationEvent):
        key = event.event_type.value
        for callback in self._listeners.get(key, []):
            callback(event)

# --- Theme Manager with Event Integration ---
class ThemeManager:
    def __init__(self):
        self.themes: Dict[str, Theme] = {}
        self.active_theme: Optional[Theme] = None
        self.event_manager = DecorationEventManager()

    def add_theme(self, theme: Theme):
        self.themes[theme.name] = theme
        if not self.active_theme:
            self.active_theme = theme
            self.event_manager.emit(DecorationEvent(DecorationEventType.THEME_CHANGED, theme))

    def set_active_theme(self, name: str):
        if name in self.themes:
            self.active_theme = self.themes[name]
            self.event_manager.emit(DecorationEvent(DecorationEventType.THEME_CHANGED, self.active_theme))

    def get_active_theme(self) -> Optional[Theme]:
        return self.active_theme

    def export_theme(self, name: str, path: Path):
        if name in self.themes:
            with open(path, 'w') as f:
                json.dump(self.themes[name].as_dict(), f, indent=2)

    def import_theme(self, path: Path):
        with open(path, 'r') as f:
            data = json.load(f)
            theme = Theme.from_dict(data)
            self.add_theme(theme)

    def list_themes(self) -> List[str]:
        return list(self.themes.keys())

    def apply_theme(self, target: DecorationTarget) -> List[Decoration]:
        """Return decorations for a given target, sorted by priority"""
        if not self.active_theme:
            return []
        decorations = sorted(
            [d for d in self.active_theme.decorations if d.target == target],
            key=lambda d: d.priority,
            reverse=True
        )
        self.event_manager.emit(DecorationEvent(DecorationEventType.DECORATION_APPLIED, decorations))
        return decorations

# Example usage:
# theme_mgr = ThemeManager()
# theme_mgr.add_theme(Theme(name="Classic", decorations=[...]))
# theme_mgr.set_active_theme("Classic")
# theme_mgr.export_theme("Classic", Path("classic_theme.json"))
# theme_mgr.import_theme(Path("custom_theme.json"))
# decorations = theme_mgr.apply_theme(DecorationTarget.WINDOW)
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Union
from enum import Enum, auto
import json
from pathlib import Path

class DecorationKind(Enum):
    """Types of decorations that can be applied"""
    COLOR = auto()          # Color-based decorations
    STYLE = auto()          # Style formatting
    PATTERN = auto()        # Visual patterns
    ANIMATION = auto()      # Animated decorations
    INDICATOR = auto()      # Status indicators

class DecorationTarget(Enum):
    """House elements that can be decorated"""
    WINDOW = auto()         # Window decorations
    DOOR = auto()           # Door decorations
    WALL = auto()           # Wall decorations
    ROOF = auto()           # Roof decorations
    FLOOR = auto()          # Floor decorations
    ROOM = auto()           # Room-wide decorations
    HOUSE = auto()          # House-wide decorations

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
    animation: Optional[Dict] = None
    priority: int = 0
    enabled: bool = True

class DecorationManager:
    """Manages decorations for the house"""
    
    def __init__(self):
        self._decorations: Dict[DecorationTarget, List[Decoration]] = {
            target: [] for target in DecorationTarget
        }
        self._color_scheme = ColorScheme()
        self._active_theme = "default"
        self._themes: Dict[str, Dict] = {"default": {}}
        
    def add_decoration(self, decoration: Decoration) -> bool:
        """Add a new decoration to the target"""
        target_decorations = self._decorations[decoration.target]
        
        # Check for conflicts and merge if needed
        for existing in target_decorations:
            if self._decorations_conflict(existing, decoration):
                if existing.priority > decoration.priority:
                    return False
                target_decorations.remove(existing)
        
        target_decorations.append(decoration)
        target_decorations.sort(key=lambda d: -d.priority)  # Higher priority first
        return True
    
    def remove_decoration(self, target: DecorationTarget, 
                         kind: Optional[DecorationKind] = None) -> List[Decoration]:
        """Remove decorations from target"""
        if kind is None:
            removed = self._decorations[target]
            self._decorations[target] = []
            return removed
            
        removed = []
        remaining = []
        for dec in self._decorations[target]:
            if dec.kind == kind:
                removed.append(dec)
            else:
                remaining.append(dec)
        self._decorations[target] = remaining
        return removed
    
    def get_decorations(self, target: DecorationTarget) -> List[Decoration]:
        """Get all decorations for a target"""
        return self._decorations[target].copy()
    
    def create_theme(self, name: str, decorations: List[Decoration],
                    color_scheme: Optional[ColorScheme] = None) -> bool:
        """Create a new decoration theme"""
        if name in self._themes:
            return False
            
        self._themes[name] = {
            "decorations": decorations,
            "color_scheme": color_scheme or self._color_scheme
        }
        return True
    
    def apply_theme(self, name: str) -> bool:
        """Apply a decoration theme"""
        if name not in self._themes:
            return False
            
        theme = self._themes[name]
        self._active_theme = name
        self._color_scheme = theme["color_scheme"]
        
        # Clear existing decorations
        for target in DecorationTarget:
            self._decorations[target] = []
            
        # Apply theme decorations
        for decoration in theme["decorations"]:
            self.add_decoration(decoration)
        
        return True
    
    def export_theme(self, name: str, path: Path):
        """Export a theme to JSON file"""
        if name not in self._themes:
            raise ValueError(f"Theme '{name}' not found")
            
        theme_data = {
            "name": name,
            "color_scheme": vars(self._themes[name]["color_scheme"]),
            "decorations": [
                {
                    "kind": dec.kind.name,
                    "target": dec.target.name,
                    "style": vars(dec.style) if dec.style else None,
                    "color": dec.color,
                    "pattern": dec.pattern,
                    "animation": dec.animation,
                    "priority": dec.priority,
                    "enabled": dec.enabled
                }
                for dec in self._themes[name]["decorations"]
            ]
        }
        
        with open(path, 'w') as f:
            json.dump(theme_data, f, indent=2)
    
    def import_theme(self, path: Path) -> str:
        """Import a theme from JSON file"""
        with open(path) as f:
            theme_data = json.load(f)
            
        name = theme_data["name"]
        color_scheme = ColorScheme(**theme_data["color_scheme"])
        
        decorations = []
        for dec_data in theme_data["decorations"]:
            style_data = dec_data.pop("style", None)
            style = DecorationStyle(**style_data) if style_data else None
            
            decorations.append(Decoration(
                kind=DecorationKind[dec_data["kind"]],
                target=DecorationTarget[dec_data["target"]],
                style=style,
                **{k: v for k, v in dec_data.items() 
                   if k not in ["kind", "target"]}
            ))
        
        self.create_theme(name, decorations, color_scheme)
        return name
    
    def _decorations_conflict(self, a: Decoration, b: Decoration) -> bool:
        """Check if two decorations conflict"""
        if a.target != b.target or a.kind != b.kind:
            return False
            
        # Check specific conflicts based on decoration kind
        if a.kind == DecorationKind.COLOR and a.color == b.color:
            return True
        if a.kind == DecorationKind.STYLE:
            return bool(a.style and b.style)
        if a.kind == DecorationKind.PATTERN:
            return a.pattern == b.pattern
        if a.kind == DecorationKind.ANIMATION:
            return bool(a.animation and b.animation)
        
        return False