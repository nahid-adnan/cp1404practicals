"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans:When the user types something that isn't a valid whole number for int() — like abc or 3.5 — because int() can't convert it.
2. When will a ZeroDivisionError occur?
Ans: When the denominator is 0, because dividing by zero is undefined
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: Yes, by checking if denominator != 0 before dividing
"""

try:

    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
