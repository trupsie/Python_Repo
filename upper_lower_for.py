name = input("Enter your name: ")
for char in name:
    if char.isupper():
        print(f"{char} is an uppercase letter.")
    elif char.islower():
        print(f"{char} is a lowercase letter.")
    else:
        print(f"{char} is not an alphabetic character.")