class shape:
    def area(self):
        pass
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
    
class square(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length*self.breadth
    
s_area=square(12,13)
print(s_area.area())