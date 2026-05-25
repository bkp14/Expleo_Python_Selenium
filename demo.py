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

def add(a,b):
    return a+b
a = int(input("enter a number"))
b = int(input("enter a number"))
result = add(a,b)
print(result)

text="welcome"
print(text[5])

greet ="welcome"
for i in "welcome":
    print(i)

    
print(greet)
del greet
print(greet)

i=0
while(i<len("welcome")):
    print("welcome"[i])
    i+=1

text="hello"
if("hel" not in text):
    print(True)
else:
    print(False)    
print(text[4::-1])

print("sello"+"sello"[::-1])

text="hello, wOrld!".lower()
print(text.count('or'))
print("j"+text[7:])
print("j"+text[-6:-1])

word = 'good day'
index = word.find("o",3)
print(index)
print(word.replace(word[0],"d"))

n= input("enter")
if(n.__eq__ (n[::-1])):
    print(True)
else:
    print(False)