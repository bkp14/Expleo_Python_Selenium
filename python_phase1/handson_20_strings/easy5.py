word = input("enter a word : ")
res = res1= ""
for ch in word:
    if(ch.islower()):
        res += ch
    if(ch.isupper()):
        res1+=ch
print(res+res1)        