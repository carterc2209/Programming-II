class Family:
    def __init__(self, less_20, a20_39, debug, test):
        self.less_20 = less_20
        self.a20_39 = a20_39
        self.debug = debug
        self.test = test
        self._family = 0
        self._percents = [0]*4  # [0,0,0,0]

    def _get_percent(self, number):
        return round((number/self._family) * 100, 2)

    def calculate(self):
        self._family = self.less_20 + self.a20_39 + self.debug + self.test
        self._percents[0] = self._get_percent(self.less_20)
        self._percents[1] = self._get_percent(self.a20_39)
        self._percents[2] = self._get_percent(self.debug)
        self._percents[3] = self._get_percent(self.test)

    def display(self):
        print("Category\t\tBudget")
        print(f"Less Than 20: {self._percents[0]}%")
        print(f"Between 20 and 39: {self._percents[1]}%")
        print(f"Debugging: {self._percents[2]}%")
        print(f"Testing: {self._percents[3]}%")
        print(f"Total amount spent: ${self._family:.2f}")


def main():
    print("Enter the amount spent last month on the following items:\n")
    less_20 = float(input("Designing: $"))
    a20_39 = float(input("Coding: $"))
    debug = float(input("Debugging: $"))
    test = float(input("Testing: $"))
    print()

    spending = Family(less_20, a20_39, debug, test)
    spending.calculate()
    spending.display()
    pass


if __name__ == "__main__":
    main()
