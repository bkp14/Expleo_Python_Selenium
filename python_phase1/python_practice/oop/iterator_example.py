class modoftwo:
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result = self.n%2
            self.n+=1
            return result
        else:
            raise StopIteration
num = modoftwo(3)
i=iter(num)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


               
