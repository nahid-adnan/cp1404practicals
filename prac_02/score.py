"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    score = float(input("Enter your score :"))
    result = get_result(score)
    print(f" User {score} is {result}")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "passable"
    else:
        return "Bad"


main()
