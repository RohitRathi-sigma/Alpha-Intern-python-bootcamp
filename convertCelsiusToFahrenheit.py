#Take a temperature in Celsius as input from the user and convert it to Fahrenheit using the formula:• Formula: Fahrenheit = (Celsius × 9/5) + 32.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"The temperature in Fahrenheit is: {fahrenheit}")
