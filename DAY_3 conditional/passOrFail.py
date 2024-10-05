#Write a program that asks the user to enter their exam score and prints whether they have passed or failed. The passing score is 40.

def check_pass_or_fail(score):
    if score >= 40:
        return "You have passed."
    else:
        return "You have failed."

score = float(input("Enter your exam score: "))

result = check_pass_or_fail(score)
print(result)