''''FORMULA FOR FACTORIALS / Factorial Numbers - always a positive number. Used for ML Algorithms, Combinatorics, etc.
5! (factorial number of 5)
n! = n * (n-1)!   
5! = 5 * 4 * 3 * 2 * 1
5! = 120
'''
def factorial_numbers(number):
   if number ==0:
      return 1
   else:
      return number * factorial_numbers(number-1)  # n! = n * (n-1)!
print(factorial_numbers(0))  #1
print(factorial_numbers(7))  #1
print(factorial_numbers(10)) #3628800
