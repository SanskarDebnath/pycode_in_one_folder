# c--- calling base class constructor from child constructor ------
class Base:
    def __init__(self, id):
        self.__id = id

    def getId(self): # public getter
        return self.__id

class Child(Base):
    def __init__(self, name, id):
        self.name = name
        # self.__id = id # it creates a local datamember with same name
        super().__init__(id)  # call to parent class constructor

    def show(self):
        print('Name = ', self.name, ' id = ', self.getId())


ob = Child('Ani', 1)
ob.show()

# --- multiple inheritance ---
class Base1:
    def __init__(self, id):
        print('in base 1')
        self.__id = id

    def getId(self): # public getter
        return self.__id
    
class Base2:
    def __init__(self, k):
        print('in base 2')
        self.__key = k

    def getKey(self): # public getter
        return self.__key

class Derived(Base2, Base1):
    def __init__(self, name, id, key):
        self.name = name
        # super().__init__(25)  --> calls only base2 constructor
        Base1.__init__(self, id)
        Base2.__init__(self, key)

    def show(self):
        print('Name = ', self.name, ' id = ', self.getId(), ' key = ', self.getKey())

co = Derived('kiki', 2, 56)
co.show()