class Student:
    Name="soundarya"
    age=22
    ID=123456789
    #print(Student.Name)
    #print(Student.age)
#memory is allocated only after object is created
obj1=Student()
print(obj1.Name)

class Dog:
    #Attributes||instaance variable||data variables
    Name="leo"
    Breed=None
    Age=None
    Height=None
    Weight=None
    # Behaviour
    def eat(self):
        print("Dog can eat")
    def sleep(self):
        print("dog can sleep")
    def walk(self):
        print("dog can walk")
obj_ref1=Dog()   # object 1 is created
obj_ref1.eat()
obj_ref1.sleep()
obj_ref1.walk()
print(obj_ref1.Name)
print(obj_ref1)

obj_ref2=Dog()  #object 2 is created
obj_ref2.eat()
obj_ref2.sleep()
obj_ref2.walk()
print(obj_ref2.Name)
print(obj_ref2)

