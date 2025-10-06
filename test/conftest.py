"""Common test configuration and utilities."""
import os
import sys
import pytest
from typing import Any, Generator, Optional
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import CPJ modules
from CPJLexer import CPJLexer
from CPJParser import CPJParser
from cpj_type_system import TypeSystem
from antlr4 import InputStream

class TestConfig:
    """Test configuration and utilities."""
    
    @staticmethod
    def get_test_file_path(filename: str) -> Path:
        """Get path to a test file in the test/data directory."""
        return PROJECT_ROOT / "test" / "data" / filename
    
    @staticmethod
    def read_test_file(filename: str) -> str:
        """Read contents of a test file."""
        path = TestConfig.get_test_file_path(filename)
        with open(path, "r") as f:
            return f.read()

@pytest.fixture
def lexer() -> CPJLexer:
    """Fixture providing a CPJ lexer instance."""
    input_stream = InputStream("")
    return CPJLexer(input_stream)

@pytest.fixture
def parser(lexer) -> CPJParser:
    """Fixture providing a CPJ parser instance."""
    return CPJParser(lexer)

@pytest.fixture
def type_system() -> TypeSystem:
    """Fixture providing a CPJ type system instance."""
    return TypeSystem()

@pytest.fixture
def setup_test_files() -> Generator[None, None, None]:
    """Fixture to set up and clean up test files."""
    # Create test data directory if it doesn't exist
    test_data_dir = PROJECT_ROOT / "test" / "data"
    test_data_dir.mkdir(parents=True, exist_ok=True)
    
    yield
    
    # Clean up test files after test
    for file in test_data_dir.glob("*.cpj"):
        file.unlink()
        
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "lexer: mark test as lexer test")
    config.addinivalue_line("markers", "parser: mark test as parser test")
    config.addinivalue_line("markers", "type_system: mark test as type system test")
    config.addinivalue_line("markers", "integration: mark test as integration test")
    config.addinivalue_line("markers", "gui: mark test as GUI test")
    config.addinivalue_line("markers", "house: mark test as house feature test")
    config.addinivalue_line("markers", "async_test: mark test as async test")