# Write a Python program to calculate Body Mass Index (BMI). Take the user's weight (in kg) and height (in meters) as input.Formula: BMI = weight / (height × height)

def calculate_bmi(weight, height):
    return weight / (height * height)

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

bmi = calculate_bmi(weight, height)

print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")