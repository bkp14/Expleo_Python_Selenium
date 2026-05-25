def hikedSalary(oldSalaryPerMonth,hike):
    hike = oldSalaryPerMonth +( (oldSalaryPerMonth) * (hike/100))
    print(hike)

old = int(input("enter: "))
hk= float(input("enter: "))
hikedSalary(old,hk)