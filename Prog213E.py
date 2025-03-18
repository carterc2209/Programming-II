class Family:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self._family = 0
        self._percents = [0]*4  # [0,0,0,0]

    def _get_percent(self, number):
        return round((number/self._family) * 100, 2)

    def calculate(self):
        self._family = self.first + self.second + self.third + self.fourth
        self._percents[0] = self._get_percent(self.first)
        self._percents[1] = self._get_percent(self.second)
        self._percents[2] = self._get_percent(self.third)
        self._percents[3] = self._get_percent(self.fourth)

    def display(self):
        print("Category\t\tBudget")
        print(f"Less Than 20: {self._percents[0]}%")
        print(f"Between 20 & 39: {self._percents[1]}%")
        print(f"Between 40 & 59: {self._percents[2]}%")
        print(f"Greater than 79: {self._percents[3]}%")
        print(f"Family Distributiont: {self._family:.2f}")


def main():
    print("Enter how many family members there are based off age:\n")
    first = float(input("Less Than 20: "))
    second = float(input("Between 20 & 39: "))
    third = float(input("Between 40 & 59: "))
    fourth = float(input("Greater than 79: "))
    print()

    spending = Family(first, second, third, fourth)
    spending.calculate()
    spending.display()
    pass


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
