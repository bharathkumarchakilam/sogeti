from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        print("bark!")
        
class Cat(Animal):
    def make_sound(self):
        print("meow!")
        
c=Cat()
d=Dog()

c.make_sound()
d.make_sound()        