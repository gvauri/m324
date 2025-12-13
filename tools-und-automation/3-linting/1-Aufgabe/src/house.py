from src.house_exception import HouseException

class House:
    def __init__(self):
        print("New house was builded")

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        if (type(name) is not str):
            raise HouseException

        self.name = name

    def get_price(self):
        print(str(50) + " CHF")