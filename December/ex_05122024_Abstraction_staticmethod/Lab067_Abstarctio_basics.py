from abc import ABC,abstractmethod
#ABC stands for Abstract Base Class. It is a module provided by Python's abc (Abstract Base Classes) module.
#By inheriting from ABC, the Animal class becomes an abstract class, meaning it cannot be instantiated directly. Instead, it serves as a blueprint for other classes.
class Animal(ABC):
    @abstractmethod  #must be implemented in subclasses
    def sound(self):
        pass

    # Regular method (can have implementation)
    def eat(self):
        print("animal is eating")
class Dog(Animal):
    def sound(self):
        print("dog makes bow bow")
class cat(Animal):
    def sound(self):
        print("cat makes meow meow")
d1=Dog()
c1=cat()
d1.sound()
d1.eat()
c1.sound()
c1.eat()
