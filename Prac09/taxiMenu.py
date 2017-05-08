__author__ = 'Tom Stanley'
from Prac09.Car import Taxi
from Prac09.Car import SilverServiceTaxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    print("Let's drive!")
    bill_to_date = 0
    menu_choice = get_valid_menu_choice()
    while menu_choice != 'q':
        if menu_choice == 'c':
            taxi_choice = choose_taxi()
            print(taxi_choice)
            # bill_to_date += taxi_choice.get_fare()
            bill_to_date += 0
            # Eliminated a previous issue I had where it was adding $4.50 prematurely by adding 0 each time.
            output_bill_to_date(bill_to_date)
            menu_choice = get_valid_menu_choice()
        else:
            bill_to_date += drive_taxi(taxi_choice, bill_to_date)
            output_bill_to_date(bill_to_date)
            menu_choice = get_valid_menu_choice()
    display_exit_message(bill_to_date)


def get_valid_menu_choice():
    valid_choice = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    while valid_choice not in ['q', 'c', 'd']:
        print("Invalid Menu choice.")
        valid_choice = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
    return valid_choice


def drive_taxi(taxi_choice, bill_to_date):
    taxi_choice.start_fare()
    fare_distance = int(input("Drive how far?"))
    taxi_choice.drive(fare_distance)
    print("Your {} will cost you ${:.2f}".format(taxi_choice.name, taxi_choice.get_fare()))
    fare = taxi_choice.get_fare()
    return fare


def output_bill_to_date(bill):
    print("Bill to date: ${:.2f}".format(bill))


def display_exit_message(bill_to_date):
    print("Total trip cost: ${:.2f}\nTaxis are now:".format(bill_to_date))
    list_taxis()


def list_taxis():
    # print([str(taxi) for taxi in taxis])
    for taxi in TAXIS:
        print("{} {}".format(TAXIS.index(taxi), taxi))


def choose_taxi():
    list_taxis()
    taxi_choice = int(input("Choose taxi:"))
    taxi = TAXIS[taxi_choice]
    return taxi
main()
