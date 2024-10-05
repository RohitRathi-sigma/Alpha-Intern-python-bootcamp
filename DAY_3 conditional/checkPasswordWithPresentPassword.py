#Write a program to take a password from the user and check if it matches a preset password ("python123"). Print "Access granted" if the password matches, otherwise print "Access denied."

def check_password(user_password):
    preset_password = "python123"
    if user_password == preset_password:
        return "Access granted"
    else:
        return "Access denied"

user_password = input("Enter your password: ")

result = check_password(user_password)
print(result)
