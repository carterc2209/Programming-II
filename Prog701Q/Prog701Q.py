# from helperProg701Q import *


def main():
    try:
        people: list[Vehicle] = []
        with open("../Langdat/prog702q.txt", 'r') as f:
            num = f.readline()
            if num == 1:
                name = str(f.readline())
                tires = int(f.readline())
                worth = str(f.readline())
                print(name)
                print(tires)
                print(worth)
                # p = Cars(name, tires, worth)
                # people.append(p)
            elif num == 2:
                name = str(f.readline())
                tires = int(f.readline())
                miles = str(f.readline())
                worth = 50000 - (0.25 * miles)
                print(name)
                print(tires)
                print(worth)
                # people.append(p)
            elif num == 3:
                home = str(f.readline()).strip()
            # num = int(f.readline())

    except OSError as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
