__author__ = 'Tom Stanley'
from Prac09.Car import SilverServiceTaxi
# from Prac09.Car import Taxi
#
# prius = Taxi("Prius 1", 100)
# prius.drive(40)
# print(prius)
# print("Your current fare is ${}".format(prius.get_fare()))
# prius.start_fare()
# prius.drive(100)
# print(prius)
# print("Your current fare is ${}".format(prius.get_fare()))
luxury_taxi = SilverServiceTaxi("Deluxe", 150, 2)
print(luxury_taxi)
luxury_taxi.drive(10)
print("Your current fare is ${:.2f}".format(luxury_taxi.get_fare()))