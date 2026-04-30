#see ascii chart 
num_rows = 6
alpha = 65 #ascii value of A
for i in range(0, num_rows):
    print(" " * (num_rows - i), end="") #only to print in equilateral triangle shape
    for j in range(0, i + 1):
        print(chr(alpha), end=" ")
        alpha += 1
    print()