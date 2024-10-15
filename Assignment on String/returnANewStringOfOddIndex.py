#Write a Python program that extracts all the characters at odd indices from a given string and returns them as a new string.

def extract_odd_indices(s):
    return s[1::2]

input_string = "abcdefg"
result = extract_odd_indices(input_string)
print("String with odd index characters:", result)