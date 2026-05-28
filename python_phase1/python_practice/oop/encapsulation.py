class encapsule:
    def __init__(self):
        self.name="krishna"
        self.__age=29
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age=age
        
ob = encapsule()
print("name: ",ob.name," age: ",ob.getage())
ob.setage(21)
print("name: ",ob.name," age: ",ob.getage())
