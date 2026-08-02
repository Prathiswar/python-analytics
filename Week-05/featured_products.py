products = {
    "P101" : {
        "Name": "Laptop",
        "Rating": 4.9,
        "Stock": 22      
    },
    "P102" : {
        "Name": "Mobile",
        "Rating": 4.2,
        "Stock": 18
    },
    "P103" : {
        "Name": "Airpods",
        "Rating": 4.0,
        "Stock": 9
    },
    "P104" : {
        "Name": "Charger",
        "Rating": 4.5,
        "Stock": 8
    }   
}
for pro_id, details in products.items():
    if details["Rating"] >= 4.8 and details["Stock"] < 5:
        print(details["Name"], "Best Seller")
    elif details["Rating"] >= 4.5 or details["Stock"] < 10:
        print(details["Name"],"Recommended")
    else:
         print(details["Name"],"Regular Product")