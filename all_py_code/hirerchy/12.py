class Parent:
   def __init__(self,name):
     self.name = name
   def getName(self):
     return self.name
   
class Child(Parent):
   def __init__(self,name,age):
     Parent.__init__(self,name)
     self.age = age
   def getAge(self):
     return self.age
   
class Grandchild(Child):
   def __init__(self,name,age,location):
     Child.__init__(self,name,age)
     self.location=location
   def getLocation(self):
     return self.location
   
gc = Grandchild("Srinivas",24,"Hyderabad")
print(gc.getName(), gc.getAge(), gc.getLocation())