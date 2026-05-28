string = input("enter a string")
n=a=0
for i in string:
    if(i.isnumeric()):
        n+=1
    elif(i.isalpha()):
        a+=1
    else:
        pass
print(n,a)