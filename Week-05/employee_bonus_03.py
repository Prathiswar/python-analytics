employees = {
    "E101": {
        "Name" : "Prathiswar",
        "Salary" : 150000,
        "Department" : "IT"       
    },
    "E102": {
        "Name" : "Reddy",
        "Salary": 85000,
        "Department": "HR"
    },
    "E103": {
        "Name" : "Rahul",
        "Salary" : 77000,
        "Department" : "IT"       
    },
    "E104": {
        "Name" : "Sneha",
        "Salary": 85000,
        "Department": "HR"
    }
}

for emp_id, details in employees.items():
    if details["Salary"] >= 90000 and details["Department"] == "IT":
        print(details["Name"],"Platinum Bonus")
    elif details["Salary"] >= 80000 and details["Department"] == "IT":
        print(details["Name"],"Gold Bonus")
    else:
        print(details["Name"],"No Bonus")
    