#Write a Python program to check if a given year is a century year (a year divisible by 100).

def is_century_year(year):
    if year % 100 == 0:
        return True  
    else:
        return False  

year = int(input("Enter a year: "))

if is_century_year(year):
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")