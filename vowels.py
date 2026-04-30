def vowels_test(word):
    vowels = 'aeiouAEIOU'
    print(len([letter for letter in word if letter in vowels]))
    print([letter for letter in word if letter in vowels])
vowels_test("I am learning Python")
    