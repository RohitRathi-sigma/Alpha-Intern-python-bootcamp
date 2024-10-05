#Write a program to check whether a triangle is valid or not based on the sides provided by the user (sum of any two sides must be greater than the third side).

def is_triangle_valid(side1, side2, side3):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True  # Triangle is valid
    else:
        return False  # Triangle is not valid

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if is_triangle_valid(side1, side2, side3):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
