num_rows = 5
# Upper part
k = 2 * num_rows - 2
for i in range(1, num_rows + 1):
    # spaces
    for j in range(k):
        print(" ", end="")
    k -= 2
    # numbers
    for j in range(i):
        print(i, end=" ")
    print()

# Lower part
k = 2
for i in range(num_rows - 1, 0, -1):
    # spaces
    for j in range(k):
        print(" ", end="")
    k += 2
    
    # numbers
    for j in range(i):
        print(i, end=" ")
    print()