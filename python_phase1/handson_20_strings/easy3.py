import string
text = input("enter a string : ")
for ch in string.punctuation:
          text= text.replace(ch,"#")

print(text)           