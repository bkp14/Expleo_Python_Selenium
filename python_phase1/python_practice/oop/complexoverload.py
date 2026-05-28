class complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def __add__(self, sec):
        r=self.real+sec.real
        i=self.img+sec.img
        return complex(r,i)
    def __str__(self):
        return str(self.real)+'+'+str(self.img)+'i'
ob = complex(5,3)
ob1 = complex(5,3)

print(ob+ob1)    
    
