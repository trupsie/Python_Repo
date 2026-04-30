#This below program works completely fine. It defines a function called squared_numbers that calculates the squares of numbers from 1 to 6 and returns them in a list. The function also prints each number along with its square. Finally, it calls the function and prints the resulting list of squared numbers.'''
'''def squared_numbers():
    """Returns a list of squared numbers."""
    list_num = list()
    for n in range(1, 7):
        list_num.append(n ** 2)
        print(n, ":", list_num[-1])
    return list_num
print(squared_numbers())
'''

#This function calculates the squares of numbers from 1 to 9 and prints each number along with its square. It does not return a list of squared numbers, but simply prints the results to the console.
def squared_numbers():
    for n in range(1,10):
        print(f"{n} => {n ** 2}")
squared_numbers()
