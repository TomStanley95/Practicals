__author__ = 'Tom Stanley'
import os, shutil


def get_file_type(file):
    if not os.path.isdir(file):
        file = file.split(".")
        file_type = file[1]
        return file_type
    else:
        pass


def main():
    print("Current directory is", os.getcwd())
    # change to desired directory
    os.chdir('FilesToSortV2')
    print("Current directory is", os.getcwd())
    discovered = []
    file_types = []
    categories = {}
    for filename in os.listdir("."):
        file_type = get_file_type(filename)
        if file_type in file_types:
            pass
        else:
            if file_type is None:
                pass
            else:
                file_types.append(file_type)
    for file_type in file_types:
        category = input("What category would you like to sort {} files into?".format(file_type)).strip()
        if category not in categories:
            categories[category] = [file_type]
            os.mkdir("./" + category)
        else:
            categories[category].append(file_type)
    # for filename in os.listdir("."):
    #     if not os.path.isdir(filename):
    #         file_type = get_file_type(filename)
    #         category = input("What category would you like to sort {} files into?".format(file_type)).strip()
    #         if category not in categories:
    #             categories[category] = [file_type]
    #             os.mkdir("./" + category)
    #         else:
    #             categories[category].append(file_type)
    print(file_types)
    print(categories)
    for filename in os.listdir("."):
        if not os.path.isdir(filename):
            if file_type in categories.get(category):
                shutil.move(filename, "./" + category)






        #         shutil.move(filename, "./" + category)
        #     else:
        #
        #         shutil.move(filename, "./" + category)
        #     print(categories)
        #     if file_type not in discovered:
        #         discovered.append(file_type)
        #     else:
        #
        #
        #         else:
        #             pass
        # else:
        #     pass


main()
