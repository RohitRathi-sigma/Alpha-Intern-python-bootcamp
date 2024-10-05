#Write a program to take the principal amount, rate of interest, and time from the user and calculate the simple interest.

def calculate_SI(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of interest: "))
time = float(input("Enter the Time (in years): "))

simple_interest = calculate_SI(principal, rate, time)

print(f"The Simple Interest is: {simple_interest}")