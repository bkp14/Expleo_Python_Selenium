num = int(input("enter"))
j = 1
sums = 0
while j < num:
    sum = int(input("enter value"))
    if sum < 0:
      break
    else:
      sums += sum
print(sums)
