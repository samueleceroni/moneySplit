class Parser:
	# command
	# idChat
	# listname
	# amount
	# description
	# keyToDelete
	# supposeOnlyOneList

	def __init__(self, update):
	    self.idChat = update['message']['chat']['id']
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

	    self.__parseAddItem() #TODO
	    return

	def __parseAddList(self):
	def __parseRemList(self):
	def __parseRemItem(self):
	def __parseShow(self):
	def __parseTotal(self):
	def __parseAddItem(self):
	












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
