__author__ = 'Tom Stanley'
temp_file = open("numbers.txt", "r")
number1 = int(temp_file.readline())
number2 = int(temp_file.readline())
print(number1 + number2)
temp_file.close()
