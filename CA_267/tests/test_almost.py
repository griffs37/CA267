import unittest
from code.almost import is_almost_equal

class AlmostEqualTestCase(unittest.TestCase):

    def test_is_almost_equal(self):
        self.assertAlmostEqual(is_almost_equal(1.66, 1.67), 7)

    def test_is_dfhfh(self):
        self.assertNotAlmostEqual(is_almost_equal(1.66, 1.96), 7)

if __name__ == '__main__':
    unittest.main()
