#Write a program to ask the user for a character and check if it is a vowel or consonant.

def check_vowel_or_consonant(char):
    char = char.lower()
    
    if char in 'aeiou':
        return "The character is a vowel."
    elif char.isalpha():  
        return "The character is a consonant."
    else:
        return "Invalid input. Please enter a letter."

character = input("Enter a character: ")

result = check_vowel_or_consonant(character)
print(result)