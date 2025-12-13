import unittest
from contextlib import redirect_stdout
from io import StringIO

from src.house import House
from src.house_exception import HouseException


class TestHouse(unittest.TestCase):
    def test_create(self):
        house = House()

        self.assertIsInstance(house, House)

    def test_raise_name_not_str(self):
        house = House()

        self.assertRaises(HouseException, house.set_name, 1234)

    def test_get_name(self):
        house = House()
        house.set_name("Hallo")

        buffer = StringIO()
        with redirect_stdout(buffer):
            house.get_name()

        output = buffer.getvalue().strip()
        self.assertEqual(output, "Hallo")

    def test_get_price(self):
        house = House()

        buffer = StringIO()
        with redirect_stdout(buffer):
            house.get_price()

        output = buffer.getvalue().strip()
        self.assertEqual(output, "50 CHF")


if __name__ == '__main__':
    unittest.main()