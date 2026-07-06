"""
CP1404/CP5632 - Practical
Program for Sales Bonus conversion
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        sales_bonus = sales * 0.1
        print(f"Bonus is: ${sales_bonus:.2f}")
    else:
        sales_bonus = sales * 0.15
        print(f"Bonus is: ${sales_bonus:.2f}")
    sales = float(input("Enter sales: $"))

