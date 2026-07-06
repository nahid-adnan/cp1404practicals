"""
CP1404/CP5632 - Practical
File reading and writing exercises
Name: B M Nahid Hasan Adnan
Date: 07/07/2026
"""
# 1.
name = input(" Enter your name: ")
FILENAME = "name.txt"
out_file = open(FILENAME, 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open(FILENAME, 'r')
name = in_file.readline().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as number_file:
    first = int(number_file.readline())
    second = int(number_file.readline())
print(first + second)

# 4.
total = 0
with open("numbers.txt", 'r') as number_file:
    for line in number_file:
        total += int(line)
print(total)
