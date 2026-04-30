num_rows = 7
#upper part of triangle
for i in range(1,num_rows):
    for j in range(i):
        print("*", end=" ")
    print()
    #lower part of triangle
for i in range(num_rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()