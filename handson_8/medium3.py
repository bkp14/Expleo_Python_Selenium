code = input("Enter values: ")

data = code.split(",")

if data[0].strip() == "1":
    a = float(data[1])
    b = float(data[2])
    print(a + b)

elif data[0].strip() == "2":
    a = int(data[1])
    b = int(data[2])
    print(a * b)

elif data[0].strip() == "3":
    a = data[1].strip().replace("'", "").replace('"', "")
    b = data[2].strip().replace("'", "").replace('"', "")
    print(a + b)