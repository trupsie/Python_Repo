#Write a map function that adds and subtracts elements of the two lists, without using lambda
'''def add(x, y):
    return x + y
Num1 = [3,5,6,8]
Num2 = [4,8,2,1]
Result = [list(map(add, Num1, Num2))]
print (Result)

#This program subtracts two numbers from the two separate lists
def sub(a, b):
    return a - b
ListA = [10, 20, 30, 40, 50]
ListB = [5, 10, 15, 20, 25]
Outcome = [list(map(sub, ListA, ListB))]
print(Outcome)'''

#This program add and subtracts together and prints results
def add_num_sub(a, b):
    return a + b, a - b
num1=[55, 23, 6888, 907]
num2=[25,66,77,22,58]
result = map(add_num_sub, num1, num2)
print(list(result))

