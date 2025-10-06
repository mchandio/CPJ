from enum import Enum, auto

class NodeType(Enum):
    # Core structure
    HOUSE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    MATERIAL = auto()
    BLOCK = auto()
    LANGUAGE_BLOCK = auto()
    LITERAL = auto()
    VARIABLE = auto()
    
    # Features
    WINDOW = auto()
    DOOR = auto()
    LIGHT = auto()
    REST = auto()    # Process suspension and async operations
    
    # AI components
    AI = auto()
    NEURAL_NETWORK = auto()
    ML_MODEL = auto()
    AGENT = auto()
    SENSOR = auto()
    ACTUATOR = auto()
    
    # AI support types
    MEMORY = auto()
    LAYER = auto()
    EXPERIENCE = auto()
    TRAINING_DATA = auto()
    INFERENCE = auto()
    
    # AI operations
    LEARN = auto()
    PREDICT = auto()
    TRAIN = auto()
    EVALUATE = auto()

class AccessLevel(Enum):
    PUBLIC = auto()
    PROTECTED = auto()
    PRIVATE = auto()

class TokenType(Enum):
    # House structure tokens
    PUBLIC = auto()
    PRIVATE = auto()
    FOUNDATION = auto()
    ROOM = auto()
    BLUEPRINT = auto()
    UTILITY = auto()
    
    # Language features
    FUNCTION = auto()
    TYPE = auto()
    MEMORY = auto()
    CPP_BLOCK = auto()
    PYTHON_BLOCK = auto()
    JAVA_BLOCK = auto()
    
    # Types
    INT = auto()
    FLOAT = auto()
    STRING_TYPE = auto()
    BOOL = auto()
    VOID = auto()
    
    # Basic tokens
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    LBRACE = auto()
    RBRACE = auto()
    LPAREN = auto()
    RPAREN = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COLON = auto()
    COMMA = auto()
    ARROW = auto()
    EQUAL = auto()
    SEMI = auto()
    DOT = auto()
    
    # Special tokens
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()
    PREPROCESSOR = auto()
    STRING_INTERP_START = auto()
    STRING_INTERP_END = auto()
    NEWLINE = auto()
    ERROR = auto()
    LBRACK = auto()  # [
    RBRACK = auto()  # ]
    PLUS = auto()    # +
    MINUS = auto()   # -
    STAR = auto()    # *
    SLASH = auto()   # /
    PERCENT = auto() # %
    HAT = auto()     # ^
    LT = auto()      # <
    GT = auto()      # >
    BANG = auto()    # !
    AND = auto()     # &
    OR = auto()      # |
    QMARK = auto()   # ?
    AT = auto()      # @
    
    # House features
    WINDOW = auto()
    DOOR = auto()
    LIGHT = auto()