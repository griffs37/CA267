import unittest

from code.almost import is_almost_equal

class AlmostEqTestCase(unittest.TestCase):

        def test_one(self):
            self.assertAlmostEqual(1.67, 1.667, 2)


        def test_two(self):
            self.assertAlmostNotEqual(1.67, 1.87, 2)



if __name__ == '__main__':
    unittest.main()
