class House:
    def __init__(self):
        self.name = None
        print("New house was builded")

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        if type(name) is not str:
            raise Exception

        self.name = name

    def get_price(self):
        print(str(50) + " CHF")