from tkinter.font import names


class Dog:
    #Attributes||instaance variable||data variables
    Name=None
    Breed=None
    Age=None
    Height=None
    Weight=None
    # Behaviour
    def __init__(self,Name,Breed):
        self.Name=Name
        self.Breed=Breed
    def display(self):
        print(self.Name,self.Breed)
    def eat(self):
        print("Dog can eat")
    def sleep(self):
        print("dog can sleep")
    def walk(self):
        print("dog can walk")

"""
obj_ref1=Dog()   # object 1 is created
obj_ref1.eat()
obj_ref1.sleep()
obj_ref1.walk()
print(obj_ref1.Name)
print(obj_ref1)
"""
obj_ref1=Dog("Leo","abc")
obj_ref1.eat()
print(obj_ref1.Name)
obj_ref1.display()

obj_ref2=Dog("Husky","bcd")
obj_ref2.eat()
print(obj_ref1.Name)
obj_ref2.display()



"""
obj_ref2=Dog()  #object 2 is created
obj_ref2.eat()
obj_ref2.sleep()
obj_ref2.walk()
print(obj_ref2.Name)
print(obj_ref2)
"""


