class Number:

    def getnum(self):
        self.num = int(input("Enter number: "))


class Square(Number):

    def findsquare(self):
        print("Square:", self.num * self.num)


class Cube(Number):

    def findcube(self):
        print("Cube:", self.num * self.num * self.num)


s = Square()
s.getnum()
s.findsquare()

c = Cube()
c.getnum()
c.findcube()