# Write a Python program to take a character as input from the user and print its ASCII value.

def get_asciiValue(character):
    return ord(character)

character = input("Enter a character: ")

if len(character) == 1:
    asciiValue = get_asciiValue(character)
    print(f"The ASCII value of '{character}' is: {asciiValue}")
else:
    print("Please enter a single character.")
