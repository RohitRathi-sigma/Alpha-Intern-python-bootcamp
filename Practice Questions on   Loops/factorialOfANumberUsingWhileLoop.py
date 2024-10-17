#Write a Python program to find the factorial of a number entered by the user using a while loop.

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
