num1 = [1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
num3 = [11, 12, 13, 14, 15]
#map function maps each element and passes the resulting expression for e.g. 1 * 6 * 11 = 66
result = map(lambda x, y, z: x * y * z, num1, num2, num3) #initialize variables x,y,z; action result, location of values required for action
print(list(result))

