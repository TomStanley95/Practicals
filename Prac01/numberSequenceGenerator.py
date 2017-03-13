__author__ = 'Tom Stanley'
number_x = 1 + int(input('Pick number X:'))
number_y = 1 + int(input('Pick number Y:'))
even_numbers = str()
odd_numbers = str()
squared_numbers = str()
choice = input('Would you like to see?\n(E)ven numbers\n(O)dd numbers\n(S)quares\n(F)inish\n Make your selection:').upper()
while choice != 'F':
    if choice == 'E':
        for i in range(number_x, number_y):
            if i % 2 == 0:
                even_numbers += str(i) + ' '
        print(even_numbers)
        choice = input(
            'Would you like to see?\n(E)ven numbers\n(O)dd numbers\n(S)quares\n(F)inish\n Make your selection:').upper()
    elif choice == 'O':
        for i in range(number_x, number_y):
            if i % 2 != 0:
                odd_numbers += str(i) + ' '
        print(odd_numbers)
        choice = input(
            'Would you like to see?\n(E)ven numbers\n(O)dd numbers\n(S)quares\n(F)inish\n Make your selection:').upper()
    else:
        for i in range(number_x, number_y):
            square = i * i
            squared_numbers += str(square) + ' '
        print(squared_numbers)
        choice = input(
            'Would you like to see?\n(E)ven numbers\n(O)dd numbers\n(S)quares\n(F)inish\n Make your selection:').upper()
print('Program finished')
