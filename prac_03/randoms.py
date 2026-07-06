"""
CP1404/CP5632 Practical - Random numbers
Name: B M Nahid Hasan Adnan
Date: 05/07/2026
"""

import random

print(random.randint(5, 20))       # line 1
# Line 1: smallest possible is 5, largest possible is 20

print(random.randrange(3, 10, 2))  # line 2
# Line 2: possible values are 3, 5, 7, 9. Smallest is 3, largest is 9.
# It could NOT produce a 4, because it steps by 2 (3, 5, 7, 9) and skips even numbers.

print(random.uniform(2.5, 5.5))    # line 3
# Line 3: a decimal (float) between 2.5 and 5.5. Smallest possible 2.5, largest 5.5.

# Code to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))