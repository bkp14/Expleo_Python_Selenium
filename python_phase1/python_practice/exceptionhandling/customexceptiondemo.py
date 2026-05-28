class error(Exception):
    pass
class valuetoosamll(error):
    pass
class valuetoolarge(error):
    pass
num = int(input("enter a value: "))
try:
    if(num<10):
        raise valuetoosamll("value too small")
    if num>100:
        raise valuetoolarge("value too large")
except valuetoosamll as e:
    print(e)
except valuetoolarge as e:
    print(e)
except error as e:
    print("parent exception: ",e)            