"""
CP1404/CP5632 - Practical
Shop Calculator with input validation and discount logic
"""

# Input validation loop for the number of items
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Calculate the total price of all items
total_price = 0.0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply a 10% discount if the total price is over $100
if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")