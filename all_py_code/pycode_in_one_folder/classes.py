#print("starting of classes in python")

class student:
    pass


sanskar = student()
sanskar2 = student()



#print(sanskar, sanskar2)

#<__main__.student object at 0x0000027D3840DC90> <__main__.student object at 0x0000027D3840DD50> this means that this two objects are taking 

#two differnt memory locations

#what if i insert the Values in it?

sanskar.name = "sanskar debnath"
sanskar.branch = "CSE"
sanskar.language = "python"
#print(sanskar.name) 

#thats how we can print the object that contains any data

#print(sanskar.name, sanskar2.name) #it will create an error

"""
AttributeError: 'student' object has no attribute 'name'

"""

#we can store the lists in the objects eg.

sanskar.subjects = ["Pyhton", "PHP", "python"]

#print(sanskar.subjects)


#example of class property

class Employee:
    Employee_depertment = 4
    pass

obj1 = Employee()

obj2 = Employee()

obj1.name = "ABCD"
obj1.sal = 45000

obj2.name = "EFGH"
obj2.sal = 65000

print(Employee.Employee_depertment) #result = 4 <access through class>

print(obj1.Employee_depertment) #result = 4 <access through objects/instances>

print(obj2.Employee_depertment) #result = 4 <access through objects/instances>

#changing the value

obj1.Employee_depertment = 45
print(obj1.Employee_depertment) #result = 45

#if i change the value then?

Employee.Employee_depertment = 96
print(Employee.__dict__)

"""
__dict__
return the dictionary only
{'__module__': '__main__', 'Employee_depertment': 96, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

"""

print(Employee.Employee_depertment) #result = 96 {we can change the class variable value using class name only}

