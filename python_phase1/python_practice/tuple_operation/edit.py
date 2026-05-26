t =(10,20,30)
print(id(t))
t=(100,)+t[1::]
print(id(t))

