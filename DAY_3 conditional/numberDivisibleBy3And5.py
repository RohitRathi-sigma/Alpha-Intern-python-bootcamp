#Write a Python program that takes a number from the user and checks if it is divisible by 3, 5, or both.

def check_divisibility(number):
    divisible_by_3 = (number % 3 == 0)
    divisible_by_5 = (number % 5 == 0)

    if divisible_by_3 and divisible_by_5:
        return "The number is divisible by both 3 and 5."
    elif divisible_by_3:
        return "The number is divisible by 3."
    elif divisible_by_5:
        return "The number is divisible by 5."
    else:
        return "The number is not divisible by 3 or 5."

number = int(input("Enter a number: "))

result = check_divisibility(number)
print(result)