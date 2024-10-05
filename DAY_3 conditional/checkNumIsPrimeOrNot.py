#Write a Python program that checks whether a given number is prime or not (for simplicity, check numbers up to 50).

def is_prime(number):
    if number <= 1:
        return False  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False 
    return True  

number = int(input("Enter a number (up to 50): "))

if 0 < number <= 50:
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
else:
    print("Please enter a number between 1 and 50.")