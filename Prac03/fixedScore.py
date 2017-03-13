__author__ = 'Tom Stanley'
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = grade(score)
    print(result)


def grade(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    else:
        if score < 50 > 0:
            result = "Bad"
        elif score > 50 < 90:
            result = "Passable"
        elif score > 90 < 100:
            result = "Excellent"
    return result

main()
