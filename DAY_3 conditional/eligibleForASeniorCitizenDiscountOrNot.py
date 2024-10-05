#. Write a Python program to check if a person is eligible for a senior citizen discount (age >= 60).

def check_senior_citizen_discount(age):
    if age >= 60:
        return "You are eligible for a senior citizen discount."
    else:
        return "You are not eligible for a senior citizen discount."

age = int(input("Enter your age: "))

result = check_senior_citizen_discount(age)
print(result)