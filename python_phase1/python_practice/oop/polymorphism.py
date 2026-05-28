class vehicle:
    def __init__(self,name,colour,price):
        self.name=name
        self.colour=colour
        self.price=price
    def show(self):
        print(f"details : {self.name},{self.colour}{self.price}")

    def max_speed(self):
        print("vehicle max spped is 150")
    def change_gear(self):
        print("vehicle change gear 6")

class car(vehicle):
    def max_speed(self):
     super().max_speed()
     print("car max spped is 240")
    def change_gear(self):
     super().change_gear() 
     print("car changed 7th gear")
c = car("carx1","red",100000) 
c.show()
c.max_speed()
c.change_gear()



    

