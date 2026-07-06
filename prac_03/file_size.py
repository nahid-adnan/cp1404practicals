"""
CP1404/CP5632 - Practical
File size and exception handling
Name: B M Nahid Hasan Adnan
Date: 07/07/2026
"""


def main():
    """Ask for filenames and report their line counts until the user enters nothing."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            number_of_lines = get_number_of_lines(filename)
            print(f"{filename} has {number_of_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def get_number_of_lines(filename):
    """Return the number of lines in the given file."""
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return len(lines)


main()
