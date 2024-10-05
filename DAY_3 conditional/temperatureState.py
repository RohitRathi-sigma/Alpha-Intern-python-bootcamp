#Write a program that takes the temperature in Celsius and prints if it is "Hot" (>30°C), "Warm" (between 20°C and 30°C), or "Cold" (<20°C).
                                                    
def categorize_temperature(temperature):
    if temperature > 30:
        return "Hot"
    elif 20 <= temperature <= 30:
        return "Warm"
    else:
        return "Cold"

temperature = float(input("Enter the temperature in Celsius: "))

result = categorize_temperature(temperature)
print(f"The temperature is {result}.")