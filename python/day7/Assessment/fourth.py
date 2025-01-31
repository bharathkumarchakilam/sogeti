from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def Profession(self):
        pass
    
    def introduce(self):
        print("I am a Father ans also a ",end=" ")
        self.Profession()
        
class Engineer(Father):
    def Profession(self):
        print("Engineer.")
        
class Doctor(Father):
    def Profession(self):
        print("Doctor.")
        
        
engineer = Engineer()
doctor = Doctor()

engineer.introduce()
doctor.introduce()
        