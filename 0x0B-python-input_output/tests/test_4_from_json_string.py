import unittest


from_json_string = __import__('4-from_json_string').from_json_string


class TestFromJsonString(unittest.TestCase):
    """Define unittests for from_json_string function"""

    def test_list(self):
        """Test conversion of JSON string to list"""
        s_my_list = "[1, 2, 3]"
        self.assertEqual(from_json_string(s_my_list), [1, 2, 3])

    def test_dict(self):
        """Test conversion of JSON string to dictionary"""
        s_my_dict = '''
        {
            "id": 12,
            "name": "John",
            "places": ["San Francisco", "Tokyo"],
            "is_active": true,
            "info": {
                "age": 36,
                "average": 3.14
            }
        }
        '''
        expected_dict = {
            "id": 12,
            "name": "John",
            "places": ["San Francisco", "Tokyo"],
            "is_active": True,
            "info": {
                "age": 36,
                "average": 3.14
            }
        }
        self.assertEqual(from_json_string(s_my_dict), expected_dict)

    def test_invalid_json(self):
        """Test handling of invalid JSON string"""
        s_invalid_json = '{"is_active": true, 12 }'
        with self.assertRaises(ValueError) as context:
            from_json_string(s_invalid_json)
        self.assertEqual(str(context.exception), "Expecting property name enclosed in double quotes: line 1 column 25 (char 25)")

if __name__ == "__main__":
    unittest.main()
