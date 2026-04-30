'''Celsius = int(input("Enter the temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
print(f"{Celsius} degrees C = {Fahrenheit} degrees F.")'''

temperature = input("Enter the temperature (e.g., 25C or 77F): ")
degrees = int(temperature[:-1])
conversion = temperature[-1] 
if conversion.upper() == 'C':
    result = int(round((degrees * 9)/5 + 32))
    conversation1 = 'F'
elif conversion.upper() == 'F':
    result = int(round((degrees - 32) * 5/9))
    conversation1 = 'C'
else:
    print("Invalid temperature unit.")
    exit()
print(f"{degrees} degrees {conversion.upper()} = {result} degrees {conversation1}")
#print("\n\r")