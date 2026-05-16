from itertools import chain
def chain_itertools(lst1, lst2, lst3):
    return chain(lst1, lst2, lst3)
result = chain_itertools([1, 2, 3], ['a', 'b', 'c'], [True, False]) #datatypes: integer, string, boolean
print(type(result)) #itertools.chain
for i in result:
    print(i)
