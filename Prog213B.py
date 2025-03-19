class Quantity:
	def __init__(self, amount):
		self.amount = amount
		self.price = 0

	def calculate(self):
		if 0 < self.amount < 100:
			self.price = 5.95
		elif 100 <= self.amount < 200:
			self.price = 5.75
		elif 200 <= self.amount < 300:
			self.price = 5.4
		elif self.amount >= 300:
			self.price = 5.15


def main():
	amount = int(input("Enter amount of product bought "))
	q = Quantity(amount)
	q.calculate()
	print(amount * q.price)


if __name__ == "__main__":
	main()
