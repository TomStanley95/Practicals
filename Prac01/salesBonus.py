__author__ = 'Tom Stanley'
""" Program to calculate and display a user's bonus based on sales. If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# .1 = 10%
sales_bonus_under_1000 = float(.1)
# .15 = 15%
sales_bonus_over_1000 = float(.15)
bonus = float(0)

sales = float(input("Enter sales: $"))
# if sales < 1000:
#     bonus = sales * sales_bonus_under_1000
#     print("Your sales bonus is ${:.2f}".format(bonus))
# else:
#     bonus = sales * sales_bonus_over_1000
#     print("Your sales bonus is ${:.2f}".format(bonus))
"""I was really confused by the use of the word 'until' at the end of the loop question.I couldn't find a way to do it
 without a while loop.
"""

while sales > 0:
    if sales < 1000:
        bonus = sales * sales_bonus_under_1000
        print("Your sales bonus is ${:.2f}".format(bonus))
        sales = float(input("Enter sales: $"))
    else:
        bonus = sales * sales_bonus_over_1000
        print("Your sales bonus is ${:.2f}".format(bonus))
        sales = float(input("Enter sales: $"))
else:
    print("You seem to have entered a negative number")





