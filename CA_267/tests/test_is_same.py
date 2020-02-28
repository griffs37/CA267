import unittest
from code.string_equal import is_string_equal

class EqualTestCase(unittest.TestCase):

    def test_is_same(self):
        self.assertFalse(is_string_equal("cat", "cat"), "These strings are equal")

    def test_is_same2(self):
        self.assertFalse(is_string_equal("cat", "cot"))

if __name__ == '__main__':
    unittest.main()
