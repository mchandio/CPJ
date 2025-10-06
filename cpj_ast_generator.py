"""
CPJ AST Generator - Builds the abstract syntax tree for our programming house.
This module takes the parser's output and constructs a complete AST that
represents the structure and relationships of our house components.
"""
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from enum import Enum, auto
from .cpj_parser2 import Node, NodeType, House, Room, Blueprint, Material

class ASTVisitor:
    """Base visitor for traversing our house's AST"""
    
    def visit(self, node: Node) -> Any:
        """Visit a node in our house's AST"""
        method = f'visit_{node.__class__.__name__.lower()}'
        if hasattr(self, method):
            return getattr(self, method)(node)
        return self.visit_default(node)
    
    def visit_default(self, node: Node) -> Any:
        """Default visitor method"""
        pass

class ASTGenerator(ASTVisitor):
    """Generates the complete AST for our house"""
    
    def __init__(self):
        self.scope_stack: List[Dict[str, Node]] = [{}]
        self.errors: List[str] = []
    
    def generate(self, node: Node) -> Optional[Node]:
        """Generate AST from parser output"""
        try:
            return self.visit(node)
        except Exception as e:
            self.errors.append(str(e))
            return None
    
    def visit_house(self, node: House) -> House:
        """Visit a complete house (program)"""
        self.enter_scope()
        
        # Process foundation first
        if node.foundation:
            node.foundation = self.visit(node.foundation)
        
        # Process blueprints (type definitions)
        blueprints = []
        for blueprint in node.blueprints:
            processed = self.visit(blueprint)
            if processed:
                blueprints.append(processed)
                self.define(processed.name, processed)
        node.blueprints = blueprints
        
        # Process rooms (functions)
        rooms = []
        for room in node.rooms:
            processed = self.visit(room)
            if processed:
                rooms.append(processed)
                self.define(processed.name, processed)
        node.rooms = rooms
        
        # Process utilities
        utilities = []
        for utility in node.utilities:
            processed = self.visit(utility)
            if processed:
                utilities.append(processed)
        node.utilities = utilities
        
        self.exit_scope()
        return node
    
    def visit_room(self, node: Room) -> Room:
        """Visit a room (function)"""
        self.enter_scope()
        
        # Process parameters
        entrances = []
        for param in node.entrances:
            processed = self.visit(param)
            if processed:
                entrances.append(processed)
                self.define(processed.name, processed)
        node.entrances = entrances
        
        # Process room contents
        if node.contents:
            node.contents = self.visit(node.contents)
        
        self.exit_scope()
        return node
    
    def visit_blueprint(self, node: Blueprint) -> Blueprint:
        """Visit a blueprint (type definition)"""
        self.enter_scope()
        
        # Process materials (fields)
        materials = []
        for material in node.materials:
            processed = self.visit(material)
            if processed:
                materials.append(processed)
                self.define(processed.name, processed)
        node.materials = materials
        
        # Process methods
        methods = []
        for method in node.methods:
            processed = self.visit(method)
            if processed:
                methods.append(processed)
                self.define(processed.name, processed)
        node.methods = methods
        
        self.exit_scope()
        return node
    
    def visit_material(self, node: Material) -> Material:
        """Visit a material (variable)"""
        # Process initializer if present
        if node.initial_state:
            node.initial_state = self.visit(node.initial_state)
        return node
    
    def visit_block(self, node: 'Block') -> 'Block':
        """Visit a block of statements"""
        self.enter_scope()
        
        statements = []
        for stmt in node.statements:
            processed = self.visit(stmt)
            if processed:
                statements.append(processed)
        node.statements = statements
        
        self.exit_scope()
        return node
    
    def visit_if(self, node: 'If') -> 'If':
        """Visit an if statement"""
        node.condition = self.visit(node.condition)
        node.then_branch = self.visit(node.then_branch)
        if node.else_branch:
            node.else_branch = self.visit(node.else_branch)
        return node
    
    def visit_while(self, node: 'While') -> 'While':
        """Visit a while loop"""
        node.condition = self.visit(node.condition)
        node.body = self.visit(node.body)
        return node
    
    def visit_for(self, node: 'For') -> 'For':
        """Visit a for loop"""
        self.enter_scope()
        
        if node.init:
            node.init = self.visit(node.init)
        node.target = self.visit(node.target)
        node.iterable = self.visit(node.iterable)
        node.body = self.visit(node.body)
        
        self.exit_scope()
        return node
    
    def visit_binary(self, node: 'BinaryOp') -> 'BinaryOp':
        """Visit a binary operation"""
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        return node
    
    def visit_unary(self, node: 'UnaryOp') -> 'UnaryOp':
        """Visit a unary operation"""
        node.operand = self.visit(node.operand)
        return node
    
    def visit_call(self, node: 'Call') -> 'Call':
        """Visit a function call"""
        node.callee = self.visit(node.callee)
        
        args = []
        for arg in node.args:
            processed = self.visit(arg)
            if processed:
                args.append(processed)
        node.args = args
        
        kwargs = {}
        for key, value in node.kwargs.items():
            processed = self.visit(value)
            if processed:
                kwargs[key] = processed
        node.kwargs = kwargs
        
        return node
    
    def visit_access(self, node: 'Access') -> 'Access':
        """Visit a member access"""
        node.object = self.visit(node.object)
        return node
    
    # Scope management
    def enter_scope(self):
        """Enter a new scope"""
        self.scope_stack.append({})
    
    def exit_scope(self):
        """Exit the current scope"""
        self.scope_stack.pop()
    
    def define(self, name: str, node: Node):
        """Define a name in the current scope"""
        self.scope_stack[-1][name] = node
    
    def resolve(self, name: str) -> Optional[Node]:
        """Resolve a name in the current scope chain"""
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return None

# Example usage
if __name__ == "__main__":
    # Example AST generation
    from cpj_enhanced_lexer import CPJEnhancedLexer
    from cpj_parser2 import Parser
    
    source = """
    memory {
        auto: true
        manual_override: false
    }
    
    type Room {
        size: int
        purpose: string
    }
    
    fn create_room(size: int, purpose: string) -> Room {
        cpp {
            // High-performance room initialization
            std::unique_ptr<Room> room = std::make_unique<Room>();
        }
        
        python {
            # Flexible room configuration
            room.configure(size=size, purpose=purpose)
        }
        
        java {
            // Enterprise-grade room validation
            RoomValidator.validate(room);
        }
    }
    """
    
    # Generate AST
    lexer = CPJEnhancedLexer(source)
    tokens = lexer.lex()
    parser = Parser(tokens)
    ast = parser.parse()
    
    generator = ASTGenerator()
    processed_ast = generator.generate(ast)
    
    print("House AST generated successfully!")
    if generator.errors:
        print("\nErrors during AST generation:")
        for error in generator.errors:
            print(f"- {error}")