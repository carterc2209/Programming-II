class idk:
    def __init__(self, less, big):
        with open("../Langdat/prog215a.dat", 'r') as f:
            self.less = int(f.readline())
            self.big = int(f.readline())

    def calc(self, less, big):
        amount = self.small + self.big
