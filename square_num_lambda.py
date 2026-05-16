numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))  # Using lambda to square each number in the list
print(squared_numbers)
print()
squared_numbers = [x**2 for x in numbers]  # Using list to square each number in the list without lambda or map
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print()
print(type(squared_numbers)) #returns data type of squared_numbers which is list
