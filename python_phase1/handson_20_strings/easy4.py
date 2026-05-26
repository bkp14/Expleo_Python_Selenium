sentence = input("enter a sentence: ")
words = sentence.split()

for word in words:
    if word.isalnum() and any(ch.isalpha() for ch in word) and any(ch.isdigit() for ch in word):
        print(word)