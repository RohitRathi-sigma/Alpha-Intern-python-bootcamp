#Write a Python program to check whether a number entered by the user is a palindrome or not using a loop.

def is_palindrome(n):
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10  
        reversed_num = reversed_num * 10 + digit  
        n //= 10 
    
    return original == reversed_num

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")