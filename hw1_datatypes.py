'''Write a Python program to convert a given string list to a tuple.
Write a Python program to reverse a tuple.
Write a Python program to convert a tuple to a dictionary'''

#Write a Python program to convert a given string list to a tuple.

subjects = ['Artificial Intelligence', 'Data Science', 'Neural Networks', 'Quantum Physics', 'Quantum Theory']
tuple_subjects = tuple(subjects)
print(tuple_subjects)
print(type(tuple_subjects))
print(type(subjects))
reverse_tuple = reversed(tuple_subjects)
print(tuple(reverse_tuple))
tuple_list = [('Artificial Intelligence', 1), ('Data Science', 2), ('Neural Networks', 3), ('Quantum Physics', 4), ('Quantum Theory', 5)]
dict_subjects = {}
for x, y in tuple_list:
   #dict_subjects.setdefault(x, []).append(y) #another format of printing dictionary
   dict_subjects.setdefault(x, y)  #setdefault = dictionary default format can be used here
print(dict_subjects)