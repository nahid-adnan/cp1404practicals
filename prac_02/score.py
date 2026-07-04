"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    score = float(input("Enter your score :"))
    result = get_result(score)
    print(f"User {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")
    random_score = random.randint(0, 100)
    result = get_result(random_score)
    print(f"Random: {random_score} = {result}")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
