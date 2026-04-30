def multiple_numbers(num1):
    total = 1
    for n in num1:
        total *= n
    return total
print(multiple_numbers([1, 2, 3, 4, 5]))
