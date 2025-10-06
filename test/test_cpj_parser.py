"""Test suite for CPJ parser functionality."""
import pytest
from antlr4 import InputStream, CommonTokenStream
from cpj_lexer import CPJLexer
from cpj_parser import CPJParser, Node, NodeType
from typing import Optional, List

@pytest.mark.parser
class TestCPJParser:
    """Test cases for the CPJ parser."""
    
    def parse_code(self, source: str) -> Optional[Node]:
        """Helper to parse source code into AST."""
        input_stream = InputStream(source)
        lexer = CPJLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = CPJParser(token_stream)
        return parser.parse()
        
    def test_basic_function_parsing(self, parser):
        """Test parsing of basic function definitions."""
        source = """
        function test(x: int, y: str) -> bool {
            return x > 0 and y != ""
        }
        """
        ast = self.parse_code(source)
        assert ast is not None
        assert ast.type == NodeType.PROGRAM
        assert len(ast.children) == 1
        func_node = ast.children[0]
        assert func_node.type == NodeType.FUNCTION
        assert func_node.name == "test"
        
    def test_expression_parsing(self, parser):
        """Test parsing of various expression types."""
        expressions = [
            "1 + 2 * 3",
            "x and y or z",
            "(a + b) * (c - d)",
            "func(x, y, z)",
            "obj.method()",
            "[1, 2, 3]",
            "{'a': 1, 'b': 2}"
        ]
        
        for expr in expressions:
            ast = self.parse_code(expr)
            assert ast is not None
            assert ast.type == NodeType.PROGRAM
            assert len(ast.children) == 1
            assert ast.children[0].type == NodeType.EXPRESSION
            
    def test_control_flow_parsing(self, parser):
        """Test parsing of control flow statements."""
        source = """
        function test(x: int) {
            if x > 0 {
                while x > 0 {
                    x = x - 1
                }
            } else {
                for i in range(10) {
                    x = x + i
                }
            }
        }
        """
        ast = self.parse_code(source)
        assert ast is not None
        assert ast.find_first(NodeType.IF) is not None
        assert ast.find_first(NodeType.WHILE) is not None
        assert ast.find_first(NodeType.FOR) is not None
        
    def test_type_annotations(self, parser):
        """Test parsing of type annotations."""
        source = """
        type Point {
            x: int
            y: int
        }
        
        function distance(p1: Point, p2: Point) -> float {
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            return sqrt(dx * dx + dy * dy)
        }
        """
        ast = self.parse_code(source)
        assert ast is not None
        type_def = ast.find_first(NodeType.TYPE_DEF)
        assert type_def is not None
        assert type_def.name == "Point"
        assert len(type_def.fields) == 2
        
    def test_error_recovery(self, parser):
        """Test parser error recovery."""
        invalid_sources = [
            "function test( {",  # Missing param closing )
            "if x > 0 {",      # Missing closing brace
            "x = ",            # Missing expression
            "function() { }"   # Missing function name
        ]
        
        for source in invalid_sources:
            with pytest.raises(Exception):
                self.parse_code(source)
                
    def test_house_features(self, parser):
        """Test parsing of house-specific features."""
        source = """
        house MyHouse {
            room LivingRoom {
                width: 20
                length: 30
                windows: 4
            }
            
            wall North {
                length: 20
                height: 10
                material: "brick"
            }
        }
        """
        ast = self.parse_code(source)
        assert ast is not None
        house_node = ast.find_first(NodeType.HOUSE)
        assert house_node is not None
        assert house_node.name == "MyHouse"
        assert len(house_node.children) == 2
        
    def test_comments_handling(self, parser):
        """Test proper handling of comments."""
        source = """
        // Single line comment
        function test() {
            /* Multi-line
               comment */
            x = 1  // End of line comment
        }
        """
        ast = self.parse_code(source)
        assert ast is not None
        # Comments should be ignored in AST
        assert ast.find_all(NodeType.COMMENT) == []
        
    @pytest.mark.parametrize("source,expected_error", [
        ("function {}", "Missing function name"),
        ("if", "Missing condition"),
        ("while", "Missing condition"),
        ("x = ;", "Missing expression"),
    ])
    def test_syntax_errors(self, parser, source: str, expected_error: str):
        """Test specific syntax error cases."""
        with pytest.raises(Exception) as exc_info:
            self.parse_code(source)
        assert expected_error.lower() in str(exc_info.value).lower()
        
    def test_nested_structures(self, parser):
        """Test parsing of deeply nested structures."""
        source = """
        function outer() {
            function middle() {
                function inner() {
                    if x > 0 {
                        while y > 0 {
                            for i in range(10) {
                                x = x + i
                            }
                        }
                    }
                }
            }
        }
        """
        ast = self.parse_code(source)
        assert ast is not None
        # Verify nesting depth
        outer = ast.find_first(lambda n: n.type == NodeType.FUNCTION and n.name == "outer")
        assert outer is not None
        middle = outer.find_first(lambda n: n.type == NodeType.FUNCTION and n.name == "middle")
        assert middle is not None
        inner = middle.find_first(lambda n: n.type == NodeType.FUNCTION and n.name == "inner")
        assert inner is not None