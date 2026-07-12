employee = input("Enter employee name: ")
attendance = int(input("Enter attendance percentage: "))
performance_rating = int(input("Enter performance rating (1-5): "))
if attendance >= 90:
    if performance_rating == 5:
        reward = "Employee is eligible for gold bonus"

    elif performance_rating == 4:
        reward = "Employee is eligible for silver bonus"

    elif performance_rating >= 3:
        reward = "Employee is eligible for regular bonus"
else:
    reward = "Employee is not eligible for any bonus "

print("------------------------------")
print("       Employee Rewards")
print("------------------------------")
print("Employee Name : ", employee)
print("Attendance    : ", attendance)
print("Performance   : ", performance_rating)
print("Reward        : ", reward)
print("------------------------------")
