__author__ = 'Tom Stanley'
name = str(input("What is your name? "))
temp_file = open("name.txt", "w")
print(name, file=temp_file)
temp_file.close()
