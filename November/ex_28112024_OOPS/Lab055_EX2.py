"""
class Caluclator:
    def __init__(self):
      print("caluclations")
    def sum(self,a,b):
        return a+b
    def diff(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
obj1=Caluclator()
a=float(input("enter the a value:"))
b=float(input("enter the b value:"))

o1=obj1.sum(a,b)
o2=obj1.diff(a,b)
o3=obj1.mul(a,b)
o4=obj1.div(a,b)
print(o1)
print(o2)
print(o3)
print(o4)
"""


# second method

class Caluclator:
    def __init__(self):
      self.a=float(input("enter the a value:"))
      self.b=float(input("enter the b value:"))
    def sum(self):
        return self.a+self.b
    def diff(self):
        return self.a-self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
obj1=Caluclator()
#a=float(input("enter the a value:"))
#b=float(input("enter the b value:"))

o1=obj1.sum()
o2=obj1.diff()
o3=obj1.mul()
o4=obj1.div()
print(o1)
print(o2)
print(o3)
print(o4)



