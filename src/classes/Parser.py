from commandsEnum import CommandsEnum

class Parser:
	# command
	# idChat
	# listname
	# amount
	# description
	# keyToDelete
	# supposeOnlyOneList

	def __init__(self, update):
	    self.__idChat = update['message']['chat']['id']
		#self.__chatName = update['message']['chat'][..]
		entireText = update['message']['text']
	    # if there is, delete '/' character
	    if entireText[0]=='/':
	    	entireText = entireText[1:]
	    # I split the entire text in words where separated by spaces
	    self.__wordsText = entireText.split(' ')

	    if self.__wordsText[0] == "add":
	    	self.__parseAddList() #TODO
	    	return

	    if self.__wordsText[0] == "remlist": #change in the API !!!
	    	self.__parseRemList() #TODO
	    	return

	    if self.__wordsText[0] == "remitem":
	    	self.__parseRemItem() #TODO
	    	return

	    if self.__wordsText[0] == "show":
	    	self.__parseShow() #TODO
	    	return

	    if self.__wordsText[0] == "total":
	    	self.__parseTotal() #TODO
	    	return

	    if self.__wordsText[0] == "ls":
	    	self.__parseTotal() #TODO
	    	return

	    self.__parseAddItem() #TODO
	    return

	def __parseAddList(self):
		# "add listname"
		self.__command = CommandsEnum.ADD_LIST
		self.__listname = ''
		for i in range(1, len(self.__wordsText) - 1)
			self.__listname += self.__wordsText[i]
		if self.__listname == '':
			raise AttributeError("I can't add list if I haven't the listname, dude")

	def __parseRemList(self):
		self.__command = CommandsEnum.REM_LIST
		self.__listname = ''
		for i in range(1, len(self.__wordsText) - 1)
			self.__listname += (self.__wordsText[i] + ' ')
		if self.__listname == '':
			raise AttributeError("I can't remove the list if I haven't the listname, dude")
		
	def __parseRemItem(self):
		self.__command = CommandsEnum.REM_ITEM
		try:
			self.__itemNumToDelete = float(words[1])
			self.__supposeOneList = True
			if len(self.__wordsText) > 2:
				raise AttributeError("You entered too many parameters dude!")
			return
		except ValueError:
			pass
		
		
	def __parseShow(self):
		self.__command = CommandsEnum.SHOW_LIST
		
	def __parseTotal(self):
		self.__command = CommandsEnum.SHOW_TOTAL
		
	def __parseAddItem(self):
		self.__command = CommandsEnum.ADD_ITEM

	def __parseShowListsNames(self):
		self.__command = CommandsEnum.SHOW_ALL_LISTS_NAMES
		
	

	def getIdChat(self):
		return self.__idChat

	def getCommand(self):
		return self.__command









	    # lower the command and the listname
	    for i in range(2):
	    	try:
	    		if isinstance(words[i], int) or isinstance(words[i], float):
	    			break
	    		words[i] = words[i].lower()
	    	except:
	    		break

	    # check if the first word of the message is a number
	    # this should happen only when adding an item in a single-list chat
	    try:
	    	float(words[0])
	    	firstIsNumber = True
	    except:
	    	pass
	    
	    if firstIsNumber:
	    	self.__command = 


	def isACommand(self, command):
"""

AVAIABLE COMMAND:
ADD LIST -> add 'listname'

REM LIST -> rem 'listname'

ADD ITEM -> 'listname' 'price' 'description'

[(REM ITEM ->  del 'listname' 'price' 'description') || (REM ITEM ->  delete 'listname' 'price' 'description')] 

SHOW LIST -> show 'listname'

SHOW TOTAL LIST -> total 'listname'

"""
