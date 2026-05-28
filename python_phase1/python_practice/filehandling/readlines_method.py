myob = open("myfile.txt","r")
var = myob.readline(-1)
print(myob.tell())
print(var)
myob.close()

#readines bring all lines

#readline bring a single line