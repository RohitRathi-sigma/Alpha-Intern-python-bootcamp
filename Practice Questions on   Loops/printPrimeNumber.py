#Write a Python program to print the prime numbers

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(limit):
    print(f"Prime numbers up to {limit}:")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=' ')
    print()  

limit = 25
print_primes(limit)