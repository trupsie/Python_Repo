from collections import Counter

#strings = 'Donnadoesnttakeenglishclass'
strings = input('Enter a string with or without space:')

def common_strings(str1, n=4):
    return Counter(str1).most_common(n)
print(common_strings(strings))