s1 = input("enter a string: ")
s2 = input("enter a string")
j=len(s2)-1
res=""
for i in range(len(s1)):
    res+=(s1[i]+s2[j])
    j-=1  
print(res)
         