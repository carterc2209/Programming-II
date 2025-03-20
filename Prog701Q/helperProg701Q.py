class Vehicle:
    def __init__(self, name, tires):
        self._name = name
        self._tires = tires
    #
    # def get_name(self):
    #     return self._first + " " + self._last


class Cars(Vehicle):
    def __init__(self, name, tires, worth):
        super().__init__(name, tires)
        self.worth = worth


class Trucks(Vehicle):
    def __init__(self, name, tires, miles):
        super().__init__(name, tires)
        self.miles = miles


class Busses(Vehicle):
    def __init__(self, name, tires, home):
        super().__init__(name, tires)
        self.home = home
