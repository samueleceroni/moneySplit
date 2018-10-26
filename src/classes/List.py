class List:
	__lastItem = 0
	__items = {}

	def __init_ (self):
		self.__lastItem = 0
		self.__items = {}

	def addElement(self, newItem):
		self.__lastItem = self.__lastItem + 1
		self.__items[self.__lastItem] = newItem
		return True

	def remElement(self, id):
		if (self.__items.contains_key(id)):
			del self.__items[id]
			return True
		else:
			return False

	def clear(self):
		self.__lastItem = 0
		self.__items.clear()
		return True