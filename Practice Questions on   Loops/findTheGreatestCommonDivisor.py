#Write a Python program to find the GCD (Greatest Common Divisor) of two numbers entered by the user using a loop.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)

print(f"The GCD of {num1} and {num2} is: {result}")