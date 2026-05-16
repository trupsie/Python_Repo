'''Write a Python program to convert a given string list to a tuple.
Write a Python program to reverse a tuple.
Write a Python program to convert a tuple to a dictionary'''

#Write a Python program to convert a given string list to a tuple
lst = ['a', 'b', 'c', 'd']
lst2 = [1, 2, 3, 'trupti', 'sam']
tup = tuple(lst)
tup2 = tuple(lst2)
print("Converted tuple:", tup)
print("Converted tuple2:", tup2)

#Write a Python program to reverse a tuple.
reversed_tup = tup[::-1], tup2[::-1]
print("Reversed tuple:", reversed_tup)

#Write a Python program to convert a tuple to a dictionary
# Assuming the tuple contains key-value pairs as sub-tuples
sample_tuple = (('a', 1), ('b', 2), ('c', 3), ('d', 4))
dict_from_tuple = dict(sample_tuple)
print("Dictionary from tuple:", dict_from_tuple)