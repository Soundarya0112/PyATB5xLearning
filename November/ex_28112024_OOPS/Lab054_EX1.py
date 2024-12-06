class Person:
    def __init__(self): #init method is automatically called when the object is created
        self.name=input("enter ur name:")
        self.age=input("enter ur age:")
        self.address=input("enter ur adress:")
        self.phno=input("enter ur phone no:")
    def print_display_function(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Address=",self.address)
        print("phone no",self.phno)
obj1=Person()
obj1.print_display_function()