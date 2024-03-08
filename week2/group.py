import math

# Area of a square.
length = int(input("Enter the length of the square: "))
area_of_square = length ** 2
print(f"The area of the square is {area_of_square:.1f}")

# Area of a rectangle.
length_of_rectangle = int(input("Enter the length of the rectangle: "))
width_of_rectangle = int(input("Enter the width of the rectangle: "))
area_of_rectangle = length_of_rectangle * width_of_rectangle
print(f"The area of the rectangle is: {area_of_rectangle:.1f}")

# Area of a circle.
radius_of_circle = int(input("Enter the radius of the circle: "))
area_of_circle = math.pi * radius_of_circle**2
print(f"The area of the circle is: {area_of_circle:.1f}")