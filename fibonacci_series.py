num = int (input("Enter the numbers in the Fibonacci series: "))
f1, f2 = 0, 1
for fib in range(num):
    print(f1, end = '  ')
    f1, f2 = f2, f1 + f2