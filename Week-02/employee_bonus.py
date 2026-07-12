print("------------------------------")
print("   EMPLOYEE_BONUS_REPORT")
print("------------------------------")

employee_name = input("Employee: ")
Attendance = int(input("Attendance: "))
Performance = int(input("Performance: "))
if Attendance >= 90 and Performance >= 4:
    print("Bonus Status: Eligible")
else:
    print("Bonus Status: Not Eligible")
print("------------------------------")


print("------------------------------")
print("EMPLOYEE_ACCESS_SYSTEM")
print("------------------------------") 
employee_name = input("Employee: ")
age = int(input("Age: "))
id_validity = (input("ID Validity (Yes/No): "))
if id_validity.lower() == "yes" and age >= 18:
    print("Access Status: Granted")
else:
    print("Access Status: Denied , Please contact HR.")