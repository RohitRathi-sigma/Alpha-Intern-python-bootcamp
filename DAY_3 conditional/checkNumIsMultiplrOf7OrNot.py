#Write a Python program that takes a number and checks whether it is a multiple of 7 or not.

def is_multiple_of_7(number):
    if number % 7 == 0:
        return True  
    else:
        return False  

number = int(input("Enter a number: "))

if is_multiple_of_7(number):
    print(f"{number} is a multiple of 7.")
else:
    print(f"{number} is not a multiple of 7.")