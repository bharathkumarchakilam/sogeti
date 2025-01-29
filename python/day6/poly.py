class two_wheeler:
    def vehicle(self):
        print("bike")
        
class four_wheeler:
    def vehicle(self):
        print("car")

two=two_wheeler()
four=four_wheeler()
        
for road_transport in [two,four]:
    road_transport.vehicle()
