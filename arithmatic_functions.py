def addition(a, b):
    return a + b
print(addition(-4, 3))  # Output: -1
print(addition(2, 7))  # Output: 9

def subtraction(a, b):
    return a - b
print(subtraction(10, 5))  # Output: 5
print(subtraction(3, 8))  # Output: -5

def multiplication(a, b):
    return a * b
print(multiplication(4, 6))  # Output: 24
print(multiplication(-2, 5))  # Output: -10

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
print(division(10, 2))  # Output: 5.0
print(division(5, 0))  # Output: Error: Division by zero is