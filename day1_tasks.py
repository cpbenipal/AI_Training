# ------------------------------
# 1️⃣ Factorial Function
# ------------------------------
def factorial(n):
    """Calculate factorial of a number recursively."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")

print("\n" + "-"*30 + "\n")

# ------------------------------
# 2️⃣ Person Class with greet()
# ------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alice", 30)
print(person.greet())

print("\n" + "-"*30 + "\n")

# ------------------------------
# 3️⃣ Dictionary Product Filter
# ------------------------------
products = {
    "Laptop": 1500,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300,
    "Chair": 120
}

print("Products priced > $100:")
for product, price in products.items():
    if price > 100:
        print(f"{product}: ${price}")

print("\n" + "-"*30 + "\n")

# ------------------------------
# 4️⃣ File Handling: Reverse Lines
# ------------------------------
# Make sure input.txt exists with sample content
with open('input.txt', 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as file:
    for line in reversed(lines):
        print (line)
        file.write(line)

print("Lines from input.txt have been reversed and written to output.txt.")
