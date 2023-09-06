print("starting of classes in python")
class student:
    pass
sanskar = student()
sanskar2 = student()
print(sanskar, sanskar2) #<__main__.student object at 0x0000027D3840DC90> <__main__.student object at 0x0000027D3840DD50> this means that this two objects are taking 
#two differnt memory locations
#what if i insert the Values in it?
sanskar.name = "sanskar debnath"
sanskar.branch = "CSE"
sanskar.language = "python"
print(sanskar.name) #thats how we can print the object that contains any data

