class House:
    def __init__(self):
        print("New house was builded")

    def GetName(self):
        print(self.name)

    def SetName(self, name):
        if (type(name) is not str):
            raise Exception

        self.name = name

    def GetPrice(self):
        print(50 + " CHF")