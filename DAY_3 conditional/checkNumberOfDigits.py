#Write a program that takes a number from the user and checks if it is a single-digit, double-digit, or more.

def categorize_number(num):
    if 0 <= num < 10:
        return "Single-digit"
    elif 10 <= num < 100:
        return "Double-digit"
    else:
        return "More than two digits"

number = int(input("Enter a number: "))

result = categorize_number(number)
print(f"The number is: {result}.")