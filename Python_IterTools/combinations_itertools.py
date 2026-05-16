import itertools as it
def combinations_data(iter, length):
    return it.combinations(iter, length) #order does not matter
    #return it.permutations(iter, length) #order matters
result = combinations_data(['T','R','U', 'P', 'T', "I"],  2)
for i in result:
    print(i)
print(type(i))