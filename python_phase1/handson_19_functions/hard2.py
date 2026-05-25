def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def calculator(operation, a, b):
    return operation(a, b)

op = input("Enter operation (add/sub/mul): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if op == "add":
    result = calculator(add, a, b)

elif op == "sub":
    result = calculator(subtract, a, b)

elif op == "mul":
    result = calculator(multiply, a, b)

else:
    result = "Invalid operation"

print("Result:", result)