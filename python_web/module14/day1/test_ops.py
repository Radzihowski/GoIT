import unittest

from ops import add, sub, mul, div

class TestExamples(unittest.TestCase):
    @classmethod
    def setup(cls):
        print("Start before all tests")

    @classmethod
    def tearDownClass(cls):
        print("Start after all tests")

    def setUp(self):
        print("Start before each test")

    def tearDown(self):
        print("Start after each test")

    def test_add(self):
        print("Add functional test")
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        print("Sub functional test")
        self.assertEqual(sub(2, 3), -1)

    def test_mul(self):
        print("Mul functional test")
        self.assertEqual(mul(2, 3), 6)

    def test_div(self):
        print("Div functional test")
        self.assertEqual(div(6, 3), 2)

if __name__ == "__main__":
    unittest.main()