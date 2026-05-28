weight = float(input("enter weight in kilograms: "))
height = float(input("enter height in meters: "))
if(weight<0):
    print("enter valid weight")
elif(height<0 and height>2.0):
    print("enter valid height")
else:
   print("BMI",round(weight/(height ** 2),2))

