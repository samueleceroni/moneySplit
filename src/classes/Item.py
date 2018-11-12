import datetime

class Item:
	def __init__(self, description, amount):
		self.__description = description
		self.__amount = amount
		#self.__time = now.strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
		self.__time = now.strftime("%Y-%m-%d %H:%M")

	def getDescription(self):
		return self.__description

	def getAmount(self):
		return self.__amount

	def getTime(self):
		return self.__time

	def toStringVerbose(self):
		rep="[" + self.__time + "]: " + self.toString()

	def toString(self):
		return self.__amount + "€ " + self.__description