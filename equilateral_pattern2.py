#reverse of equilateral pattern
num_rows=6
#upper part of triangle
k=2*num_rows-2
for i in range(0,num_rows-1):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("*", end=" ")
    print('\r')
k=-1
    #lower part of triangle
for i in range(num_rows-1, -1, -1):
    for j in range(k, -1, -1):
        print(end=" ")
    k=k+2
    for j in range(0, i+1):
        print("*", end=" ")
    print('\r')