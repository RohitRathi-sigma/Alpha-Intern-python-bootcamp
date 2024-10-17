#Write a Python program to print the Fibonacci series up to n terms, where n is entered by the user.

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()

num_terms = int(input("Enter the number of terms: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    fibonacci(num_terms)