# Function to check if a number is even or odd
#num_list = [11, 32, 13, 4, 25, 46, 87, 85, 90, 101]

def is_even_odd(num):
    #result = []
    for n in num:
        if n % 2 == 0:
            #result.append(n)
            print(f"{n} is even.")
            #print("even number", n)
        else:
           #result.append(n)
            print(f"{n} is odd.") 
            #print("odd number", n)
    #return result
print(is_even_odd([11, 32, 13, 4, 25, 46, 87, 85, 90, 101]))