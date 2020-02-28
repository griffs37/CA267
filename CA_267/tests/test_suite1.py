import unittest
from test_long_message import LongMessageTestcase
from testRevString import TestIfReverse

def my_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LongMessageTestcase))
    suite.addTest(unittest.makeSuite(TestIfReverse))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()
