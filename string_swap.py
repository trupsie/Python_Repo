def string_swap(str1, str2):
    swapped_str1 = ""
    swapped_str2 = ""

    for char in str1:
        swapped_str1 += char
    for char in str2:
        swapped_str2 += char
    return swapped_str2, swapped_str1

print(string_swap(input("Enter first string: "), input("Enter second string: ")))
    
