#Take the radius of a circle from the user and calculate the area and circumference.• Formula:Area = π × radius²;  Circumference = 2 × π × radius.

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

radius = float(input("Enter the radius of the circle: "))

area = calculate_area(radius)
circumference = calculate_circumference(radius)

print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")
