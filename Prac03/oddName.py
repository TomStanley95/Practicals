__author__ = 'Tom Stanley'
"""Tom Stanley"""


def main():
    letters_to_skip = int(input("How many letters of your name would you like to skip each time?"))
    user_name = get_name()
    name_loop(user_name, letters_to_skip)


def name_loop(user_name, skip_variable):
    for i in range(1, len(user_name), skip_variable):
        print(user_name[i])


def get_name():
    user_name = str(input("Please enter your name:").strip(" "))
    while user_name == "":
        user_name = str(input("Your name cant be nothing.Please enter your name:").strip())
    return user_name


main()


