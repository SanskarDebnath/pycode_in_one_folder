class Employee:
    Employee_depertment = 4
    def printdetails(self):
        #What is self?
        #self means that the current object which we are / will use in the program

        return f"Employee Name is {self.name}. Employee salary is {self.sal}"

        """
        In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside braces. The expressions are replaced with their values."""


obj1 = Employee()
obj2 = Employee()

obj1.name = "ABCD"
obj1.sal = 45000

obj2.name = "EFGH"
obj2.sal = 65000



print(obj2.printdetails()) #output : Employee Name is EFGH. Employee salary is 65000
print(obj1.printdetails()) #output : Employee Name is ABCD. Employee salary is 45000