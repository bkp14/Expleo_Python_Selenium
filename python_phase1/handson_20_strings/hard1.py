word = input("enter a word : ")
l=s=u=0 
for ch in word:
    if(ch.islower()):
        u+=1
    elif(ch.isupper()):
        l+=1
    else:
        s+=1    
print("number of uppercase letters:",u)
print("number of lowercase letters: ",l)
print("number of special characters: ",s)     