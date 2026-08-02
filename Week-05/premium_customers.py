customers = {
    "CUS101": {
         "Name": "Prathiswar",
         "City": "Pune",
         "Premium": "Yes"   
    },
    "CUS102": {
        "Name": "Reddy",
        "City": "Hyderabad",
        "Premium": "No"
    },
    "CUS103": {
        "Name": "Vansh",
        "City": "Ludhiana",
        "Premium": "Yes"
    }
}
for cus_id, details in customers.items():
    if details["Premium"] == "Yes":
        print(details["Name"],"VIP customer")
    elif details["Premium"] == "Yes" or details["City"] == "Mumbai":
        print(details["Name", "Premium customer"])
    else: 
        print(details["Name"], "Regular customer")