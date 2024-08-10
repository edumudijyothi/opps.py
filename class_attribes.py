#class attributes  or user attributes or object attribute are   changable.
#a object to create invidual name
class Person:
    city="hyd"#city is a class attribute
    def __init__(self,name,age):#constor call
      self.name=name
      self.age=age
    def prnt(self):#fuction name is prnt
        print(self.name,self.age,Person.city)#city is a class attribute
#take user input for name and age
name=input("Enter name:")
age=input("Enter age:")
p=Person(name,age) 
p.prnt()
name=input("Enter name:")
age=input("Enter age:")
q=Person(name,age)#instance attributes 
q.print()
#parameter values are change but not change default attributes/self attibute.
    
