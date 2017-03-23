__author__ = 'Tom Stanley'
import random
number_of_picks = int(input("How many quick picks? "))
# Ask the user for the amount of quick picks to generate.
quick_picks = []
# TODO Convert the two for loops into a list comprehension.
for i in range(0, number_of_picks):
    current_pick = []
    for n in range(0, 6):
        random_number = random.randrange(0, 46)
        # current_pick.append(random.randrange(0, 46))
        # generate a random number between 0 and 46, then checks if it already exists, if so generate a new number.
        while random_number in current_pick:
            random_number = random.randrange(0, 46)
        current_pick.append(random_number)
        current_pick.sort()

    quick_picks.append(current_pick)

for i in range(0, number_of_picks):
    print("{}".format(str(quick_picks[i]).strip('[]').replace(',', " ")))

