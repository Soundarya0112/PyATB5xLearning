"""
class PyATB:
    def __init__(self): #init method is automatically called when the object is created
        self.name=input("enter ur name:")
        self.age=input("enter ur age:")
        self.address=input("enter ur adress:")
        self.phno=input("enter ur phone no:")
        self.id=input("enter ur id no:")
    def print_student_information(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Address=",self.address)
        print("phone no",self.phno)
        print("id no",self.id)
obj1=PyATB()
obj1.print_student_information()
"""
from tkinter.font import names


class PyATB:
    def __init__(self,name,age,address,phno,id): #init method is automatically called when the object is created
        self.name=name
        self.age=age
        self.address=address
        self.phno=phno
        self.id=id
    def print_student_information(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Address=",self.address)
        print("phone no",self.phno)
        print("id no",self.id)
obj1=PyATB("PINKY",21,"HYDERAB",123344,12)
obj2=PyATB("ROSY",21,"GUNTUR",123344,12)
obj1.print_student_information()
obj2.print_student_information()