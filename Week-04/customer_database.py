customers = {
    "C101": {
        "Name": "Prathiswar",
        "City": "Pune",
        "Orders": 21,
        "Premium": True
    },
    "C102": {
        "Name": "Ramy",
        "City": "Hyderabad",
        "Orders": 11,
        "Premium": False
    },
    "C103": {
        "Name": "Reddy",
        "City": "Hyderabad",
        "Orders": 19,
        "Premium": True
    }
}

for cust_id, details in customers.items():
    print(cust_id)

    for key, value in details.items():
        print(key, ":", value)