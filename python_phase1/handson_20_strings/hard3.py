string1 = input()

print("Initial String with use of Triple Quotes:", string1)

print("Escaping Single Quote:", string1.replace("'", "\\'"))

print("Escaping Double Quotes:", string1.replace('"', '\\"'))

word = string1.split('"')[1] if '"' in string1 else "Python"

print("Escaping Backslashes: C:\\Python\\" + word + "\\")

print("Tab:")
print("\tHi", word)

print("New Line:")
print("Python", word)