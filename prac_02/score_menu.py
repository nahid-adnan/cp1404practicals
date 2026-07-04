"""
CP1404/CP5632 - Practical
Program with a menu for score checking
"""

Menu = """G- get a valid score
P- print result
S- show stars
Q- quit """

score = 0
print(Menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "G":
        score = float(input("Enter your score: "))
        print(score)
    elif choice == "P":
        if score < 0 or score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("passable")
        else:
            print("Bad")
    elif choice == "S":
        stars = "*" * int(score // 10)
        print(stars)
    else:
        print("Invalid option")
    print(Menu)
    choice = input(">>> ").upper()
print("Thank you")
