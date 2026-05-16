import itertools as it
def permutations_data(iter, length):
    return it.permutations(iter, length)
result = permutations_data(['T','R','U', 'P', 'T', "I"],  2) #2 is the length (or number of times of combinations)of the permutation
for i in result:
    print(i)


