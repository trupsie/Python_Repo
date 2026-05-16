from itertools import product
from tkinter.font import names
def permutations_names(names, n):
    for x in product(names, repeat=n):
        count = ''.join(x)
        print(count, end=' ')
beings = ('CAT', 'DOG', 'BIRD')
print('Permutations of beings:', '\n')

n = 1
permutations_names(beings, n)
print('\n\n')

n = 2
permutations_names(beings, n)
print('\n\n')

n = 3
permutations_names(beings, n)
print('\n\n')
