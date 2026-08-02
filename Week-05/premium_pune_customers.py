customers = {
    "C101": {
        "Name": "Prathiswar",
        "City": "Pune",
        "Premium": "Yes"
    },
    "C102": {
        "Name": "Ramy",
        "City": "Hyderabad",
        "Premium": "No"
    },
    "C103": {
        "Name": "Reddy",
        "City": "Hyderabad",
        "Premium": "Yes"
    }
}

for cust_id, details in customers.items():
    if details["Premium"] == "Yes" and details["City"] == "Pune":
        print(details["Name"])