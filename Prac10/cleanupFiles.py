"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'


def main():
    print("Current directory is", os.getcwd())
    # change to desired directory
    os.chdir('Lyrics')
    # print a list of all files (test)
    # print(os.listdir('.'))
    # make a new directory
    # os.mkdir('temp')
    for dir_name, subdir_list, file_list in os.walk('.'):
        #     print("Currently sorting files in {}".format(dir_name))
        #     # loop through each file in the (original) directory
        for filename in os.listdir(dir_name):
            # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                os.rename(filename, new_name)


def get_fixed_filename(name):
    # not_fixed_name = "SilentNight.txt"
    # not_fixed_name = "ItIsWell (oh my soul).txt"
    # not_fixed_name = "o little town of bethlehem.txt"
    not_fixed_name = name
    new_name = " "
    for letter in not_fixed_name:
        if letter.isupper():
            new_name += " " + letter.lower()
        else:
            new_name += letter
    not_fixed_name = new_name
    not_fixed_name = not_fixed_name.split(" ")
    new_name = ""
    for word in not_fixed_name:
        word = word.capitalize()
        new_name += " " + word
    new_name = new_name.strip().replace(" ", "_").replace(".TXT", ".txt")
    return new_name

main()
# Processing subdirectories using os.walk()

# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)