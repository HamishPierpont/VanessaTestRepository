import unittest
from vanessatestrepository.src.math import add, multiply, subtract


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertEqual("Python good!", add("Python ", "good!"))
        with self.assertRaises(TypeError):
            add(1)  # Missing a positional argument

    def test_multiply(self):
        self.assertEqual(12, multiply(4, 3))
        self.assertEqual(0, multiply(20000000000000, 0))
        with self.assertRaises(TypeError):
            multiply(1, 1, 1, 1, 1, 1, 1, 1) # Too many positional arguments

    def test_subtract(self):
        self.assertEqual(0, subtract(2, 2))
        self.assertNotEqual(0, subtract(5, 0))
        with self.assertRaises(TypeError):
            subtract() # Missing two positional arguments


def run_tests():
    unittest.main()


if __name__ == "__main__":
    run_tests()
