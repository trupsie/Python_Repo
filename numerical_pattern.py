num_rows=6
for i in range(1, num_rows + 1):
    #for j in range(1, i + 1):
    for j in range(num_rows -i): #reverse pattern
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print(j, end=" ")
    print()