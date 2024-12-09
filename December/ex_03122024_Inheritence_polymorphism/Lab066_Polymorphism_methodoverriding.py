class Animal:
    def sound(self):
        print("all animals makes sound")
class Dog(Animal):

    def sound(self):
        super().sound()  #parent sound will call
        print("dog makes bow bow")
class Cat(Animal):
    def sound(self):
        print("cat makes meow meow")
#a1=Animal()
d1=Dog()
c1=Cat()
#a1.sound()
d1.sound()
c1.sound()
