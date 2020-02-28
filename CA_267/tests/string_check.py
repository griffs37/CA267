import unittest
from code.string_check import check1

class StringEqual(unittest.TestCase):

    def check_string(self):
        self.assertTrue(check1("cat", "cat"))

    def check_string2(self):
        self.assertFalse(check1("cat", "cot"))


if __name__ == '__main__':
    unittest.main()
