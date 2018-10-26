class Item:
	__description = ""
	__amount = 0.0
	__time = ""

	def __init__(self, description, amount):
		self.__description = description
		self.__amount = amount
		#self.__time = now.strftime("%Y-%m-%d %H:%M:%S")
		self.__time = now.strftime("%Y-%m-%d %H:%M")

	def getDescription(self):
		return __description

	def getAmount(self):
		return __amount

	def getTime(self):
		return __time

	def toString(self):
		return "[" + __time + "]: " + __amount + "€ " + __description