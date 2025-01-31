from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    
    def show(self):
        print("The concrete method")
        
class Child(Father):
    def disp(self):
        print("Implemented disp method")

child = Child()
child.disp()  
child.show()  
