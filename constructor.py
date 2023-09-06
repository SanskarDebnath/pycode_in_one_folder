class Employee:
    Employee_depertment = 4

    def __init__(self,aname,asal):
        self.name = aname
        self.sal = asal



    def printdetails(self):
        return f"Employee Name is {self.name}. Employee salary is {self.sal}"


#the way we assign values in class it is called an Instructor


obj1 = Employee("Sanskar Debnath", 65000)
obj2 = Employee("ddn", 3211)

# what if we now print the instances

#print(Employee.printdetails()) 
# Error: Employee() takes no arguments

#now what should i do?

#i need to create an __init__ function in the classs and pass the arguments as value

#now print the result

print(obj1.name, obj1.sal)

