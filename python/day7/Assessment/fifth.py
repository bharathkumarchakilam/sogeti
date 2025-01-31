from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass
    
class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass
    
class Manager(Person,Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def get_name(self):
        print(self.name)
        
    def get_salary(self):
        print(self.salary)
        
manager=Manager("Bharath",27500)
manager.get_name()
manager.get_salary()
