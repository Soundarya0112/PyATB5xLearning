
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def walk(self):
        #print(self.name,self.age)
        return self.name
obj1=Student("pinky",23)
print(obj1.walk())
obj2=Student("minni",20)
print(obj2.walk())
print(obj1.walk(),"is walking")
print(obj2.walk(),"is walking")
