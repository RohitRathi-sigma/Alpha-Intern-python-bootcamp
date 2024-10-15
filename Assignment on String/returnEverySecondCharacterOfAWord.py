#Write a Python program that takes a string and returns every second character, starting from the first character, using advanced slicing.

def get_every_second_character(s):
    return s[::2]

input_string = "Alpha"
result = get_every_second_character(input_string)
print("String with every second character:", result)