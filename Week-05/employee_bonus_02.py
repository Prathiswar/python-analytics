employees = {
    "E101" : {
        "Name" : "Prathiswar",
        "Salary" : 150000,
        "Department" : "IT"       
    },
    "E102" : {
        "Name" : "Reddy",
        "Salary": 85000,
        "Department": "HR"
    },
    "E101" : {
        "Name" : "Rahul",
        "Salary" : 77000,
        "Department" : "IT"       
    },
    "E102" : {
        "Name" : "Sneha",
        "Salary": 85000,
        "Department": "HR"
    }
}
for emp_id ,details in employees.items():
    if details["Salary"] >= 80000:
        print(details["Name"]), "gets Bonus"
    else: 
        print(details["Name"]), "does not get bonus"