class woman:
    def free_bus(self):
        return "woman go in free bus"
    
class man:
    def walk(self):
        return "man go by walk"
    
class person(woman,man):
    def drive(self):
        return "person can drive a vehicle"
    
p=person()
print(p.free_bus())
print(p.walk())
print(p.drive())

m1=man()
m1=person()
print(m1.drive())