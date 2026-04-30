# reverse each word in a given string
def reverse_words(string):
    for word in string.split('\n'):  # split the string into lines
        return ' '.join(word.split()[::-1]) # split the line into words, reverse the list of words, and join them back into string
print(reverse_words("The quick brown fox jumps over the lazy dog"))
print(reverse_words("my python practice"))