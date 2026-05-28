class myclass:
    def __init__(self,radius=1.0,colour="red"):
        self.radius=radius
        self.colour =colour
    def getradius(self):
        return self.radius
    def getcolour(self):
        return self.colour
    def setradius(self,rad):
        self.radius=rad
    def setcolour(self,colo):
        self.colour=colo
    def getarea(self):
        return (3.14*self.radius**2)        
    def __str__(self):
        return f"circle[radius={self.radius},colour={self.colour}]"
ob = myclass()
print(ob.getradius())
print(ob.getcolour())
print(ob.getarea())
ob.setcolour("blue")
ob.setradius(2.8)
print(ob.getarea())
print(ob)


        