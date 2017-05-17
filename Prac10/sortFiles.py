__author__ = 'Tom Stanley'

import os, shutil


os.chdir("FilesToSort")
print("current DIR is", os.getcwd())
os.mkdir("./doc")
os.mkdir("./docx")
os.mkdir("./png")
os.mkdir("./gif")
os.mkdir("./txt")
os.mkdir("./xls")
os.mkdir("./xlsx")
os.mkdir("./jpg")

for filenames in os.listdir("."):
    if filenames.endswith(".doc"):
        shutil.move(filenames, "./doc")
    elif filenames.endswith(".docx"):
        shutil.move(filenames, "./docx")
    elif filenames.endswith(".docx"):
        shutil.move(filenames, "./docx")
    elif filenames.endswith(".png"):
        shutil.move(filenames, "./png")
    elif filenames.endswith(".gif"):
        shutil.move(filenames, "./gif")
    elif filenames.endswith(".txt"):
        shutil.move(filenames, "./txt")
    elif filenames.endswith(".xlsx"):
        shutil.move(filenames, "./xlsx")
    elif filenames.endswith(".xls"):
        shutil.move(filenames, "./xls")
    elif filenames.endswith(".jpg"):
        shutil.move(filenames, "./jpg")