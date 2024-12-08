#poly--Python refers to the ability of different objects to respond to the same method or function
                                                                           # call in different ways
#method overloading--method overloading refers to the ability to define multiple methods with the same
# name but different parameters. Python does not support method overloading in the traditional sense,
# as it allows multiple arguments to be passed to a function.

class Animal:
    def sound(self):
        print("all animals makes sound")
class Dog(Animal):
    def sound(self,breed):
        print("dog makes bow bow")
class Cat(Animal):
    def sound(self,breed,colour):
        print("cat makes meow meow")
a1=Animal()
d1=Dog()
c1=Cat()
a1.sound()
d1.sound("abc")
#d1.sound()
c1.sound("abcd","white")
#c1.sound()

class Addition:
    def add(self,a,b):
        return a+b
    def add(self,a=0,b=0,c=0,): #we need to define by default arguments for overloading
        return a+b+c
    def add(self,a=0,b=0,c=0,d=0):
        return a+b+c+d
add1=Addition()
print(add1.add(2,3))
print(add1.add(2,3,4))
print(add1.add(2,3,4,5))