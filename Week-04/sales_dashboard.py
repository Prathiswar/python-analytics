products = {
    "P101": {
        "Product": "Laptop",
        "Price": 72000,
        "Stock": 11,
        "Rating": 4.1
    },
    "P102": {
        "Product": "Mobile",
        "Price": 65000,
        "Stock": 10,
        "Rating": 4.8
    },
    "P103": {
        "Product": "Keyboard",
        "Price": 7000,
        "Stock": 20,
        "Rating": 4.9
    },
    "P104": {
        "Product": "Mouse",
        "Price": 5500,
        "Stock": 25,
        "Rating": 4.5
    }
}
for prod_id, details in products.items():
    print(prod_id)

    for key, value in details.items():
        print(key, ":", value)


