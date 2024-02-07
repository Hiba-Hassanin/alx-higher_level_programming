import unittest


to_json_string = __import__('3-to_json_string').to_json_string


class TestToJsonString(unittest.TestCase):
    """Define unittests for to_json_string function"""

    def test_list(self):
        """Test JSON representation of a list"""
        my_list = [1, 2, 3]
        self.assertEqual(to_json_string(my_list), "[1, 2, 3]")

    def test_dict(self):
        """Test JSON representation of a dictionary"""

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
        expected_json = '{"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"], "is_active": true, "info": {"age": 36, "average": 3.14}}'
        self.assertEqual(to_json_string(my_dict), expected_json)

    def test_set(self):
        """Test JSON representation of a set"""
        my_set = {132, 3}
        with self.assertRaises(TypeError) as context:
            to_json_string(my_set)
        self.assertEqual(str(context.exception), "{3, 132} is not JSON serializable")

if __name__ == "__main__":
    unittest.main()
