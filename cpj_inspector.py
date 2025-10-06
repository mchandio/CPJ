"""
CPJ Foundation Inspector - Error Detection and Reporting System
This module provides comprehensive error checking and reporting
for our CPJ house's foundation components.
"""
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from enum import Enum, auto
from .cpj_enhanced_lexer import Token, TokenType
from .cpj_parser2 import Node, NodeType
from .cpj_ast_generator import ASTVisitor

class ErrorLevel(Enum):
    """Error severity levels"""
    WARNING = auto()
    ERROR = auto()
    CRITICAL = auto()

@dataclass
class FoundationError:
    """Represents an error in our house's foundation"""
    level: ErrorLevel
    message: str
    location: tuple  # (line, column)
    source: str
    context: str

class FoundationInspector(ASTVisitor):
    """Inspects the foundation of our CPJ house for structural issues"""
    
    def __init__(self):
        self.errors: List[FoundationError] = []
        self.current_scope: List[str] = []
        self.defined_types: Dict[str, Node] = {}
        self.defined_rooms: Dict[str, Node] = {}
    
    def inspect(self, ast: Node) -> List[FoundationError]:
        """Inspect the entire house structure"""
        self.visit(ast)
        return self.errors
    
    def report_error(self, level: ErrorLevel, message: str, 
                    node: Node, context: str = ""):
        """Report a foundation issue"""
        error = FoundationError(
            level=level,
            message=message,
            location=node.location,
            source=node.__class__.__name__,
            context=context
        )
        self.errors.append(error)
    
    def visit_house(self, node: 'House'):
        """Inspect overall house structure"""
        # Check foundation presence
        if not node.foundation:
            self.report_error(
                ErrorLevel.CRITICAL,
                "House missing foundation configuration",
                node,
                "Every CPJ program requires basic foundation settings"
            )
        
        # Check for main entry point
        if not any(room.name == "main" for room in node.rooms):
            self.report_error(
                ErrorLevel.ERROR,
                "No main entry point found",
                node,
                "Every house needs a main entrance (main function)"
            )
        
        # Process all components
        super().visit_house(node)
    
    def visit_room(self, node: 'Room'):
        """Inspect room (function) structure"""
        self.current_scope.append(node.name)
        
        # Check return type exists
        if node.exits != "void" and node.exits not in self.defined_types:
            self.report_error(
                ErrorLevel.ERROR,
                f"Unknown return type '{node.exits}'",
                node,
                f"Room exit type must be 'void' or a defined blueprint"
            )
        
        # Check parameter types
        for entrance in node.entrances:
            if entrance.material_type not in self.defined_types:
                self.report_error(
                    ErrorLevel.ERROR,
                    f"Unknown parameter type '{entrance.material_type}'",
                    entrance,
                    "Room entrance materials must use defined types"
                )
        
        # Check room contents
        if not node.contents:
            self.report_error(
                ErrorLevel.WARNING,
                "Empty room found",
                node,
                "Room has no implementation"
            )
        
        super().visit_room(node)
        self.current_scope.pop()
    
    def visit_blueprint(self, node: 'Blueprint'):
        """Inspect blueprint (type) structure"""
        # Register blueprint
        self.defined_types[node.name] = node
        
        # Check material types
        for material in node.materials:
            if material.material_type not in self.defined_types:
                self.report_error(
                    ErrorLevel.ERROR,
                    f"Unknown material type '{material.material_type}'",
                    material,
                    "Blueprint materials must use defined types"
                )
        
        super().visit_blueprint(node)
    
    def visit_block(self, node: 'Block'):
        """Inspect code block structure"""
        if not node.statements:
            self.report_error(
                ErrorLevel.WARNING,
                "Empty block found",
                node,
                "Block contains no statements"
            )
        
        super().visit_block(node)
    
    def visit_material(self, node: 'Material'):
        """Inspect material (variable) usage"""
        # Check material type
        if node.material_type not in self.defined_types:
            self.report_error(
                ErrorLevel.ERROR,
                f"Unknown material type '{node.material_type}'",
                node,
                "Materials must use defined types"
            )
        
        # Check initialization if required
        if not node.is_permanent and not node.initial_state:
            self.report_error(
                ErrorLevel.WARNING,
                "Uninitialized material",
                node,
                "Non-permanent materials should be initialized"
            )
        
        super().visit_material(node)
    
    def visit_if(self, node: 'If'):
        """Inspect conditional statements"""
        if not node.condition:
            self.report_error(
                ErrorLevel.ERROR,
                "Missing condition in if statement",
                node,
                "Conditional statements require a condition"
            )
        
        super().visit_if(node)
    
    def visit_while(self, node: 'While'):
        """Inspect loop structures"""
        if not node.condition:
            self.report_error(
                ErrorLevel.ERROR,
                "Missing condition in while loop",
                node,
                "Loops require a condition"
            )
        
        super().visit_while(node)
    
    def visit_for(self, node: 'For'):
        """Inspect for loop structures"""
        if not node.target or not node.iterable:
            self.report_error(
                ErrorLevel.ERROR,
                "Incomplete for loop structure",
                node,
                "For loops require both target and iterable"
            )
        
        super().visit_for(node)
    
    def visit_call(self, node: 'Call'):
        """Inspect function calls"""
        # Check if called room exists
        if isinstance(node.callee, Node):
            room_name = node.callee.name
            if room_name not in self.defined_rooms:
                self.report_error(
                    ErrorLevel.ERROR,
                    f"Call to undefined room '{room_name}'",
                    node,
                    "Can only call rooms that exist in the house"
                )
        
        super().visit_call(node)

# Example usage
if __name__ == "__main__":
    from cpj_enhanced_lexer import CPJEnhancedLexer
    from cpj_parser2 import Parser
    from cpj_ast_generator import ASTGenerator
    
    # Example code with some intentional issues
    source = """
    // Missing memory configuration
    
    type Room {
        size: unknown_type  // Error: undefined type
        purpose: string
    }
    
    fn create_room() -> Room {
        // Empty room - will generate warning
    }
    
    // Missing main function - will generate error
    """
    
    # Generate and inspect AST
    lexer = CPJEnhancedLexer(source)
    tokens = lexer.lex()
    parser = Parser(tokens)
    ast = parser.parse()
    
    generator = ASTGenerator()
    processed_ast = generator.generate(ast)
    
    inspector = FoundationInspector()
    errors = inspector.inspect(processed_ast)
    
    # Report findings
    print("Foundation Inspection Results:")
    for error in errors:
        print(f"\n{error.level.name} at line {error.location[0]}:")
        print(f"  {error.message}")
        if error.context:
            print(f"  Context: {error.context}")