#Write a Python program to calculate the sum of all the numbers from 1 to 100 using a for loop and the range function.
        
total_sum = 0

for num in range(1, 101):
    total_sum += num

print(f"The sum of all numbers from 1 to 100 is: {total_sum}")