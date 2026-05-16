from itertools import combinations_with_replacement
def combinations_names(names, n):
    return combinations_with_replacement(names, n)
names = ['John', 'Jane', 'Mike']
print("Combinations with repetition of names:", '\n')
n = 1
print(list(combinations_names(names, n)))
print()
n = 2
print(list(combinations_names(names, n)))
print()
n = 3
print(list(combinations_names(names, n)))
print()
