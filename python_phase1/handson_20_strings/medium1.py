tuple1 = eval(input().split(": ")[1])
tuple2 = eval(input().split(": ")[1])

result = tuple(a + b for a, b in zip(tuple1, tuple2))

print("The concatenated tuple:", result)