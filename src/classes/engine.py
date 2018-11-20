from util import Backup
from util import Util
from database import Database
from commandsEnum import CommandsEnum
import messages

databaseName = "sborndb"

textParsed = None
database = None
chat = None

def executeCommand(updateParsed):
	if updateParsed.getCommand() == CommandsEnum.START:
		return Message.sendWelcome("")
	if updateParsed.getCommand == CommandsEnum.HELP:
		return messages.sendHelp()

	try:
		# if there is, load the database
		database = Backup.load(databaseName)
	except IOError:
		# create a database
		database = Database()
		Backup.save(database, databaseName)
		Util.log("New database created")
	except Exception:
		Util.log("Exception raised while loading the database - engine.py")
	
	textParsed = updateParsed
	# create chat if not present
	if not database.checkChat(textParsed.getIdChat()):
		database.addChat(textParsed.getIdChat())

	chat = database.getChat(textParsed.getIdChat())

	# execute the appropriate command
	commToSwitch = textParsed.getCommand()

	if commToSwitch == CommandsEnum.ADD_LIST:
		rep = __addList()
	elif commToSwitch == CommandsEnum.REM_LIST:
		rep = __remList()
	elif commToSwitch == CommandsEnum.ADD_ITEM:
		rep = __addItem()
	elif commToSwitch == CommandsEnum.REM_ITEM:
		rep = __remItem()
	elif commToSwitch == CommandsEnum.SHOW_LIST:
		rep = __showList()
	elif commToSwitch == CommandsEnum.SHOW_TOTAL:
		rep = __showTotal()
	elif commToSwitch == CommandsEnum.SHOW_ALL_LISTS_NAMES:
		rep = __showAllLists()
	else:
		rep = messages.sendHelp()

	return rep

def __addList():
	listname = textParsed.getListName()
	if not chat.checkList(listname):
		chat.addList(listname)
		return "List added"
	else:
		return "The list already exists"

def __remLIst():
	listname = textParsed.getListName()
	if chat.checkList(listname):
		chat.remList(listname)
		return "List removed"
	else:
		return "The list does not exist"

def __addItem():
	if textParsed.getSupposeOneList():
		if chat.getNumberOfList() == 0:
			return "Before adding an item you have to add a list! Try add \'listname\'"
		if chat.getNumberOfList() == 1:
			listname = chat.getTheOnlyListName()
		else:
			return "There is more than one list, please specify it"
	else:
		listname = textParsed.getListName()
		if not chat.checkList(listname):
			return "There is no such list!"
	itemToAdd = Item(textParsed.getDescription(), textParsed.getAmount())
	chat.getList(listname).addElement(itemToAdd)
	return "Item added!"

def __remItem():
	return
def __showList():
	return
def __showTotal():
	return
def __showAllLists():
	return