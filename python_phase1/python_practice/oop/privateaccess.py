class myclass:
    def __init__(self):
        self.name="kp"
        self.__age=29
    def getage(self):
        print(self.__age)    
ob = myclass()
print(ob.name)
ob.getage()       
