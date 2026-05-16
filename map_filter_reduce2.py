#This program will map, filter, reduce fuctions implementation using strings

#map function for strings: break the word string into individual letters
def str_letters(str1):
    result = map(list, str1)  #map conversion list to string
    return list(result)
language = ['Java', 'Python', 'Go', 'SQL', '.Net'] #input values
print(str_letters(language))

#filter function for strings: 
languages = ['Java', 'Python', 'Go', 'SQL', '.Net'] #input values
def str_letters(str1):
    #result = filter(list, str1)  #filter
    #return list(result)
    return str1[0].lower() in ['a', 'e', 'i', 'o', 'u']
filter_language = list(filter(str_letters, languages))
print(filter_language)
#print(str_letters(languages))