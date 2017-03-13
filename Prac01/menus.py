__author__ = 'Tom Stanley'
name = input('What is your name?')
choice = str(input('Menu \n(H)ello\n(G)oodbye\n(Q)uit\nWhat is your choice?').upper())
while choice != 'Q':
    if choice == 'H':
        print('Hello ' + name)
    elif choice == 'G':
        print('Goodbye ' + name)
    else:
        print('Invalid choice!Please pick again.')
    choice = str(input('Menu \n(H)ello\n(G)oodbye\n(Q)uit\nWhat is your choice?').upper())
print('Finished')

