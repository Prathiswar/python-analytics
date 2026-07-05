name = input("Enter the student's name: ")
student_class = input("Enter the class: ")
section = input("Enter the section: ")
roll_number = int(input("Enter your roll number: "))
marks = int(input("Enter the marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"


if grade == "F":
    result = "Fail"
else:
    result = "Pass"

print("------------------------------")
print("         Student Report")
print("------------------------------")
print("Name:", name)
print("Class:", student_class)
print("Section:", section)
print("Roll Number:", roll_number)
print("Marks:", marks)
print("Grade:", grade)
print("Result:", result) 