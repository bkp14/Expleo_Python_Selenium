myob = open("myfile.txt","r+")
old = myob.seek(0,2)
sentence = input("enter the string:")
sentence1 = input("enter the string:")
sentence2 = input("enter the string:")
myob.writelines([sentence+"\n",sentence1+"\n",sentence2])
myob.seek(old)
lines=myob.readlines()
for i in lines:
    words=i.split()
    print(words)
    
myob.close()