__author__ = 'Tom Stanley'
"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac07.car import Car


def main():
    """Demo test code to show how to use car class."""
    # bus = Car(180)
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus.odometer)
    # print(bus)
    # print("Car {}, {}".format(bus.fuel, bus.odometer))
    # print("Car {self.fuel}, {self.odometer}".format(self=bus))
    limo = Car('Limo', 100)

    limo.fuel += 20
    print("{} has {self.fuel} fuel".format(limo.name, self=limo))
    limo.drive(115)
    print("{} has driven {self.odometer}".format(limo.name, self=limo))
    print(limo)


main()