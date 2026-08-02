students = {
    "S101": {
        "Name": "Reddy",
        "CGPA": 4.0,
        "Attendance": 95
    },
    "S102": {
        "Name": "Varun",
        "CGPA": 3.1,
        "Attendance": 77
    },
    "S103": {
        "Name": "Prathiswar",
        "CGPA": 4.0,
        "Attendance": 99
    }
}
for student_id, details in students.items():
    if details["CGPA"] >= 3.8 and details["Attendance"] >= 95:
        print(details["Name"],"Full Scholarship")
    elif details["CGPA"] >= 3.5 and details["Attendance"] >= 90:
        print(details["Name","Partial Scholarship"])
    else:
         print(details["Name"],"No Scholarship")