#Write a Python program to calculate the sum of all the digits of a number entered by the user using a loop.

def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        digit = n % 10  
        total_sum += digit  
        n //= 10 
    return total_sum

num = int(input("Enter a number: "))

if num < 0:
    num = -num

result = sum_of_digits(num)
print(f"The sum of the digits is: {result}")