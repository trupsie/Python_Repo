#This program converts list and tuple into strings using map function
num_list = [2, 4, 6, 8]
num_tuple = (3, 5, 7, 9)
#convert list and tuple into strings
result_list = list(map(str, num_list)) #str = target string data type, num_list indicates variable in list
result_tuple = tuple(map(str, num_tuple))
print(result_list)
print(result_tuple)
