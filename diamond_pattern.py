n = 5  #total rows
num = 1 #number to print, starting from 1
# Upper half
for i in range(1, n + 1):
    print(" " * ((2*n - i)), end="")
    for j in range(i):
        print(num, end="")
        num += 1
    print()
# Lower half
for i in range(n - 1, 0, -1):
    print(" " * ((2*n - i)), end="")
    for j in range(i):
       print(num, end="")
       num += 1
    print()

''' n = 5  # Height of the top half
# Upper Half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower Half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))'''