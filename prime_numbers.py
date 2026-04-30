def primenum (num):
    if num <= 0 or num ==1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
print(primenum(0))  #False
print(primenum(1))  #False
print(primenum(2))  #True
print(primenum(-10))  #False
print(primenum(15))  #False