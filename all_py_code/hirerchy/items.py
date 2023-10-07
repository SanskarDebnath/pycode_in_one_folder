#Example of Hirerchical Inheritance 
class item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    

class Mobile (item):
    def __init__ (self, quantity, price, cam, rom):
        super().__init__(quantity, price)
        self.cam = cam
        self.rom = rom
    def showdetailsmobile (self):
        print(f"{self.rom}, {self.cam}")

class Book (item):
    def __init__ (self, quantity, author, Publisher, price):
        super().__init__(quantity, price)
        self.au = author
        self.pub = Publisher
        
    def showdetailsbook (self):
        print(f"{self.au}, {self.pub}")

class Laptop (item):
    def __init__ (self, quantity, price, Ram, Processor):
        super().__init__(quantity, price)
        self.ra = Ram
        self.pro = Processor
        
    def showdetailslap (self):
        print(f"{self.ra}, {self.pro}")
        print(f"{self.quantity}, {self.price}")


ins = Laptop("4", "44", "55", "6")
ins.showdetailslap()