myob =open("myfile.txt","r")
print(myob.read())
d=myob.readlines()
for line in d:
    words = line.split()
    print(words)