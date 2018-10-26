
class User:
	__name = ""
	__key = ""
	__lists = {} #{ 'lists_name' : [('price', 'description'),('price', 'description'),] }
	
	def __init__(self, name, key):
		self.__name = name
		self.__key = key

	def addList(self, listname):
		if(self.__lists.contains_key(listname)):
			return False
		else:
			self.__lists[listname] = []
	    	return True

	def remList(self, listname):
		# TODO check if listname is present
	    if(self.__lists.contains_key(listname)):
	    	del self.__lists[listname]
			return True
	    else:
	    	return False

	def getLists(self):
		rep = ""
		for record in self.__lists:
			rep += (record + "\n")
		return rep

	def getName(self):
		return self.__name

	def getKey(self):
		return self.__key

