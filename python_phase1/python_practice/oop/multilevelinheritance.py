class student:
    def info(self):
        name = input("enter name: ")
        id = int(input("enter id: "))

        self.__name = name
        self.__id = id

    def display(self):
        print(self.__name, self.__id)


class marks(student):

    def getmarks(self):
        self.info()

        self.__mark1 = int(input("enter sub1 mark: "))
        self.__mark2 = int(input("enter sub2 mark: "))
        self.__mark3 = int(input("enter sub3 mark: "))

    def printmarks(self):
        self.display()

        print(self.__mark1)
        print(self.__mark2)
        print(self.__mark3)

    def calculate(self):
         total = self.__mark1 + self.__mark2 + self.__mark3
         return total
        
class results(marks):
    def getResult(self):
        self.getmarks()
        self.__total=self.calculate()
    def putresult(self):
        self.printmarks()
        print("total marks out of 300: ",self.__total)
obj = results()
obj.getResult()
obj.putresult()            