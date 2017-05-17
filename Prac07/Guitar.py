__author__ = 'Tom Stanley'


class Guitar():
    def __init__(self, name="", cost=0, year=0):
        self.name = name
        self.cost = cost
        self.year = year

    def __str__(self):
        vintage_string = ""
        if self.is_vintage():
            vintage_string = "(vintage)"
        return "{} ({}) , worth ${} {}".format(self.name, self.year, self.cost, vintage_string)

    def get_age(self):
        age = 2017 - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False

