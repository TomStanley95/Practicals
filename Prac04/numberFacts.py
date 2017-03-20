__author__ = 'Tom Stanley'


def main():
    numbers = []
    for i in range(0, 5):
        numbers.append(int(input("Number: ")))

    facts(numbers)


def facts(numbers):
    average_of_numbers = sum(numbers) / len(numbers)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}". format(average_of_numbers))


main()
