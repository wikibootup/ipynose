import unittest
from ipynose import ipynose


class TestIpynose(unittest.TestCase):
    def setUp(self):
        self.TRUE_TEST_PATH = "tests/test_true.py"
        self.FALSE_TEST_PATH = "tests/test_false.py"

    def test_all_nose_results(self):
        """
        skip because it causes recursive testing
        """
        pass

    def test_nose_result_with_true_test(self):
        self.assertTrue("OK" in ipynose.nose_result(self.TRUE_TEST_PATH))

    def test_nose_result_with_false_test(self):
        self.assertTrue("FAILED" in ipynose.nose_result(self.FALSE_TEST_PATH))
