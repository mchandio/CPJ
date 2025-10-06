"""
CPJ Language Feature Tests

This module tests CPJ's language features including:
- Indentation handling
- Mixed language syntax
- Type inference
- Cross-language type mapping
"""
import unittest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from cpj_parser import IndentAwareParser
from cpj_runtime import CPJRuntime


class TestCPJLanguageFeatures(unittest.TestCase):
    def setUp(self):
        self.parser = IndentAwareParser()
        self.runtime = CPJRuntime()

    def test_python_style_indentation(self):
        """Test Python-style indentation parsing"""
        code = """
def calculate(x: int) -> int:
    if x > 0:
        result = x * 2
        if result > 10:
            return result
        else:
            return x
    return 0
"""
        tree = self.parser.parse_code(code)
        self.assertIsNotNone(tree)
        # Verify indentation levels were preserved
        parsed = str(tree)
        self.assertIn("if x > 0", parsed)
        self.assertIn("if result > 10", parsed)

    def test_cpp_style_blocks(self):
        """Test C++-style block parsing"""
        code = """
class Calculator {
    private:
        int value;
    
    public:
        Calculator(int v) {
            this->value = v;
        }
        
        int calculate() {
            return value * 2;
        }
};
"""
        tree = self.parser.parse_code(code)
        self.assertIsNotNone(tree)
        # Verify C++ syntax was preserved
        parsed = str(tree)
        self.assertIn("private:", parsed)
        self.assertIn("public:", parsed)
        self.assertIn("this->value", parsed)

    def test_java_style_methods(self):
        """Test Java-style method parsing"""
        code = """
public class DataProcessor {
    private String data;
    
    public DataProcessor(String initialData) {
        this.data = initialData;
    }
    
    public String processData() throws Exception {
        if (data == null) {
            throw new Exception("No data");
        }
        return data.toUpperCase();
    }
}
"""
        tree = self.parser.parse_code(code)
        self.assertIsNotNone(tree)
        # Verify Java syntax was preserved
        parsed = str(tree)
        self.assertIn("public class", parsed)
        self.assertIn("throws Exception", parsed)
        self.assertIn("toUpperCase()", parsed)

    def test_mixed_language_syntax(self):
        """Test mixing syntax from different languages"""
        code = """
def process_data(data: List[str]) -> Dict[str, Any]:
    # Python-style function with type hints
    result = {}
    
    class DataProcessor {
        // C++-style class
        private:
            vector<string> items;
        
        public:
            void add(string item) {
                items.push_back(item);
            }
    };
    
    public interface Processor {
        // Java-style interface
        String process(String input);
    }
    
    return result
"""
        tree = self.parser.parse_code(code)
        self.assertIsNotNone(tree)
        # Verify mixed syntax was preserved
        parsed = str(tree)
        self.assertIn("def process_data", parsed)
        self.assertIn("vector<string>", parsed)
        self.assertIn("public interface", parsed)

    def test_type_inference(self):
        """Test type inference across languages"""
        code = """
def calculate_stats(numbers):  # Python-style no type hints
    sum = 0.0  # Should infer double/float
    count = 0  # Should infer int
    
    for num in numbers:
        sum += num
        count += 1
    
    return {
        "average": sum / count,
        "count": count
    }
"""
        tree = self.parser.parse_code(code)
        self.assertIsNotNone(tree)
        # Verify type inference
        types = self.runtime.infer_types(tree)
        self.assertEqual(types["sum"], "float")
        self.assertEqual(types["count"], "int")

    def test_cross_language_types(self):
        """Test type mapping between languages"""
        mappings = {
            "python_int": ["int32_t", "Integer"],
            "python_str": ["std::string", "String"],
            "python_list": ["std::vector", "ArrayList"],
            "python_dict": ["std::map", "HashMap"],
            "python_float": ["double", "Double"],
            "python_bool": ["bool", "Boolean"]
        }
        
        for py_type, [cpp_type, java_type] in mappings.items():
            mapped_cpp = self.runtime.map_type(py_type, "cpp")
            mapped_java = self.runtime.map_type(py_type, "java")
            
            self.assertEqual(mapped_cpp, cpp_type)
            self.assertEqual(mapped_java, java_type)


if __name__ == '__main__':
    unittest.main()