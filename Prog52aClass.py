class Shape:
    # Constructor: sets up class data
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self._area = 0  # _ prefix basically means 'private' so
        self._perim = 0  # it should only be called in the class

    #Mutator/Setter Method: modifies class data
    def calculate(self):
        self._area = self.length * self.width
        self._perim = 2 * self.length + 2 * self.width

    # Accessor/Getter Method(s)
    def get_area(self):
        return self._area

    def get_perim(self):
        return self._perim


def main():
    length = int(input("Enter Length:"))
    width = int(input("Enter Width: "))
    shape = Shape(length, width)
    shape.calculate()
    print("Area: ", shape.get_area())

if __name__ == "__main__":
    main()
