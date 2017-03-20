__author__ = 'Tom Stanley'
import random
number_of_picks = int(input("How many quick picks?"))
# Ask the user for the amount of quick picks to generate, then creates that many emtpy lists
quick_picks = []
for i in range(0, number_of_picks):
    quick_picks.append(0)
print(quick_picks)

random.randrange(0, 45)
