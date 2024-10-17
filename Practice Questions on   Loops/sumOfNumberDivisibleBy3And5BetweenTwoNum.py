#Write a Python program to find the sum of all numbers between 1 and 1000 that are divisible by 3 or 5.

def sum_divisible_by_3_or_5():
    total_sum = 0
    for num in range(1,30):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    return total_sum

result = sum_divisible_by_3_or_5()
print(f"The sum of all numbers between 1 and 30 that are divisible by 3 or 5 is: {result}")