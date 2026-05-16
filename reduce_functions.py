from functools import reduce

# for numerical values, it will single value depending on expression (operation)
numbers = [11, 22, 33, 44, 55]
#reduced_sum = reduce(lambda x, y: x + y, numbers)
reduced_sum = reduce(lambda x, y: x + y, numbers, -100) #with initialization value either positive or negative
print(reduced_sum)  # Output: 15

# it will make a sentence for strings
trees = ('oak', 'pine', 'birch', 'maple')
reduced_trees = reduce(lambda x, y: x + ' ' + y, trees, 'lemon') #with initialization value either positive or negative
#reduced_trees = reduce(lambda x, y: x + ' ' + y, trees) #without initialization value
print(reduced_trees)  # Output: 'oak-pine-birch-maple