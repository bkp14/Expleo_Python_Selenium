class example:
    def method(self,a,b=None):
        if b is None:
            print(f"single argument: {a}")
        elif isinstance(a,int) and  isinstance(b,int):
            print(f"two integers: {a},{b}")
        elif isinstance(a,str) and  isinstance(b,str):
            print(f"two strings: {a},{b}")
        else:
            print(f"mixed types: {a},{b}")

ob = example()
ob.method(1)
ob.method(1,2)
ob.method("h","k")
ob.method(1,"k")

            