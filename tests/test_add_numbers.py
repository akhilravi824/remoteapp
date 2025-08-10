import unittest

from add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_add_multiple_numbers(self):
        self.assertEqual(add_numbers(1, 2, 3, 4), 10)

    def test_add_no_numbers(self):
        self.assertEqual(add_numbers(), 0)


if __name__ == "__main__":
    unittest.main()
