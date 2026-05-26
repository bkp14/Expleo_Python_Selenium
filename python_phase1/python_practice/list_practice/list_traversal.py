integers = "12345"
t=list(integers)
for i in t:
    print(i)

for i in range(len(t),0,-1):
    print(t[i-1])  
