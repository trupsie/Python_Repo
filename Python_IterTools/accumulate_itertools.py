from itertools import accumulate
import operator
def accumulate_itertools(lst):
    #return accumulate(lst, operator.add)
    #return accumulate(lst, operator.mul)
    #return accumulate(lst, operator.sub)
    return accumulate(lst, operator.truediv) #modulus of each element to the next element = 2/5, 5/9, 9/11
    #return accumulate(lst, operator.pow)  #power of each element to the next element
    #return accumulate(lst, operator.floordiv) #floor division of each element to the next element
result = accumulate_itertools([2, 5, 9, 11]) #datatypes: integer
print(type(result)) #itertools.accumulate
for i in result:
    print(i)