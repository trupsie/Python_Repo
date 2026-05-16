def threshold_number(num, threshold):
    if num >= threshold:
        return True
    else:
        return False
numbers = [1, 5, 10, 35, 45, 25, 50]
threshold = 15
filtered_numbers = filter(lambda x: threshold_number(x, threshold), numbers)
print(list(filtered_numbers))