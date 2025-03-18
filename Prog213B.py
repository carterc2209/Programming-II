class Quantity:
	def __init__(self, amount, price):
		self.amount = amount
		self.price = price

	def calculate(self):
		if 0 < self.amount < 100:
			price = 5.95
		elif 100 <= self.amount < 200:
			price = 5.75
		elif 200 <= self.amount < 300:
			price = 5.4
		elif self.amount >= 300:
			price = 5.15
		total = price * self.amount


def main():
	amount = int(input("Enter amount of product bought"))
	print(amount)
