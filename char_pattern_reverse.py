num_rows=6
alpha=65 #ascii value of A
for i in range(num_rows, 0, -1):
    print(" " * (num_rows - i), end="") #only to print in equilateral triangle shape
    for j in range(0, i):
        print(chr(alpha), end=" ")
        alpha += 1
    print()