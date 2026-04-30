deposit_amount = float(input("Enter the amount you want to deposit: "))
if deposit_amount < 10000:
   interest = deposit_amount * 0.10
else:
    if deposit_amount <= 15000:
        interest = deposit_amount * 0.20
    else: 
        if deposit_amount >= 20000:
            interest = deposit_amount * 0.30
        else:
            interest = 0
print("The total amount is equal to ", deposit_amount + interest)
print("Total interest rate is:", interest)
