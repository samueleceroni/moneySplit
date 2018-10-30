class Chat:
	def __init__(self, name, key):
		self.__name = name
		self.__key = key
		self.__lists = {}		#{ 'lists_name' : [('price', 'description'),('price', 'description'),] }

	def addList(self, listname):
		if(self.__lists.contains_key(listname)):
			return False
		else:
			self.__lists[listname] = List(listname)
	    	return True

	def remList(self, listname):
	    if(self.__lists.contains_key(listname)):
	    	del self.__lists[listname]
			return True
	    else:
	    	return False

	def getListsName(self):
		rep = ""
		for record in self.__lists:
			rep += (record + "\n")
		return rep

	def getName(self):
		return self.__name

	def getKey(self):
		return self.__key

	def getList(self, listname):
		if(self.__lists.contains_key(listname)):
			return self.__lists[listname]
		else:
			return None