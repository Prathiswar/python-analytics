employees = {
    "E101" : {
        "Name" : "Prathiswar",
        "Department": "IT",
        "Salary": 100000
    },
    "E102" : {
        "Name" : "Reddy",
        "Department" : "Marketing",
        "Salary" : 100000
    }
}
for emp_id, details in employees.items():
    if details["Department"] == "IT" and details["Salary"] > 70000:
        print(details["Name"])