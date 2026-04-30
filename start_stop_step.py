#this program will skip and print the next one in the list. In between stop and start.
num = [11, 23, 45, 67, 2, 83, 50, 26, 89, 90]
#for i in range(len(num) - 1, -1, -1):  #reverse order
for i in range(0, len(num), 3):
    print(num[i])