class myclass:
    def __init__(self,radius=1.0,colour="red"):
        self.radius=radius
        self.colour =colour
    @classmethod
    def withradius(cls,radius):
        return cls(radius)
    @classmethod
    def withcolour(cls,colour):
        return cls(colour=colour)
    def getradius(self):
        return self.radius
    def getcolour(self):
        return self.colour
ob = myclass()
r=myclass.withradius(2.0)
c=myclass.withcolour("green")
print(r.getradius())
print(c.getcolour())
print(ob.getradius())
print(ob.getcolour())




        