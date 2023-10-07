class inheritence:
  def __init__ (self, name, id):
    self.name = name
    self.id = id
    self.__private = "private member"
  def show_details(self):
    print(f"The name is {self.name} and id is {self.id}")
    #without f string the output will be  print(f"The name is {self.name} #and id is {self.id}") but with f string the output is normal
    #replacement is not an option so as an alternate we will use inheritance

class sing_inheritance(inheritence):
  def __init__ (self, child_name, child_no):
    self.childname = child_name
    self.childnumber = child_no

  def printdetails(self):
    print(f"child name is : {self.childname} and my number is {self.childnumber}")
    print("I am inherited from sing_inheritance class")
    

employee = inheritence ("Sanskar", 55) #1st object
#employee.show_details()
print(employee._inheritence__private)#can access the private member __private, this is known as name mangling

employee2 = sing_inheritance("Child1", 1)
employee2.printdetails()

#python have no public, private, protected concept
