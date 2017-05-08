__author__ = 'Tom Stanley'
from Prac09.taxiinheritance import Taxi

prius = Taxi("Prius 1", 100)
prius.drive(40)
print(prius)
print("Your current fare is ${}".format(prius.get_fare()))
prius.start_fare()
prius.drive(100)
print(prius)
print("Your current fare is ${}".format(prius.get_fare()))

