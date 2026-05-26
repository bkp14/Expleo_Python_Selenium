sentence = input("enter the string : ")
word = input("enter the word")
index = sentence.rfind(word)
print(f"Last occurrence of {word} starts at index {index} ")