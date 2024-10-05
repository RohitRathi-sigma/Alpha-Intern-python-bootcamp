#Write a Python program to determine whether a person’s height (in cm) is considered short (<150), average (150-180), or tall (>180).

def categorize_height(height):
    if height < 150:
        return "Short"
    elif 150 <= height <= 180:
        return "Average"
    else:
        return "Tall"

height = float(input("Enter your height in cm: "))

result = categorize_height(height)
print(f"Your height is considered: {result}.")