__author__ = 'Tom Stanley'
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score < 50 > 0:
        print("Bad")
    elif score > 50 < 90:
        print("Passable")
    elif score > 90 < 100:
        print("Excellent")
