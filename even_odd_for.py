numbers = [2, 4, 6, 8, 10, 83, 45, 67, 90]
even_count = 0
odd_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)