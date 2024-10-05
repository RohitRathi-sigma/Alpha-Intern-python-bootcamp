#Write a program that asks the user for their age and checks if they are eligible to vote (age >= 18).

def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

age = int(input("Enter your age: "))

result = check_voting_eligibility(age)
print(result)