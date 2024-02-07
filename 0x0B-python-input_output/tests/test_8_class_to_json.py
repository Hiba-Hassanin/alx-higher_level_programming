import unittest
from io import StringIO
from unittest.mock import patch
class_to_json = __import__('8-class_to_json').class_to_json

class TestClassToJson(unittest.TestCase):
    """Define unittests for class_to_json function"""

    def test_simple_class(self):
        """Test class with simple attributes"""
        class MyClass:
            """Simple class"""
            def __init__(self, name):
                self.name = name
                self.number = 89

        obj = MyClass("John")
        expected = {'name': 'John', 'number': 89}
        self.assertEqual(class_to_json(obj), expected)

    def test_class_with_methods(self):
        """Test class with methods"""
        class MyClass:
            """Class with methods"""
            score = 0
            def __init__(self, name):
                self.__name = name
                self.number = 4
                self.is_team_red = (self.number % 2) == 0
            def win(self):
                self.score += 1
            def lose(self):
                self.score -= 1

        obj = MyClass("John")
        obj.win()
        expected = {'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
        self.assertEqual(class_to_json(obj), expected)

if __name__ == "__main__":
    unittest.main()
