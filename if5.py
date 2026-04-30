salary=float(input("Enter your salary: "))
if salary >= 30000:
    tax = salary * 0.10
    print("The tax amount is:", tax)
elif salary > 50000:
    tax = salary * 0.20
    print("The tax amount is:", tax)
else:
    print("No tax")