'''given tuple values,if element value is even then square the number,If element value is odd then cube the number'''

'''num_tuple = (3, 5, 7, 9, 2, 4, 6, 8)
result_tuple = tuple(map(lambda x: x**2 if x%2 == 0 else x**3, num_tuple))
print(result_tuple)'''


num_tuple = [3, 5, 7, 9, 2, 4, 6, 8]
num_tuple2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def listnum(num):
    result = []
    for i in num:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return tuple(result)
    #return list(result)
#output = listnum(num_tuple)
#print(output)
print(listnum(num_tuple))
print(tuple(listnum(num_tuple2)))




