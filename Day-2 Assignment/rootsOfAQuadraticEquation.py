#Write a Python program to calculate the roots of a quadratic equation. The quadratic equation has the form ax2+bx+c=0ax^2 + bx + c = 0ax2+bx+c=0. You will take input values for aaa, bbb, and ccc from the user. The roots can be calclated using the formula: • D=b2−4acD = b^2 - 4acD=b2−4ac     • Root 1 = −b+D2a\frac{-b + \sqrt{D}}{2a}2a−b+D    • Root 2 = −b−D2a\frac{-b - \sqrt{D}}{2a}2a−b−D.

import math

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"The roots of the equation are: Root 1 = {root1}, Root 2 = {root2}")
elif D == 0:
    root = -b / (2 * a)
    print(f"The root of the equation is: Root = {root}")
else:
    print("The equation has no real roots.")