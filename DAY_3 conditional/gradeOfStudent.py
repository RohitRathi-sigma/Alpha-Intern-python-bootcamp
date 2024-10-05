#Write a Python program that calculates the grade of a student based on their marks. Criteria: Marks >= 90: `A+;   Marks >= 80: `A`;  Marks >= 70: `B+`;  Marks >= 60: `B`;  Marks >= 50: `C`;  Else: `Fail`

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

marks = float(input("Enter the marks obtained by the student: "))

grade = calculate_grade(marks)

print(f"The grade for marks {marks} is: {grade}")