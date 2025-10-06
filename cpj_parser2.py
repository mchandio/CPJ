"""CPJ Parser - AST Generation and Full Language Support using house metaphor"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Dict, Union, Any, TypeVar

from cpj_type_system import WallSection, TypeSystem, TypeKind
from cpj_parser_helpers import Variable, Expression, ParseError

T = TypeVar('T')

class TokenType(Enum):
    # House structure tokens
    PUBLIC = auto()
    PRIVATE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    
    # Basic tokens
    IDENTIFIER = auto()
    LBRACE = auto()
    RBRACE = auto()
    LPAREN = auto()
    RPAREN = auto()
    COLON = auto()
    COMMA = auto()
    ARROW = auto()
    EQUAL = auto()
    SEMI = auto()
    DOT = auto()
    EOF = auto()  # End of file marker
    
class NodeType(Enum):
    HOUSE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    MATERIAL = auto()
    LANGUAGE_BLOCK = auto()
    LITERAL = auto()
    VARIABLE = auto()

@dataclass
class Node:
    node_type: NodeType
    location: tuple = field(default_factory=lambda: (1, 1))  # (line, column)
    name: str = field(default="")
    wall_section: Optional[WallSection] = field(default=None)  # Type information
    
    def __init__(self, node_type: NodeType, **kwargs):
        self.node_type = node_type
        self.location = kwargs.get('location', (1, 1))
        self.name = kwargs.get('name', "")
        self.wall_section = kwargs.get('wall_section', None)

@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: Any
    line: int
    column: int
    location: tuple = field(init=False)
    
    def __post_init__(self):
        self.location = (self.line, self.column)

@dataclass
class House(Node):
    foundation: Optional['Foundation'] = field(default=None)
    rooms: List['Room'] = field(default_factory=list)
    blueprints: Dict[str, 'Blueprint'] = field(default_factory=dict)
    utilities: List['Utility'] = field(default_factory=list)
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.HOUSE, **kwargs)
        self.foundation = kwargs.get('foundation', None)
        self.rooms = kwargs.get('rooms', [])
        self.blueprints = kwargs.get('blueprints', {})
        self.utilities = kwargs.get('utilities', [])

@dataclass
class Foundation(Node):
    memory_config: Dict[str, Any] = field(default_factory=dict)
    type_system: TypeSystem = field(default_factory=TypeSystem)
    utilities: List['Utility'] = field(default_factory=list)
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.FOUNDATION, **kwargs)
        self.memory_config = kwargs.get('memory_config', {})
        self.type_system = kwargs.get('type_system', TypeSystem())
        self.utilities = kwargs.get('utilities', [])

@dataclass
class Room(Node):
    purpose: str = field(default="")  # Room's purpose (function's role)
    entrances: List[Variable] = field(default_factory=list)  # Parameters
    exits: WallSection = field(default_factory=lambda: WallSection(TypeKind.UNDEFINED, 'void'))  # Return type
    contents: Optional['Block'] = field(default=None)  # Function body
    is_async: bool = field(default=False)  # Async rooms
    windows: List[Window] = field(default_factory=list)  # State inspection points
    doors: List[Door] = field(default_factory=list)  # Access control points
    lights: List[Light] = field(default_factory=list)  # Output/logging points
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.ROOM, **kwargs)
        self.purpose = kwargs.get('purpose', "")
        self.entrances = kwargs.get('entrances', [])
        self.exits = kwargs.get('exits', WallSection(TypeKind.UNDEFINED, 'void'))
        self.contents = kwargs.get('contents', None)
        self.is_async = kwargs.get('is_async', False)
        self.windows = kwargs.get('windows', [])
        self.doors = kwargs.get('doors', [])
        self.lights = kwargs.get('lights', [])

@dataclass
class Blueprint(Node):
    body: Optional['Block'] = field(default=None)
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.BLUEPRINT, **kwargs)
        self.body = kwargs.get('body', None)

@dataclass
class Utility(Node):
    body: Optional['Block'] = field(default=None)
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.UTILITY, **kwargs)
        self.body = kwargs.get('body', None)

@dataclass
class Block(Node):
    """A block of code"""
    statements: List[Node] = field(default_factory=list)
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.LANGUAGE_BLOCK, **kwargs)
        self.statements = kwargs.get('statements', [])

@dataclass
class Material(Node):
    """A constant value"""
    value: Any = field(default=None)
    
    def __init__(self, **kwargs):
        super().__init__(NodeType.MATERIAL, **kwargs)
        self.value = kwargs.get('value', None)

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.type_system = TypeSystem()
        
    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF
    
    def peek(self) -> Token:
        return self.tokens[self.current]
    
    def previous(self) -> Token:
        return self.tokens[self.current - 1]
    
    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()
    
    def match(self, *types: TokenType) -> bool:
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False
    
    def check(self, type: TokenType) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == type
    
    def consume(self, type: TokenType, message: str) -> Token:
        if self.check(type):
            return self.advance()
        raise ParseError(message)

    def parse_parameters(self) -> List[Variable]:
        params = []
        self.consume(TokenType.LPAREN, "Expected '(' after room name")
        while not self.is_at_end() and self.peek().type != TokenType.RPAREN:
            name = self.consume(TokenType.IDENTIFIER, "Expected parameter name")
            type_annotation = None
            if self.match(TokenType.COLON):
                type_annotation = self.parse_type()
            params.append(Variable(name=name.lexeme, type=type_annotation))
            if not self.match(TokenType.COMMA):
                break
        self.consume(TokenType.RPAREN, "Expected ')' after parameters")
        return params

    def parse_type(self) -> WallSection:
        type_name = self.consume(TokenType.IDENTIFIER, "Expected type name").lexeme
        return WallSection(TypeKind.UNDEFINED, type_name)
        
    def parse_room(self) -> Room:
        name = self.consume(TokenType.IDENTIFIER, "Expected room name").lexeme
        params = self.parse_parameters() if self.peek().type == TokenType.LPAREN else []
        return_type = self.parse_type() if self.peek().type == TokenType.ARROW else WallSection(TypeKind.UNDEFINED, 'void')
        body = self.parse_block()
        
        return Room(
            name=name,
            purpose="",  # Can be updated later
            entrances=params,
            exits=return_type,
            contents=body
        )
        
    def parse_block(self) -> Block:
        statements = []
        self.consume(TokenType.LBRACE, "Expected '{' before block")
        
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            statements.append(self.parse_statement())
            
        self.consume(TokenType.RBRACE, "Expected '}' after block")
        
        return Block(statements=statements)

    def parse_statement(self) -> Node:
        if self.match(TokenType.ROOM):
            return self.parse_room()
        elif self.match(TokenType.BLUEPRINT):
            return self.parse_blueprint()
        elif self.match(TokenType.UTILITY):
            return self.parse_utility()
        elif self.match(TokenType.WINDOW):
            return self.parse_window()
        elif self.match(TokenType.DOOR):
            return self.parse_door()
        elif self.match(TokenType.LIGHT):
            return self.parse_light()
        else:
            raise ParseError(f"Unexpected token {self.peek().type} at {self.peek().location}")

    def parse_window(self) -> Window:
        name = self.consume(TokenType.IDENTIFIER, "Expected window name").lexeme
        self.consume(TokenType.LPAREN, "Expected '(' after window name")
        target = self.consume(TokenType.IDENTIFIER, "Expected target identifier").lexeme
        access = AccessLevel.PUBLIC
        if self.match(TokenType.COLON):
            access_str = self.consume(TokenType.IDENTIFIER, "Expected access level").lexeme.upper()
            access = AccessLevel[access_str]
        self.consume(TokenType.RPAREN, "Expected ')' after window definition")
        return Window(name=name, target=target, access_level=access)

    def parse_door(self) -> Door:
        name = self.consume(TokenType.IDENTIFIER, "Expected door name").lexeme
        self.consume(TokenType.LPAREN, "Expected '(' after door name")
        source = self.consume(TokenType.IDENTIFIER, "Expected source room name").lexeme
        self.consume(TokenType.ARROW, "Expected '->' between rooms")
        target = self.consume(TokenType.IDENTIFIER, "Expected target room name").lexeme
        access = AccessLevel.PRIVATE
        allowed_types = []
        if self.match(TokenType.COLON):
            access_str = self.consume(TokenType.IDENTIFIER, "Expected access level").lexeme.upper()
            access = AccessLevel[access_str]
            if self.match(TokenType.LBRACE):
                while not self.check(TokenType.RBRACE):
                    type_wall = self.parse_type()
                    allowed_types.append(type_wall)
                    if not self.match(TokenType.COMMA):
                        break
                self.consume(TokenType.RBRACE, "Expected '}' after allowed types")
        self.consume(TokenType.RPAREN, "Expected ')' after door definition")
        return Door(name=name, source_room=source, target_room=target,
                   access_level=access, allowed_types=allowed_types)

    def parse_light(self) -> Light:
        name = self.consume(TokenType.IDENTIFIER, "Expected light name").lexeme
        level = "info"
        format = "{message}"
        if self.match(TokenType.LPAREN):
            if self.peek().type == TokenType.IDENTIFIER:
                level = self.consume(TokenType.IDENTIFIER, "Expected light level").lexeme
            if self.match(TokenType.COMMA):
                format = self.consume(TokenType.STRING, "Expected format string").lexeme
            self.consume(TokenType.RPAREN, "Expected ')' after light configuration")
        return Light(name=name, level=level, format=format)
    
    def parse_blueprint(self) -> Blueprint:
        name = self.consume(TokenType.IDENTIFIER, "Expected blueprint name").lexeme
        body = self.parse_block()
        return Blueprint(
            name=name,
            body=body)
    
    def parse_utility(self) -> Utility:
        name = self.consume(TokenType.IDENTIFIER, "Expected utility name").lexeme
        body = self.parse_block()
        return Utility(
            node_type=NodeType.UTILITY,
            name=name,
            body=body
        )

    def add_to_house(self, area: Node, rooms: List['Room'], 
                    blueprints: List['Blueprint'], utilities: List['Utility']):
        if isinstance(area, Room):
            rooms.append(area)
        elif isinstance(area, Blueprint):
            blueprints[area.name] = area
        elif isinstance(area, Utility):
            utilities.append(area)
        else:
            raise ParseError(f"Unexpected area type {type(area).__name__}")

    def parse_house(self) -> House:
        rooms = []
        blueprints = {}
        utilities = []
        foundation = None

        while not self.is_at_end():
            if self.match(TokenType.FOUNDATION):
                if foundation is not None:
                    raise ParseError("Only one foundation allowed per house")
                foundation = self.parse_foundation()
            else:
                area = self.parse_statement()
                self.add_to_house(area, rooms, blueprints, utilities)

        return House(
            node_type=NodeType.HOUSE,
            name="main",
            foundation=foundation,
            rooms=rooms,
            blueprints=blueprints,
            utilities=utilities
        )

    def parse_foundation(self) -> Foundation:
        memory_config = {}  # Parse memory configuration
        type_system = TypeSystem()  # Configure type system
        utilities = []  # Parse foundation utilities
        
        self.consume(TokenType.LBRACE, "Expected '{' after foundation")
        
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            area = self.parse_statement()
            if isinstance(area, Utility):
                utilities.append(area)
            else:
                raise ParseError("Only utilities allowed in foundation")
                
        self.consume(TokenType.RBRACE, "Expected '}' after foundation block")
        
        return Foundation(
            node_type=NodeType.FOUNDATION,
            memory_config=memory_config,
            type_system=type_system,
            utilities=utilities
        )
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Union, Any, TypeVar
from dataclasses import dataclass, field
from cpj_type_system import WallSection, TypeSystem, TypeKind
from cpj_parser_helpers import Variable, Expression, ParseError
from cpj_house_features import Window, Door, Light
from cpj_enums import NodeType, TokenType, AccessLevel

class AccessLevel(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()

T = TypeVar('T')

class NodeType(Enum):
    HOUSE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    MATERIAL = auto()
    LANGUAGE_BLOCK = auto()
    LITERAL = auto()
    VARIABLE = auto()

@dataclass
class Node:
    node_type: NodeType
    location: tuple = field(default_factory=lambda: (1, 1))  # (line, column)
    name: str = field(default="")
    wall_section: Optional[WallSection] = field(default=None)  # Type information
    
    def __init__(self, node_type: NodeType, **kwargs):
        self.node_type = node_type
        self.location = kwargs.get('location', (1, 1))
        self.name = kwargs.get('name', "")
        self.wall_section = kwargs.get('wall_section', None)
from enum import Enum, auto
from cpj_enhanced_lexer import Token
def parse_room(self) -> 'Room':
        """Parse a room (function) definition"""
        name = self.consume(TokenType.IDENTIFIER, "Expected room name").text
        
        # Parse parameters
        self.consume(TokenType.LPAREN, "Expected '(' after room name")
        parameters = []
        
        while not self.check(TokenType.RPAREN):
            param_name = self.consume(TokenType.IDENTIFIER, "Expected parameter name").text
            self.consume(TokenType.COLON, "Expected ':' after parameter name")
            param_type = self.parse_type_reference()
            
            param = Variable(
                node_type=NodeType.VARIABLE,
                name=param_name,
                var_type=param_type
            )
            parameters.append(param)
            
            if not self.match(TokenType.COMMA):
                break
                
        self.consume(TokenType.RPAREN, "Expected ')' after parameters")
        
        # Parse return type
        return_type = "void"
        if self.match(TokenType.ARROW):
            return_type = self.parse_type_reference()
        
        # Parse room body
        contents = self.parse_block()
        
        room = Room(
            node_type=NodeType.ROOM,
            name=name,
            entrances=parameters,
            exits=return_type,
            contents=contents,
            purpose="" # Default purpose
        )
        
        # Register room type in type system
        param_types = [self.type_system.get_type(p.var_type) for p in parameters]
        return_wall = self.type_system.get_type(return_type)
        room.wall_section = self.type_system.create_function_type(param_types, return_wall)
        
        return room
    
    def add_to_house(self, area: Node, rooms: List[Room], 
                     blueprints: List['Blueprint'], utilities: List['Utility']):
        """Add parsed area to appropriate house section"""
        if area.node_type == NodeType.ROOM:
            rooms.append(area)
        elif area.node_type == NodeType.BLUEPRINT:
            blueprints.append(area)
        elif area.node_type == NodeType.UTILITY:
            utilities.append(area)em, TypeKind, WallSection

# Type variables for recursive types
T = TypeVar('T')

class TokenType(Enum):
    # House structure tokens
    PUBLIC = auto()
    PRIVATE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    
    # Basic tokens
    IDENTIFIER = auto()
    LBRACE = auto()
    RBRACE = auto()
    LPAREN = auto()
    RPAREN = auto()
    COLON = auto()
    COMMA = auto()
    ARROW = auto()
    EQUAL = auto()
    SEMI = auto()
    DOT = auto()
    EOF = auto()  # End of file marker
    
    # Type system
    TYPE = auto()
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOL = auto()
    VOID = auto()

# House-specific types
@dataclass
class Blueprint(Node):
    """Type definition blueprint"""
    materials: List['Material'] = field(default_factory=list)
    methods: List['Room'] = field(default_factory=list)
    variants: List[str] = field(default_factory=list)  # For generic types
    
    def __init__(self, node_type: NodeType = NodeType.BLUEPRINT, **kwargs):
        super().__init__(node_type=node_type, **kwargs)

@dataclass
class Utility(Node):
    """Built-in feature or tool"""
    purpose: str = field(default="")
    implementation: Optional['Block'] = field(default=None)

@dataclass
@dataclass
class Material(Node):
    """A constant value"""
    value: Any = field(default=None)
    
    def __init__(self, node_type: NodeType = NodeType.MATERIAL, **kwargs):
        super().__init__(node_type, **kwargs)
        self.value = kwargs.get('value', None)

# AST Node Types
class NodeType(Enum):
    # House Foundation
    HOUSE = auto()         # Complete program
    FOUNDATION = auto()    # Core language features
    ROOM = auto()         # Function/module
    BLUEPRINT = auto()     # Type definition
    MATERIAL = auto()     # Variable/constant
    UTILITY = auto()      # Built-in features
    
    # Statements
    BLOCK = auto()
    IF = auto()
    WHILE = auto()
    FOR = auto()
    MATCH = auto()
    RETURN = auto()
    IMPORT = auto()
    TRY = auto()
    
    # Expressions
    BINARY = auto()
    UNARY = auto()
    CALL = auto()
    ACCESS = auto()
    LITERAL = auto()
    IDENTIFIER = auto()
    
    # Language Blocks
    CPP_BLOCK = auto()
    PYTHON_BLOCK = auto()
    JAVA_BLOCK = auto()
    GUI_BLOCK = auto()

@dataclass
class Type:
    """Material type specification"""
    name: str
    params: List['Type'] = field(default_factory=list)  # For generic types
    is_optional: bool = False

class NodeType(Enum):
    HOUSE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    MATERIAL = auto()
    LANGUAGE_BLOCK = auto()
    LITERAL = auto()
    FN = auto()

@dataclass
class Node:
    node_type: NodeType
    location: tuple = field(default_factory=lambda: (1, 1))  # (line, column)
    name: str = field(default="")
    wall_section: Optional[WallSection] = field(default=None)  # Type information
    
    def __init__(self, node_type: NodeType, **kwargs):
        self.node_type = node_type
        self.location = kwargs.get('location', (1, 1))
        self.name = kwargs.get('name', "")
        self.wall_section = kwargs.get('wall_section', None)

@dataclass
class House(Node):
    """Represents a complete CPJ program as a house"""
    foundation: Optional['Foundation'] = field(default=None)
    rooms: List['Room'] = field(default_factory=list)
    blueprints: List['Blueprint'] = field(default_factory=list)
    utilities: List['Utility'] = field(default_factory=list)
    public_areas: List[str] = field(default_factory=list)  # Public interface
    
    def __post_init__(self):
        self.node_type = NodeType.HOUSE

@dataclass
class Foundation(Node):
    """Core language features and configuration"""
    memory_config: Dict[str, Any] = field(default_factory=dict)
    type_system: Dict[str, Any] = field(default_factory=dict)
    error_handling: Dict[str, Any] = field(default_factory=dict)

@dataclass
class TypeDecl(Node):
    fields: List['Material'] = field(default_factory=list)
    methods: List['Room'] = field(default_factory=list)
    type_params: List[str] = field(default_factory=list)  # For generic types

@dataclass
@dataclass
class Room(Node):
    """A function/module represented as a room"""
    purpose: str = field(default="")  # Room's purpose (function's role)
    entrances: List['Variable'] = field(default_factory=list)  # Parameters
    exits: WallSection = field(default_factory=lambda: WallSection(TypeKind.UNDEFINED, 'void'))  # Return type
    contents: Optional['Block'] = field(default=None)  # Function body
    is_async: bool = field(default=False)  # Async rooms
    
    def __init__(self, node_type: NodeType = NodeType.ROOM, **kwargs):
        super().__init__(node_type, **kwargs)
        self.purpose = kwargs.get('purpose', "")
        self.entrances = kwargs.get('entrances', [])
        self.exits = kwargs.get('exits', WallSection(TypeKind.UNDEFINED, 'void'))
        self.contents = kwargs.get('contents', None)
        self.is_async = kwargs.get('is_async', False)

@dataclass
class Variable(Node):
    var_type: str = field(default="")
    initializer: Optional[Node] = field(default=None)
    is_const: bool = False

@dataclass
class Block(Node):
    """A block of code"""
    statements: List[Node] = field(default_factory=list)
    
    def __init__(self, node_type: NodeType = NodeType.LANGUAGE_BLOCK, **kwargs):
        super().__init__(node_type, **kwargs)
        self.statements = kwargs.get('statements', [])

@dataclass
class If(Node):
    """Conditional branching"""
    condition: Optional[Node] = field(default=None)
    then_branch: Optional[Node] = field(default=None)
    else_branch: Optional[Node] = field(default=None)

@dataclass
class While(Node):
    """Loop structure"""
    condition: Optional[Node] = field(default=None)
    body: Optional[Node] = field(default=None)

@dataclass
class For(Node):
    """Iteration structure"""
    init: Optional[Node] = field(default=None)
    target: Optional[Node] = field(default=None)
    iterable: Optional[Node] = field(default=None)
    body: Optional[Node] = field(default=None)
    is_parallel: bool = field(default=False)

@dataclass
class Match(Node):
    subject: Optional[Node] = field(default=None)
    cases: List[tuple[Node, Node]] = field(default_factory=list)  # [(pattern, body), ...]

@dataclass
class Try(Node):
    body: Optional[Node] = field(default=None)
    catches: List[tuple[str, str, Node]] = field(default_factory=list)  # [(type, name, handler), ...]
    finally_block: Optional[Node] = field(default=None)

@dataclass
class Import(Node):
    module: str = field(default="")
    names: List[tuple[str, Optional[str]]] = field(default_factory=list)  # [(name, alias), ...]

@dataclass
class BinaryOp(Node):
    op: str = field(default="")
    left: Optional[Node] = field(default=None)
    right: Optional[Node] = field(default=None)

@dataclass
class UnaryOp(Node):
    op: str = field(default="")
    operand: Optional[Node] = field(default=None)

@dataclass
class Call(Node):
    callee: Optional[Node] = field(default=None)
    args: List[Node] = field(default_factory=list)
    kwargs: Dict[str, Node] = field(default_factory=dict)

@dataclass
class Access(Node):
    object: Optional[Node] = field(default=None)
    member: str = field(default="")

@dataclass
class Literal(Node):
    value: Any = field(default=None)
    literal_type: str = field(default="")
    
    def __post_init__(self):
        self.node_type = NodeType.LITERAL

@dataclass
class Identifier(Node):
    name: str

@dataclass
class LanguageBlock(Node):
    language: str = field(default="")  # 'cpp', 'python', 'java'
    code: str = field(default="")
    
    def __post_init__(self):
        self.node_type = NodeType.LANGUAGE_BLOCK

class Parser:
    def __init__(self, tokens: List[Token]):
        """Initialize parser with tokens from lexer"""
        self.tokens: List[Token] = tokens
        self.current: int = 0
        self.scope_stack: List[Dict[str, Node]] = []  # Track variable scope
        self.errors: List[str] = []
        self.type_system = TypeSystem()  # Add type system
    
    def parse(self) -> House:
        """Parse tokens into a complete house (program)"""
        foundation = self.parse_foundation()
        rooms = []
        blueprints = []
        utilities = []
        public_areas = []
        
        while not self.is_at_end():
            try:
                if self.match(TokenType.PUBLIC):
                    self.advance()  # Skip ':'
                    while not self.check(TokenType.PRIVATE) and not self.is_at_end():
                        area = self.parse_house_area()
                        self.add_to_house(area, rooms, blueprints, utilities)
                        public_areas.append(area.name)
                else:
                    area = self.parse_house_area()
                    self.add_to_house(area, rooms, blueprints, utilities)
            except Exception as e:
                self.synchronize()
                self.errors.append(str(e))
        
        return House(
            type=NodeType.HOUSE,
            location=(1, 1),
            name="main",
            foundation=foundation,
            rooms=rooms,
            blueprints=blueprints,
            utilities=utilities,
            public_areas=public_areas
        )
    
    def parse_foundation(self) -> Foundation:
        """Parse the house foundation (core language features)"""
        memory_config = {}
        type_system = {}
        error_handling = {}
        
        # Parse foundation configurations
        while self.match(TokenType.FOUNDATION):
            section = self.consume(TokenType.IDENTIFIER, "Expected foundation section").text
            self.consume(TokenType.LBRACE, "Expected '{' after section name")
            
            config = {}
            while not self.check(TokenType.RBRACE):
                key = self.consume(TokenType.IDENTIFIER, "Expected config key").text
                self.consume(TokenType.COLON, "Expected ':'")
                value = self.parse_literal()
                config[key] = value
            
            self.consume(TokenType.RBRACE, "Expected '}'")
            
            if section == "memory":
                memory_config = config
            elif section == "types":
                type_system = config
            elif section == "errors":
                error_handling = config
        
        return Foundation(
            node_type=NodeType.FOUNDATION,
            location=(self.previous().line, self.previous().column),
            memory_config=memory_config,
            type_system=type_system,
            utilities=utilities
        )
    
    def parse_house_area(self) -> Node:
        """Parse any top-level house area (room, blueprint, or utility)"""
        if self.match(TokenType.ROOM):
            return self.parse_room()
        elif self.match(TokenType.BLUEPRINT):
            return self.parse_blueprint()
        elif self.match(TokenType.UTILITY):
            return self.parse_utility()
        else:
            raise Exception(f"Expected house area, got {self.peek().type}")
    
    def add_to_house(self, area: Node, rooms: List[Room], 
                     blueprints: List['Blueprint'], utilities: List['Utility']):
        """Add parsed area to appropriate house section"""
        if area.node_type == NodeType.ROOM:
            rooms.append(area)
        elif area.node_type == NodeType.BLUEPRINT:
            blueprints.append(area)
        elif area.node_type == NodeType.UTILITY:
            utilities.append(area)
            
    def parse_literal(self) -> Any:
        """Parse a literal value (number, string, boolean)"""
        token = self.peek()
        
        if token.type == TokenType.INT:
            self.advance()
            return int(token.text)
        elif token.type == TokenType.FLOAT:
            self.advance()
            return float(token.text)
        elif token.type == TokenType.STRING:
            self.advance()
            return token.text[1:-1]  # Remove quotes
        elif token.text == 'true':
            self.advance()
            return True
        elif token.text == 'false':
            self.advance()
            return False
        
        raise Exception(f"Expected literal, got {token.type}")

    
    def parse_declaration(self) -> Node:
        """Parse any top-level declaration"""
        if self.match(TokenType.TYPE):
            return self.parse_type_declaration()
        elif self.match(TokenType.FN):
            return self.parse_function()
        elif self.match([TokenType.LET, TokenType.CONST]):
            return self.parse_variable()
        elif self.match([TokenType.CPP, TokenType.PYTHON, TokenType.JAVA]):
            return self.parse_language_block()
        elif self.match(TokenType.GUI):
            return self.parse_gui_block()
        else:
            raise Exception(f"Expected declaration, got {self.peek().type}")
    
    def parse_type_declaration(self) -> TypeDecl:
        """Parse a type declaration"""
        name = self.consume(TokenType.IDENTIFIER, "Expected type name").text
        
        # Create wall section for this type
        wall_section = self.type_system.define_type(name, TypeKind.COMPOSITE)
        type_params = []
        
        # Handle generic parameters
        if self.match(TokenType.LT):
            while not self.match(TokenType.GT):
                type_params.append(self.consume(TokenType.IDENTIFIER, "Expected type parameter name").lexeme)
                self.match(TokenType.COMMA)
        
        self.consume(TokenType.LBRACE, "Expected '{' after type name")
        
        fields = []
        methods = []
        
        while not self.match(TokenType.RBRACE):
            if self.match(TokenType.FN):
                methods.append(self.parse_function())
            else:
                fields.append(self.parse_variable())
        
        return TypeDecl(
            type=NodeType.TYPE,
            location=self.previous().location,
            name=name,
            fields=fields,
            methods=methods,
            type_params=type_params
        )
    
    def parse_function(self) -> Function:
        """Parse a function declaration"""
        name = self.consume(TokenType.IDENTIFIER, "Expected function name").lexeme
        is_async = self.previous().type == TokenType.ASYNC
        
        self.consume(TokenType.LPAREN, "Expected '(' after function name")
        params = []
        
        if not self.check(TokenType.RPAREN):
            while True:
                param_name = self.consume(TokenType.IDENTIFIER, "Expected parameter name").lexeme
                self.consume(TokenType.COLON, "Expected ':' after parameter name")
                param_type = self.parse_type()
                params.append(Variable(
                    type=NodeType.VARIABLE,
                    location=self.previous().location,
                    name=param_name,
                    type=param_type
                ))
                
                if not self.match(TokenType.COMMA):
                    break
        
        self.consume(TokenType.RPAREN, "Expected ')' after parameters")
        
        # Return type
        return_type = Type(name="void")
        if self.match(TokenType.ARROW):
            return_type = self.parse_type()
        
        # Function body
        body = self.parse_block()
        
        return Function(
            type=NodeType.FUNCTION,
            location=self.previous().location,
            name=name,
            params=params,
            return_type=return_type,
            body=body,
            is_async=is_async
        )
    
    def parse_block(self) -> Block:
        """Parse a block of statements"""
        statements = []
        
        self.consume(TokenType.LBRACE, "Expected '{' before block")
        
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            statements.append(self.parse_statement())
            
        self.consume(TokenType.RBRACE, "Expected '}' after block")
        
        return Block(
            type=NodeType.BLOCK,
            location=self.previous().location,
            statements=statements
        )
    
    def parse_statement(self) -> Node:
        """Parse any statement"""
        if self.match(TokenType.IF):
            return self.parse_if_statement()
        elif self.match(TokenType.WHILE):
            return self.parse_while_statement()
        elif self.match(TokenType.FOR):
            return self.parse_for_statement()
        elif self.match(TokenType.MATCH):
            return self.parse_match_statement()
        elif self.match(TokenType.RETURN):
            return self.parse_return_statement()
        elif self.match(TokenType.TRY):
            return self.parse_try_statement()
        elif self.match([TokenType.LET, TokenType.CONST]):
            return self.parse_variable()
        else:
            return self.parse_expression_statement()
    
    def parse_expression(self) -> Node:
        """Parse any expression"""
        return self.parse_assignment()
    
    def parse_assignment(self) -> Node:
        """Parse assignment expressions"""
        expr = self.parse_logical_or()
        
        if self.match(TokenType.ASSIGN):
            value = self.parse_assignment()
            if isinstance(expr, (Identifier, Access)):
                return BinaryOp(
                    type=NodeType.BINARY,
                    location=self.previous().location,
                    op="=",
                    left=expr,
                    right=value
                )
            raise Exception("Invalid assignment target")
        
        return expr
    
    def parse_type(self) -> Type:
        """Parse a type expression"""
        base = self.consume(TokenType.IDENTIFIER, "Expected type name").lexeme
        params = []
        
        if self.match(TokenType.LT):
            while not self.match(TokenType.GT):
                params.append(self.parse_type())
                self.match(TokenType.COMMA)
        
        type_ = Type(name=base, params=params)
        
        if self.match(TokenType.QMARK):
            type_.is_optional = True
            
        return type_
    
    def synchronize(self):
        """Recover from parsing errors"""
        self.advance()
        
        while not self.is_at_end():
            if self.previous().type == TokenType.NEWLINE:
                return
            
            if self.peek().type in [
                TokenType.TYPE,
                TokenType.FN,
                TokenType.LET,
                TokenType.CONST,
                TokenType.IF,
                TokenType.WHILE,
                TokenType.FOR,
                TokenType.RETURN
            ]:
                return
            
            self.advance()
    
    def match(self, types) -> bool:
        """Match and consume a token if it matches any of the given types"""
        if not isinstance(types, list):
            types = [types]
            
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False
    
    def check(self, type_: TokenType) -> bool:
        """Check if current token is of given type"""
        if self.is_at_end():
            return False
        return self.peek().type == type_
    
    def advance(self) -> Token:
        """Advance to next token"""
        if not self.is_at_end():
            self.current += 1
        return self.previous()
    
    def is_at_end(self) -> bool:
        """Check if we've reached end of tokens"""
        return self.peek().type == TokenType.EOF
    
    def peek(self) -> Token:
        """Get current token"""
        return self.tokens[self.current]
    
    def previous(self) -> Token:
        """Get previous token"""
        return self.tokens[self.current - 1]
    
    def consume(self, type_: TokenType, message: str) -> Token:
        """Consume and return token if it matches, otherwise error"""
        if self.check(type_):
            return self.advance()
        raise Exception(f"{message} at {self.peek().location}")