__author__ = 'Tom Stanley'

from Prac07.Guitar import Guitar


def error_check_number_input(value_name):
    """
    This function returns an error checked value, making sure it is a value - Imported from assignment 1 and modified
    """
    while True:
        # while loop ensures the input is actually a number
        try:
            value = int(input("Enter your guitars {}:".format(value_name)))
            return value
        except ValueError:
            print("Invalid input; enter a number please :)")


def main():
    user_guitars = []
    # guitar_name = input("Enter your guitars name:").strip().capitalize()
    # while guitar_name != "":
    #     guitar_cost = error_check_number_input("price")
    #     guitar_age = error_check_number_input("age")
    #     user_guitars.append(Guitar(guitar_name, guitar_cost, guitar_age))
    #     print("{} ({}) : $ {} added.".format(guitar_name, guitar_age, guitar_cost))
    #     guitar_name = input("Enter your guitars name:").strip().capitalize()
    user_guitars.append(Guitar("Gibson L-5 CES", 16035.40, 1922))
    user_guitars.append(Guitar("Line 6 JTV-59", 1512.9, 2010))
    print("These are my guitars")
    print([str(guitar) for guitar in user_guitars])
    guitar_count = 1
    for guitar in user_guitars:
        print("Guitar {} : {}".format(guitar_count, str(guitar)))
        guitar_count += 1


main()
