employees = {
    "EMP101": {
        "Name":"Rahul",
        "Department": "IT",
        "Salary": 75000
    },
    "EMP102": {
        "Name": "Priya",
        "Department": "HR",
        "Salary": 65000
    }
}

for emp_id, details in employees.items():
    if details["Salary"] > 70000:
     print(details["Name"])