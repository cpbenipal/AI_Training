products = {
    "Laptop": 1500,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300,
    "Chair": 120
}

# Print products with price > 100
for product, price in products.items():
    if price > 300:
        print(f"{product}: ${price}")
