#This program will map, filter, reduce fuctions implementation
from functools import reduce
#map function
numbers = [7, 8, 9, 10, 11, 12, 13]
result1 = list(map(lambda x: x*2, numbers))
print(result1)
print()

#filter function
result2 = list(filter(lambda y: y%2 == 0, numbers))
print(result2)
print()

#reduce function
result3 = reduce(lambda a, b: a + b, numbers)
print(result3)
print()