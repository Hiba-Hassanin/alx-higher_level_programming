import unittest
from io import StringIO
from unittest.mock import patch
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

class TestSaveToJsonFile(unittest.TestCase):
    """Define unittests for save_to_json_file function"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_list(self, mock_stdout):
        """Test saving list to JSON file"""
        my_list = [1, 2, 3]
        filename = "my_list.json"
        save_to_json_file(my_list, filename)
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), '[1, 2, 3]\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_dict(self, mock_stdout):
        """Test saving dictionary to JSON file"""
        my_dict = {
            'id': 12,
            'name': "John",
            'places': ["San Francisco", "Tokyo"],
            'is_active': True,
            'info': {
                'age': 36,
                'average': 3.14
            }
        }
        filename = "my_dict.json"
        save_to_json_file(my_dict, filename)
        with open(filename, 'r') as f:
            self.assertEqual(f.read(), '{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_json(self, mock_stdout):
        """Test handling of invalid JSON serializable object"""
        my_set = {132, 3}
        filename = "my_set.json"
        with self.assertRaises(TypeError) as context:
            save_to_json_file(my_set, filename)
        self.assertEqual(str(context.exception), "{3, 132} is not JSON serializable")

if __name__ == "__main__":
    unittest.main()
