#write a map function without lambda to print square of numbers within a list
num_list = [2, 4, 6, 8, 10]
def square(x): 
    return x ** 2
for i in num_list:
    result = [list(map(square, num_list))]
print ((result), ' ')


