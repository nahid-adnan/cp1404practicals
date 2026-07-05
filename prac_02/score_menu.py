"""
CP1404/CP5632 - Practical
Program with a menu for score checking
"""

MENU = """G- get a valid score
P- print result
S- show stars    
Q- quit """


def main():
    """Run the score menu, letting the user get scores, check results, and see stars."""
    score = get_valid_score()
    print(MENU)
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
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you ")


def get_valid_score():
    """Get a valid score between 0 and 100 from the user."""
    score = float(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score


def get_result(score):
    """Work out and return the result category for a score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_stars(score):
    """Return a string of stars, one for each point in the score."""
    stars = "*" * int(score)
    return stars


main()
