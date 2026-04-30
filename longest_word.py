def longest_word(words_list):
    word_length = []
    for word in words_list:
        word_length.append((len(word), word))  #append a tuple of length of word and word itself to word_lengh list
    word_length.sort()  #sort the list of word_length in ascending order
    return word_length[-1][0], word_length[-1][1]  #return the length and the longest word from the sorted list
result = longest_word(["Python", "JavaScript", "machine_learning", "Java"])
print(result[1])
print(result[0])

