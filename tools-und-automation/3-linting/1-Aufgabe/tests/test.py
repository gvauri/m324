import unittest
from ..src.house import *


class TestHouse(unittest.TestCase):
    def test_create(self):
        house = House()

        self.assertIsInstance(house, House)

    def test_set_name(self):
        house = House()
        house.set_name("villa")

        print(house)
        self.assertEqual(house.get_name(), "villa")


if __name__ == '__main__':
    unittest.main()