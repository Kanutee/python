import math
temp_in_fahrenheit = int(input("Enter temperature in Fahrenheit: "))

temp_in_celsius = (temp_in_fahrenheit -32)*5/9

print(f'The temperature in Celsius is {math.ceil(temp_in_celsius)} degrees.')