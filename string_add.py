def string_add(str1):
    length = len(str1)
    if length > 4:
        str1 += ", Hello"
    elif length <= 4:
        str1 += ", Not Hello"
    return str1
print(string_add(input("Enter a name: ")))



    
    