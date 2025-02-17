radius = float(input("Enter the Radius: "))
pi = 3.14159


def circumference():
    cir = (2 * pi * radius)
    print("Circumference: ", cir)


def area():
    are = (pi * radius**2)
    print("Area: ", are)


def main():
    circumference()
    area()


if __name__ == "__main__":
    main()
