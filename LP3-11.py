class Budget:
    def __init__(self, design, code, debug, test):
        self.design = design
        self.code = code
        self.debug = debug
        self.test = test
        self._budget = 0
        self._percents = [0]*4  # [0,0,0,0]

    def _get_percent(self, number):
        return round((number/self._budget) * 100, 2)

    def calculate(self):
        self._budget = self.design + self.code + self.debug + self.test
        self._percents[0] = self._get_percent(self.design)
        self._percents[1] = self._get_percent(self.code)
        self._percents[2] = self._get_percent(self.debug)
        self._percents[3] = self._get_percent(self.test)

    def display(self):
        print("Category\t\tBudget")
        print(f"Designing: {self._percents[0]}%")
        print(f"Coding: {self._percents[1]}%")
        print(f"Debugging: {self._percents[2]}%")
        print(f"Testing: {self._percents[3]}%")
        print(f"Total amount spent: ${self._budget:.2f}")


def main():
    print("Enter the amount spent last month on the following items:\n")
    design = float(input("Designing: $"))
    code = float(input("Coding: $"))
    debug = float(input("Debugging: $"))
    test = float(input("Testing: $"))
    print()

    spending = Budget(design, code, debug, test)
    spending.calculate()
    spending.display()
    pass


if __name__ == "__main__":
    main()
