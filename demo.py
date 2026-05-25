'''num=1;
print(type(num))
num=12.0;
print(type(num));
num1=6
print(num1+num1);
num = -12.76;
print(type(num));
'''
list = [1,"hello",3.15]
list[1]=2
print(list[1],'=',type(list[1]))

tuple=(1,"hi",3.14)
#tuple[2]=6
print(tuple[2])

set={1,1,2,3,"jihc"}
print(set)

f=2
for x in set:
    if(f==x):
        print(x)

myvar = None
print(type(myvar))

dict ={"name":"krishna","marks":69.5}

dict['name']="hi"
print(dict['name'])

x =(1==True)
print(x)
x =(1==False)
print(x)
x=1+True
x=1+False
print(x)

num1 = 1

print(type(num1) is not int)


num2=num1
print(id(num1))
print(id(num2))
num2 =1
print(id(num2))
print()
a=[1,2,3]
print("1" in a)

a=[1,2,3]
print("1" not in a)

num =1
print(type(num))
print(float(num))
print(type(num))

fname = input(["enter your name"])
age = input(["what is u r age"])
print(type(age))

name ="krishna"
age =12
print("hi",name)
print(f"hi {name} my age is {age}")
print("apple","orange","banana",sep="88",end=".\n")