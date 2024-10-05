#Take two numbers as input from the user and swap their values without using a third variable

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1, num2 = num2, num1

print(f"After swapping: First number = {num1}, Second number = {num2}")
