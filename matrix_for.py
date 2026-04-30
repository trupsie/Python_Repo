row_num = int(input("Enter the number of rows: "))
col_num = int(input("Enter the number of columns: "))

multi_matrix = [[3 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_matrix[row][col] = row * col
print("Multiplication Matrix:", multi_matrix)
#print('\n\n')
