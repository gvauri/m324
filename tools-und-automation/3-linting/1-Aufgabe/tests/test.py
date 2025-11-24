import unittest
from src.house import *


class TestHouse(unittest.TestCase):
    def test_create(self):
        house = House()

        self.assertIsInstance(house, House)


if __name__ == '__main__':
    unittest.main()