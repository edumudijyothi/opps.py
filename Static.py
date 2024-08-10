#case sensitive
class Person:
    city="hyd"#class attribute
    def __init__(self,name,age):#constructor call
        self.name=name
        self.age=age
    def prnt(self):
        print(self.name,self.age,Person.city)
    @staticmethod #static keyword method
    def Hello():
        print("hello")
name="RAM"
age="23"
p=Person(name,age)
p.Hello()#calling static method
p.prnt()
print(p.name)
print("Hello")



 
  
