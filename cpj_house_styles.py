"""CPJ House Style Customization

Provides concrete implementations for code style formatting and syntax highlighting,
integrating with the base decoration system.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Set
from pathlib import Path
import re

from cpj_house_decorations import (
    DecorationManager, Decoration, DecorationKind, 
    DecorationTarget, DecorationStyle, ColorScheme
)

@dataclass
class CodeStyle:
    """Code formatting style configuration"""
    indent_size: int = 4
    use_tabs: bool = False
    max_line_length: int = 80
    align_parameters: bool = True
    space_before_blocks: bool = True
    space_around_operators: bool = True
    blank_lines_between_sections: int = 2
    wrap_long_lines: bool = True
    sort_imports: bool = True

@dataclass
class SyntaxStyle:
    """Syntax highlighting style configuration"""
    color_scheme: ColorScheme
    highlight_matching_brackets: bool = True
    highlight_current_line: bool = True
    show_indent_guides: bool = True
    show_whitespace: bool = False
    rainbow_brackets: bool = True

class StyleManager:
    """Manages code style and syntax highlighting"""
    
    def __init__(self, decoration_manager: DecorationManager):
        self.decoration_manager = decoration_manager
        self.code_style = CodeStyle()
        self.syntax_style = SyntaxStyle(ColorScheme())
        
    def apply_code_style(self, code: str) -> str:
        """Apply code formatting style to code string"""
        lines = code.split('\n')
        formatted = []
        
        indent = '\t' if self.code_style.use_tabs else ' ' * self.code_style.indent_size
        current_indent = 0
        
        for line in lines:
            # Strip existing indentation
            stripped = line.lstrip()
            if not stripped:
                if self.code_style.blank_lines_between_sections > 1:
                    formatted.append('')
                continue
                
            # Calculate new indentation level
            if stripped.startswith(('class ', 'def ', 'if ', 'while ', 'for ', 'try:', 'else:', 'elif ')):
                if self.code_style.space_before_blocks:
                    formatted.append('')
                new_line = indent * current_indent + stripped
                formatted.append(new_line)
                if stripped.endswith(':'):
                    current_indent += 1
            elif stripped.startswith(('return', 'break', 'continue', 'pass')):
                new_line = indent * current_indent + stripped
                formatted.append(new_line)
                if current_indent > 0:
                    current_indent -= 1
            else:
                new_line = indent * current_indent + stripped
                if self.code_style.wrap_long_lines and len(new_line) > self.code_style.max_line_length:
                    # Simple wrapping for demonstration
                    wrapped = self._wrap_line(new_line, self.code_style.max_line_length)
                    formatted.extend(wrapped)
                else:
                    formatted.append(new_line)
        
        return '\n'.join(formatted)
    
    def _wrap_line(self, line: str, max_length: int) -> List[str]:
        """Wrap a line to fit within max_length"""
        if len(line) <= max_length:
            return [line]
            
        indent = ' ' * (len(line) - len(line.lstrip()))
        parts = line.lstrip().split()
        lines = []
        current = indent
        
        for part in parts:
            if len(current) + len(part) + 1 <= max_length:
                current += ' ' + part if current != indent else part
            else:
                lines.append(current)
                current = indent + '    ' + part
        
        if current:
            lines.append(current)
        
        return lines
    
    def create_syntax_decorations(self, target: DecorationTarget) -> List[Decoration]:
        """Create syntax highlighting decorations for a target"""
        decorations = []
        
        # Basic syntax colors
        for token_type, color in self.syntax_style.color_scheme.syntax_colors.items():
            decorations.append(Decoration(
                kind=DecorationKind.COLOR,
                target=target,
                color=color,
                priority=100,
                enabled=True
            ))
        
        # Special highlighting features
        if self.syntax_style.highlight_matching_brackets:
            decorations.append(Decoration(
                kind=DecorationKind.COLOR,
                target=target,
                color=self.syntax_style.color_scheme.accent,
                priority=200,
                enabled=True
            ))
        
        if self.syntax_style.highlight_current_line:
            decorations.append(Decoration(
                kind=DecorationKind.COLOR,
                target=target,
                color=f"{self.syntax_style.color_scheme.background}22",  # Semi-transparent
                priority=50,
                enabled=True
            ))
        
        if self.syntax_style.show_indent_guides:
            decorations.append(Decoration(
                kind=DecorationKind.PATTERN,
                target=target,
                pattern="indent_guide",
                color=f"{self.syntax_style.color_scheme.foreground}22",
                priority=25,
                enabled=True
            ))
        
        return decorations
    
    def apply_syntax_style(self, target: DecorationTarget):
        """Apply syntax highlighting style to a target"""
        decorations = self.create_syntax_decorations(target)
        for decoration in decorations:
            self.decoration_manager.add_decoration(decoration)
    
    def load_style_config(self, path: Path):
        """Load style configuration from file"""
        import json
        with open(path) as f:
            config = json.load(f)
            
        if "code_style" in config:
            self.code_style = CodeStyle(**config["code_style"])
            
        if "syntax_style" in config:
            syntax_config = config["syntax_style"]
            color_scheme = ColorScheme(**syntax_config.pop("color_scheme", {}))
            self.syntax_style = SyntaxStyle(color_scheme, **syntax_config)
    
    def save_style_config(self, path: Path):
        """Save style configuration to file"""
        config = {
            "code_style": vars(self.code_style),
            "syntax_style": {
                **vars(self.syntax_style),
                "color_scheme": vars(self.syntax_style.color_scheme)
            }
        }
        
        with open(path, 'w') as f:
            json.dump(config, f, indent=2)

# Example style configurations
DEFAULT_LIGHT_STYLE = {
    "code_style": CodeStyle(),
    "syntax_style": SyntaxStyle(ColorScheme())
}

DEFAULT_DARK_STYLE = {
    "code_style": CodeStyle(),
    "syntax_style": SyntaxStyle(ColorScheme(
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
}