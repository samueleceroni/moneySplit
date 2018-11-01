class Parser:
	# command
	# idChat
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
	    	    
	    for i in range(len(words)):
	    	if i >= 2:
	    		break
	    	try:
	    		if isinstance(words[i], int) or isinstance(words[i], float):
	    			break
	    		words[i] = words[i].lower()
	    	except:
	    		break

	    try:
	    	float(words[0])
	    	firstIsNumber = True
	    except:
	    	pass
	    
	    if not firstIsNumber:
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
