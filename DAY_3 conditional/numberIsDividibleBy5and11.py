#Write a Python program to check whether a number is divisible by both 5 and 11.

def is_divisible_by_5_and_11(number):
    if number % 5 == 0 and number % 11 == 0:
        return True  
    else:
        return False  

number = int(input("Enter a number: "))

if is_divisible_by_5_and_11(number):
    print(f"{number} is divisible by both 5 and 11.")
else:
    print(f"{number} is not divisible by both 5 and 11.")