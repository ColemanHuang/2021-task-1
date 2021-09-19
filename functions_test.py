import unittest
from functions import first_level
from functions import second_level
from functions import last_level


class MyTestCase(unittest.TestCase):
    counts = {'break': 7, 'case': 5, 'default': 2, 'double': 1,
              'else': 4, 'elseif': 3, 'if': 4, 'int': 2,
              'long': 1, 'return': 1, 'switch': 2}
    expected2 = (2, [3, 2])
    expected3 = (2, 2)

    def test_first_level(self):
        self.assertEqual(first_level(), self.counts)

    def test_second_level(self):
        self.assertEqual(second_level(self.counts), self.expected2)

    def test_last_level(self):
        self.assertEqual(last_level(), self.expected3)


if __name__ == '__main__':
    unittest.main()
