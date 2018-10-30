class List:
	def __init__ (self, listname):
		self.__lastItem = 0
		self.__items = {}
		self.__totalAmount = 0
		self.__listname = listname

	def addElement(self, newItem):
		self.__lastItem = self.__lastItem + 1
		self.__items[self.__lastItem] = newItem
		self.__totalAmount += newItem.getAmount()
		return True

	def remElement(self, id):
		if (self.__items.contains_key(id)):
			self.__totalAmount -= self.__items[id].getAmount()
			del self.__items[id]
			return True
		else:
			return False

	def clear(self):
		self.__lastItem = 0
		self.__items.clear()

	def toString(self):
		rep = "List " + self.__listname + '\n'
		for id in range(self.__lastItem):
			if(self.__items.contains_key(id)):
				rep += (id.toString() + ": ")
				rep += self.__items[id].toString()
				rep += '\n'