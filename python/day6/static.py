import dis

class static_variable:
    def __init__(self):
        self.name="Bharath"
    
    def display(self):
        print(self.name)
        
c=static_variable()
c.display()
dis.dis(static_variable)
dis.dis(c)
        
