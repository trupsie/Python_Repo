from itertools import accumulate
def maxnum_accumulate(lst):
    return accumulate(lst, max)   #max will give the maximum value at each step, but we want the minimum value at each step, so we use min instead of max
    #return accumulate(lst, min) #min will give the minimum value at each step, but we want the maximum value
numbers = [11, 29, 300, 45, 52, -600, -50, 0, 1000, 500, 25]   
#result = maxnum_accumulate([11, 29, 300, 45, 52, -600, -50, 0, 1000, 500, 25])
result = maxnum_accumulate(numbers)
print('original list of numbers:', numbers) #original list
#print(result)
for i in result:
    print(i)
    