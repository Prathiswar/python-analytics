students = {
    "S101": {
        "Name": "Reddy",
        "CGPA": 4.0
    },
    "S102": {
        "Name": "Varun",
        "CGPA": 3.1
    },
    "S103": {
        "Name": "Prathiswar",
        "CGPA": 4.0
    }
}
for student_id, details in students.items():
    print(student_id)
    for key, value in details.items():
            print(key, ":", value)

