from abc import ABC, abstractmethod

class vehicle(ABC):
    
    def __init__(self,brand):
        self.brand=brand
        
    @abstractmethod   
    def max_speed(self):
        pass
    
class bike(vehicle):
    
    def max_speed(self):
        return 150
        
class car(vehicle):
    
    def max_speed(self):
        return 200

car = car("Toyota")
bike = bike("Yamaha")

print(f"{car.brand} max speed: {car.max_speed()} km/h")
print(f"{bike.brand} max speed: {bike.max_speed()} km/h")