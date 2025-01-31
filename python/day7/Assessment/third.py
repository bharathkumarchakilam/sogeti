from abc import ABC, abstractmethod
import math

class shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class rectangle(shape):
    
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
class circle(shape):
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return math.pi * self.radius*self.radius
    
c=circle(7)
r=rectangle(12,10)

print(c.area())
print(r.area())
    

