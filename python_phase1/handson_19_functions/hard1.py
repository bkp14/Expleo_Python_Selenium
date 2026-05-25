def calculate_increment(salary, rating):
    if rating >= 1 and rating <= 4:
        return salary + (salary * 0.10)

    elif rating > 4 and rating <= 7:
        return salary + (salary * 0.25)

    elif rating > 7 and rating <= 10:
        return salary + (salary * 0.30)

    else:
        return "Invalid Input"


salary = float(input("Enter the salary: "))
rating = float(input("Enter the appraisal rating: "))

if salary <= 0 or rating < 1 or rating > 10:
    print("Invalid Input")
else:
    result = calculate_increment(salary, rating)
    print(int(result))