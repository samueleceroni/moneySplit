class Parser:
	# command
	# idChat -
	# listname
	# amount
	# description
	# keyToDelete
	# supposeOnlyOneList

	def __init__(self, update):
		text = update['message']['text']
	    self.__idChat = update['message']['chat']['id']
	    words = text.split(' ')
	    firstIsNumber = False

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
