def pascal_triangle(n):
    triangle_rows = [1] #rows
    y = [0] #columns
    for i in range(max(n, 0)):   # max is used to ensure that n is non-negative
        print(triangle_rows)
        triangle_rows = [lst + row for lst, row in zip(triangle_rows + y, y + triangle_rows)]
    return n >= 1
pascal_triangle(10)
    
