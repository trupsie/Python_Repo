#Person_Age = int(input("Enter your age: "))
Person_Age = [16, 18, 20, 33, 22, 67, 12, 21, 17, 11]
def driving_age(age):
    return age >= 18
Legal_Driving_Age = filter(driving_age, Person_Age)
print(list(Legal_Driving_Age))
