"""Runtime management for decoration features."""

from typing import Dict, Any, Optional, List, Set
from cpj_type_system import TypeSystem
from cpj_house_decorations import (
    DecorationEventType, DecorationEvent, DecorationEventManager,
    DecorationKind, DecorationTarget, DecorationStyle, ColorScheme
)

class DecorationRuntime:
    """Manages decorative features in the house"""
    
    def __init__(self, type_system: TypeSystem):
        self._type_system = type_system
        self._event_manager = DecorationEventManager()
        self._styles: Dict[str, DecorationStyle] = {}
        self._color_schemes: Dict[str, ColorScheme] = {}
        self._active_decorations: Dict[DecorationTarget, Dict[str, Any]] = {}
        
        # Initialize default styles and color schemes
        self._initialize_defaults()
        
    def _initialize_defaults(self):
        """Initialize default decoration configurations"""
        # Default style
        self._styles['default'] = DecorationStyle()
        
        # Light theme
        self._color_schemes['light'] = ColorScheme()
        
        # Dark theme
        self._color_schemes['dark'] = ColorScheme(
            background="#1E1E1E",
            foreground="#FFFFFF",
            accent="#569CD6",
            error="#F44747",
            warning="#CCA700",
            success="#6A9955"
        )
        
        # High contrast theme
        self._color_schemes['high_contrast'] = ColorScheme(
            background="#000000",
            foreground="#FFFFFF",
            accent="#0080FF",
            error="#FF0000",
            warning="#FFFF00",
            success="#00FF00"
        )
        
    def create_style(self, name: str, **style_args) -> DecorationStyle:
        """Create a new decoration style"""
        style = DecorationStyle(**style_args)
        self._styles[name] = style
        return style
        
    def create_color_scheme(self, name: str, **color_args) -> ColorScheme:
        """Create a new color scheme"""
        scheme = ColorScheme(**color_args)
        self._color_schemes[name] = scheme
        return scheme
        
    def apply_decoration(self, target: DecorationTarget, kind: DecorationKind,
                        style_name: Optional[str] = None,
                        scheme_name: Optional[str] = None,
                        **kwargs) -> bool:
        """Apply a decoration to a target"""
        decoration = {
            'kind': kind,
            'style': self._styles.get(style_name or 'default'),
            'scheme': self._color_schemes.get(scheme_name or 'light'),
            **kwargs
        }
        
        # Store the decoration
        if target not in self._active_decorations:
            self._active_decorations[target] = {}
        self._active_decorations[target][kind] = decoration
        
        # Emit decoration event
        event = DecorationEvent(
            DecorationEventType.DECORATION_APPLIED,
            {
                'target': target,
                'decoration': decoration
            }
        )
        self._event_manager.emit(event)
        return True
        
    def get_decoration(self, target: DecorationTarget,
                      kind: Optional[DecorationKind] = None) -> Optional[Dict[str, Any]]:
        """Get active decorations for a target"""
        target_decorations = self._active_decorations.get(target, {})
        if kind:
            return target_decorations.get(kind)
        return target_decorations
        
    def list_styles(self) -> List[str]:
        """List available decoration styles"""
        return list(self._styles.keys())
        
    def list_color_schemes(self) -> List[str]:
        """List available color schemes"""
        return list(self._color_schemes.keys())
        
    def subscribe_to_changes(self, callback: callable,
                           event_type: Optional[DecorationEventType] = None):
        """Subscribe to decoration changes"""
        if event_type:
            self._event_manager.subscribe(event_type, callback)
        else:
            # Subscribe to all event types
            for event_type in DecorationEventType:
                self._event_manager.subscribe(event_type, callback)
                
    def apply_theme(self, target: DecorationTarget, scheme_name: str) -> bool:
        """Apply a color scheme theme to a target"""
        scheme = self._color_schemes.get(scheme_name)
        if not scheme:
            return False
            
        event = DecorationEvent(
            DecorationEventType.THEME_CHANGED,
            {
                'target': target,
                'scheme': scheme_name
            }
        )
        self._event_manager.emit(event)
        return True