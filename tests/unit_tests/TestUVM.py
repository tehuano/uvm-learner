#!/usr/bin/python2.7
"""
high level support for doing this and that.
"""
import unittest
import test_model_tests

class TestUVM(unittest.TestCase):
    """
    high level support for doing this and that.
    """
    def test_build(self):
        """
        high level support for doing this and that.
        """
        self.assertEqual(test_model_tests.run('model_sim_build'),True)
    
    def test_sim_200ns(self):
        """
        high level support for doing this and that.
        """
        self.assertEqual(test_model_tests.run('run_adder_200ns'),True)
        #self.assertEqual(test_model_tests.run('model_sim_build'),True)

if __name__ == '__main__':
    unittest.main()
