__author__ = 'Tom Stanley'


def main():
    VALUE_MIN = 33
    VALUE_MAX = 127
    user_character = str(input("Enter a character: "))
    print("The ASCII code for {} is {}.".format(user_character, ord(user_character)))
    user_number = get_number(VALUE_MIN, VALUE_MAX)
    # user_number = int(input("Enter a number between {} and {}: ".format(VALUE_MIN, VALUE_MAX)))
    # while user_number < VALUE_MIN or user_number > VALUE_MAX:
    #     print("Please choose a number between {} and {}: ".format(VALUE_MIN, VALUE_MAX))
    #     user_number = int(input("Enter a number between {} and {}: ".format(VALUE_MIN, VALUE_MAX)))
    # else:
    print('The character for {} is {}'.format(user_number, chr(user_number)))
    for i in range(33, 127):
        print("{:>3} {:>2}".format(i, chr(i)))


def get_number(lower, upper):
    finished = False
    user_number = 0
    while not finished:
        try:
            user_number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            while user_number < lower or user_number > upper:
                print("Please choose a number between {} and {}: ".format(lower, upper))
                user_number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")
    return user_number

main()
