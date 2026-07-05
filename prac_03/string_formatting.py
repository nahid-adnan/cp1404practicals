"""
CP1404/CP5632 Practical-String formatting examples
Name: B M Nahid Hasan Adnan
Date: 05/07/2026
"""

year = 1922
guitar_model = "Gibson L-5 CES"
price = 16036.18

print(f"{year} {guitar_model} for about ${price:,.0f}!")


for i in range(0, 11):
    print(f"2 ^{i:2} is {2 ** i:4}")

