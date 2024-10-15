#Write a Python function that takes a string and two indices, and extracts the characters between these indices in reverse order using advanced slicing.

def extract_and_reverse(s, start_idx, end_idx):
    return s[start_idx:end_idx][::-1]

input_string = "Alpha Intern"
start = 2
end = 7
result = extract_and_reverse(input_string, start, end)
print("Extracted and reversed substring:", result)