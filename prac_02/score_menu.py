"""
CP1404/CP5632 - Practical
Program with a menu for score checking
"""

Menu = """G- get a valid score
P- print result
S- show stars    
Q- quit """


def main():
    score = get_valid_score()
    print(Menu)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print(get_stars(score))
        else:
            print("Invalid choice")
        print(Menu)
        choice = input(">>>").upper()
    print("Thank you ")


def get_valid_score():
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_stars(score):
    stars = "*" * int(score // 10)
    return stars


main()