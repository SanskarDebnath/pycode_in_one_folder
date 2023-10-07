class Hierarchy:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_values(self, name, price):
        self.name = name
        self.__price = price

    def show_details(self):
        print(f"{self.name}, {self.__price}")

class Child77(Hierarchy):
    def __init__(self, name, price):
        super().__init__(name, price)

    def show_details44(self):
        print(self.name)


ins = Child77("s", 44)
ins.show_details()
