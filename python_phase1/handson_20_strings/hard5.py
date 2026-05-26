s1 = input("enter: ")
s2 = input("enter: ")

len1 = len(s1)
len2 = len(s2)

x = s1[0] + s2[0]

z = s1[len1 - 1] + s2[len2 - 1]


y1 = s1[len1 // 2]
y2 = s2[len2 // 2]

y = y1 + y2

print(x + y + z)