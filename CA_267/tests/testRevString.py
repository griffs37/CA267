import unittest
from code.reverse import reverse_string

class TestIfReverse(unittest.TestCase):

    def test_one(self):
        self.assertEqual("god", reverse_string("dog"))

    def test_two(self):
        self.assertNotEqual("steve", reverse_string("jeremy"))

    # Wont work because wrong data type is returned; nonBool
    #def test_three(self):
        #self.assertTrue("stephen", reverse_string("nehpets"))

    #def test_four(self):
        #self.assertFalse("kendrick", "kendrick")

    
if __name__ == '__main__':
    unittest.main()

# reverse_string("cole"))                         
    
