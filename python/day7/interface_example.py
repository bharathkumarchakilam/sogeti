from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "bark"

    def move(self):
        return "The dog runs."

class Bird(Animal):
    def make_sound(self):
        return "sweet"

    def move(self):
        return "The bird flies."

dog = Dog()
print(dog.make_sound())
print(dog.move())

bird = Bird()
print(bird.make_sound())
print(bird.move())
