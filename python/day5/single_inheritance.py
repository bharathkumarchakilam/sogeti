class Parent:
    def __init__(self):
        self.height = "160cm"
       

    def display_parent(self):
        print("This is the parent class.")
        

class Child(Parent):
    def __init__(self):
        super().__init__()
        print(f"Height: {self.height}")
        

    def display_child(self):
        print("This is the child class.")

child1 = Child()
child1.display_parent() 
child1.display_child()   
