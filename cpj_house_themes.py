"""CPJ House Theme System

Manages complete themes that combine decorations, styles, and color schemes
into cohesive visual experiences.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from pathlib import Path
import json
from datetime import datetime

from cpj_house_decorations import (
    DecorationManager, Decoration, DecorationKind, 
    DecorationTarget, DecorationStyle, ColorScheme
)
from cpj_house_styles import StyleManager, CodeStyle, SyntaxStyle

@dataclass
class ThemeMetadata:
    """Metadata for a house theme"""
    name: str
    description: str
    author: str = "Unknown"
    version: str = "1.0.0"
    created: datetime = field(default_factory=datetime.now)
    modified: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

class Theme:
    """Complete house theme including decorations and styles"""
    
    def __init__(self, metadata: ThemeMetadata):
        self.metadata = metadata
        self.decorations: List[Decoration] = []
        self.code_style = CodeStyle()
        self.syntax_style = SyntaxStyle(ColorScheme())
    
    def to_dict(self) -> Dict:
        """Convert theme to dictionary for serialization"""
        return {
            "metadata": {
                "name": self.metadata.name,
                "description": self.metadata.description,
                "author": self.metadata.author,
                "version": self.metadata.version,
                "created": self.metadata.created.isoformat(),
                "modified": self.metadata.modified.isoformat(),
                "tags": self.metadata.tags
            },
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
                for dec in self.decorations
            ],
            "code_style": vars(self.code_style),
            "syntax_style": {
                **vars(self.syntax_style),
                "color_scheme": vars(self.syntax_style.color_scheme)
            }
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Theme':
        """Create theme from dictionary"""
        metadata = ThemeMetadata(
            name=data["metadata"]["name"],
            description=data["metadata"]["description"],
            author=data["metadata"].get("author", "Unknown"),
            version=data["metadata"].get("version", "1.0.0"),
            created=datetime.fromisoformat(data["metadata"]["created"]),
            modified=datetime.fromisoformat(data["metadata"]["modified"]),
            tags=data["metadata"].get("tags", [])
        )
        
        theme = cls(metadata)
        
        # Load decorations
        for dec_data in data["decorations"]:
            style_data = dec_data.pop("style", None)
            style = DecorationStyle(**style_data) if style_data else None
            
            decoration = Decoration(
                kind=DecorationKind[dec_data["kind"]],
                target=DecorationTarget[dec_data["target"]],
                style=style,
                **{k: v for k, v in dec_data.items() 
                   if k not in ["kind", "target"]}
            )
            theme.decorations.append(decoration)
        
        # Load styles
        theme.code_style = CodeStyle(**data["code_style"])
        syntax_data = data["syntax_style"]
        color_scheme = ColorScheme(**syntax_data.pop("color_scheme", {}))
        theme.syntax_style = SyntaxStyle(color_scheme, **syntax_data)
        
        return theme

class ThemeRegistry:
    """Central registry for managing house themes"""
    
    def __init__(self, decoration_manager: DecorationManager, 
                 style_manager: StyleManager):
        self.decoration_manager = decoration_manager
        self.style_manager = style_manager
        self.themes: Dict[str, Theme] = {}
        self._active_theme: Optional[str] = None
        
        # Initialize with default themes
        self._create_default_themes()
    
    def create_theme(self, metadata: ThemeMetadata) -> Theme:
        """Create a new theme"""
        if metadata.name in self.themes:
            raise ValueError(f"Theme '{metadata.name}' already exists")
            
        theme = Theme(metadata)
        self.themes[metadata.name] = theme
        return theme
    
    def apply_theme(self, name: str) -> bool:
        """Apply a theme to the house"""
        if name not in self.themes:
            return False
            
        theme = self.themes[name]
        
        # Apply decorations
        for decoration in theme.decorations:
            self.decoration_manager.add_decoration(decoration)
        
        # Apply styles
        self.style_manager.code_style = theme.code_style
        self.style_manager.syntax_style = theme.syntax_style
        
        self._active_theme = name
        return True
    
    def get_active_theme(self) -> Optional[Theme]:
        """Get currently active theme"""
        return self.themes.get(self._active_theme)
    
    def save_theme(self, name: str, path: Path):
        """Save theme to file"""
        if name not in self.themes:
            raise ValueError(f"Theme '{name}' not found")
            
        theme_data = self.themes[name].to_dict()
        with open(path, 'w') as f:
            json.dump(theme_data, f, indent=2)
    
    def load_theme(self, path: Path) -> str:
        """Load theme from file"""
        with open(path) as f:
            theme_data = json.load(f)
            
        theme = Theme.from_dict(theme_data)
        self.themes[theme.metadata.name] = theme
        return theme.metadata.name
    
    def _create_default_themes(self):
        """Create default built-in themes"""
        # Light theme
        light = self.create_theme(ThemeMetadata(
            name="light",
            description="Default light theme",
            author="CPJ",
            tags=["light", "default"]
        ))
        light.code_style = CodeStyle()
        light.syntax_style = SyntaxStyle(ColorScheme())
        
        # Dark theme
        dark = self.create_theme(ThemeMetadata(
            name="dark",
            description="Default dark theme",
            author="CPJ",
            tags=["dark", "default"]
        ))
        dark.code_style = CodeStyle()
        dark.syntax_style = SyntaxStyle(ColorScheme(
            background="#1E1E1E",
            foreground="#D4D4D4",
            accent="#569CD6",
            syntax_colors={
                "keyword": "#569CD6",
                "string": "#CE9178",
                "number": "#B5CEA8",
                "comment": "#6A9955",
                "type": "#4EC9B0",
                "function": "#DCDCAA",
                "variable": "#9CDCFE"
            }
        ))
        
        # Nature theme
        nature = self.create_theme(ThemeMetadata(
            name="nature",
            description="Nature-inspired theme with earthy colors",
            author="CPJ",
            tags=["nature", "custom"]
        ))
        nature.code_style = CodeStyle(indent_size=2)
        nature.syntax_style = SyntaxStyle(ColorScheme(
            background="#F5F5DC",  # Beige
            foreground="#2F4F4F",  # Dark slate gray
            accent="#228B22",      # Forest green
            syntax_colors={
                "keyword": "#006400",  # Dark green
                "string": "#8B4513",   # Saddle brown
                "number": "#A0522D",   # Sienna
                "comment": "#556B2F",  # Dark olive green
                "type": "#2F4F4F",     # Dark slate gray
                "function": "#4A4A00", # Olive drab
                "variable": "#004225"   # Dark forest green
            }
        ))

# Example usage:
# registry = ThemeRegistry(decoration_manager, style_manager)
# registry.apply_theme("dark")
# 
# # Create custom theme
# custom = registry.create_theme(ThemeMetadata(
#     name="custom",
#     description="My custom theme",
#     author="User"
# ))
# custom.decorations = [...]  # Add decorations
# custom.code_style = CodeStyle(...)  # Configure style
# registry.apply_theme("custom")