myob=open("myfile.txt","w")
lines = ["ehello veryone \n","writing #multiline string\n","this is third line \n"]
myob.writelines(lines)
myob.close()