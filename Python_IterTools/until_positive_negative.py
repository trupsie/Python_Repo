#from itertools import accumulate
import itertools as it
def negative_numbers(n):
    return n < 7
def until_positive_negative(numbers):
    return it.dropwhile(negative_numbers, numbers) #dropwhile will drop the elements until its true
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = until_positive_negative(numbers)
print(list(result))


 
