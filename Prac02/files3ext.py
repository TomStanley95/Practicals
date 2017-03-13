__author__ = 'Tom Stanley'
temp_file = open("numbers.txt", "r")
total = 0
for line in temp_file:
    number = int(line)
    total += number
print(total)
temp_file.close()
