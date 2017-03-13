__author__ = 'Tom Stanley'
temp_file = open("name.txt", "r")
name = temp_file.readline()
print("Your name is {}".format(name))
temp_file.close()
