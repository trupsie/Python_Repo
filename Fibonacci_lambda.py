#This program still works but does not print in a single line sequence. Not to be used.
'''x, y = 0, 1
fib = lambda x, y: (x, y+x)  #cannot initialize same values x,y again. use different inner variables
num = int(input("Enter the number of Fibonacci numbers to generate: "))
for n in range(num):
    x, y = y, x + y 
    print(fib(x, y)) '''
    
#This program works
'''num = int(input("Enter the number of Fibonacci numbers to generate: "))
fib = lambda x:0 if x == 0 else 1 if x==1 else fib(x-1) + fib(x-2)
for n in range(num): 
    print(fib(n), end = ' ')'''

#This also works
num = int(input("Enter the number of terms for Fibonacci Series: "))
x, y = 0, 1
for i in range(num):
    print(x, end = ' ')
    x, y = (lambda a, b: (b, a+b)) (x,y)
   
 

