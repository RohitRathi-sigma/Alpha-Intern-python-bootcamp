#Write a Python program to print the multiplication table of a number entered by the user up to 10.

num = int(input("Enter a number: "))

print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")