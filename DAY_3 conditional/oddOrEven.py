#Write a Python program to check whether a given number is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

number = int(input("Enter a number: "))

result = check_even_odd(number)
print(result)
