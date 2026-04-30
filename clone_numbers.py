'''def clone_numbers(n):
    return [n] * 3
print(clone_numbers(5))'''

'''def clone_numbers(num):
    """Returns a list containing three copies of the input number."""
    lst_numbers = []
    #lst_numbers = [num] * 3
    for n in range(4):
        lst_numbers.append(num)
    return lst_numbers
print(clone_numbers([2, 3, 4, 6]))'''

def clone_numbers(num):
    for i in range(3):
        clone = num.copy()   # use copy to avoid reference issue
        print(f"Iteration {i+1}: {clone}")
#clone_numbers([2, 3, 4, 6])
clone_numbers(input("Enter a list of numbers (comma separated): ").split(","))

