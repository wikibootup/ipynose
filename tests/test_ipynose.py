import unittest
from .. import ipynose

class TestIpynose(unittest.TestCase):
    def setUp(self):
        self.TRUETESTPATH = "tests/test_true.py"
        self.FALSETESTPATH = "tests/test_false.py"

    def test_all_test_results(self):
        """
        skip because it causes recursive testing
        """
        pass

    def test_test_result_with_true_test(self):
        self.assertTrue("OK" in ipynose.test_result(self.TRUETESTPATH))

    def test_test_result_with_false_test(self):
        self.assertTrue("FAILED" in ipynose.test_result(self.FALSETESTPATH))
