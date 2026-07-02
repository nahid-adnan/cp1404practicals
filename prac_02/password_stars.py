"""CP5632 Practical 02 - Password Checker with Stars
Name: B M Nahid Hasan Adnan
Date: 30/06/2026 """


MIN_LENGTH = 6


def main():
    password = get_password()
    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password() -> str:
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("password is too short")
        password = input("Enter your password: ")
    return password


main()
