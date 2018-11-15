from commandsEnum import CommandsEnum

class Parser:
    # command
    # idChat
    # listname
    # amount
    # description
    # keyToDelete
    # supposeOnlyOneList

#    def __init__(self, update):
#        self.__idChat = update['message']['chat']['id']
#        #self.__chatName = update['message']['chat'][..]
#        entireText = update['message']['text']
    def __init__ (self, entireText):
        # if there is, delete '/' character
        if entireText[0]=='/':
            entireText = entireText[1:]
        # I split the entire text in words where separated by spaces
        self.__wordsText = Parser.__lowerUntilNumber(entireText.split(' '))

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
        self.__listname = Parser.__parseListName(self.__wordsText[1:])
        return

    def __parseRemList(self):
        self.__command = CommandsEnum.REM_LIST
        self.__listname = Parser.__parseListName(self.__wordsText[1:])
        return

    def __parseRemItem(self):
        self.__command = CommandsEnum.REM_ITEM
        if len(self.__wordsText) == 1:
            raise AttributeError("You have to insert the name of the list and the index of the item")
        try:
            checkDecimal = float(self.__wordsText[1])
            checkDecimal = checkDecimal % 1
            if checkDecimal != 0.0:
                raise AttributeError("The number is not an integer, please insert a correct index")
            self.__itemNumToDelete = int(self.__wordsText[1])
            self.__supposeOneList = True
            if len(self.__wordsText) > 2:
                raise AttributeError("You entered too many parameters dude!")
            return
        except ValueError: # the second word is not the number, so it is the name of the list
            pass
        if len(self.__wordsText) <= 2:
            raise AttributeError("You have to insert the name of the list and the index of the item")
        # the last word should be the number
        try:
            checkDecimal = float(self.__wordsText[len(self.__wordsText) - 1])
            checkDecimal = checkDecimal % 1
            if checkDecimal != 0.0:
                raise AttributeError("The number is not an integer, please insert a correct index")
            self.__itemNumToDelete = int(self.__wordsText[len(self.__wordsText) - 1])
            self.__supposeOneList = False
        except AttributeError as exc:
            raise exc
        self.__listname = Parser.__parseListName(self.__wordsText[1:-1])
        return
        
    def __parseShow(self):
        self.__command = CommandsEnum.SHOW_LIST
        self.__listname = Parser.__parseListName(self.__wordsText[1:])
        return

    def __parseTotal(self):
        self.__command = CommandsEnum.SHOW_TOTAL
        self.__listname = Parser.__parseListName(self.__wordsText[1:])
        return

    def __parseShowListsNames(self):
        self.__command = CommandsEnum.SHOW_ALL_LISTS_NAMES
        return

    def __parseAddItem(self):
        self.__command = CommandsEnum.ADD_ITEM
        try:
            checkNum = float(self.__wordsText[0])
            self.__amount = checkNum
            self.__supposeOneList = True
            self.__description = Parser.__parseDescription(self.__wordsText[1:])
            return
        except ValueError:
            pass
        #check if at least an element is the price
        for i in range(1, len(self.__wordsText) - 1):
            try:
                checkNum = float(self.__wordsText[i])
                self.__amount = checkNum
                self.__listname = Parser.__parseListName(self.__wordsText[:i])
                self.__description = Parser.__parseDescription(self.__wordsText[i+1:])
                return
            except ValueError: # normal, when the current word is not a number
                pass
            except Exception:
                raise Exception("Ops, something went wrong")
        raise Exception("Dude you didn't tell me any amount!")
    '''
        STATIC PRIVATE FUNCTIONS
    '''
    def __lowerUntilNumber(strVectWords):
        if type(strVectWords) == str:
            Util.log(strVectWords + " is a string, not an array of String")
            raise AttributeError("This is a string, not an array of String")
        for i in range(len(strVectWords)):
            try:
                float(strVectWords[i])
                break
            except ValueError:
                strVectWords[i] = strVectWords[i].lower()
        return strVectWords

    def __parseListName(strVectListName):
        listname = Parser.__linkWordsFromVector(strVectListName)
        if listname == '':
            raise AttributeError("I can't remove the list if I haven't the listname, dude")
        return listname

    def __parseDescription(strVectDescription):
        return Parser.__linkWordsFromVector(strVectDescription)

    def __linkWordsFromVector(strVect):
        linkedWords = ''
        for word in strVect:
            linkedWords += word
        return linkedWords
    '''
        GETTERS
    '''
    def getIdChat(self):
        return self.__idChat

    def getCommand(self):
        return self.__command

    def getListName(self):
        return self.__listname

    def getAmount(self):
        return self.__amount

    def getDescription(self):
        return self.__description

"""
AVAIABLE COMMAND:
ADD LIST -> add 'listname'

REM LIST -> rem 'listname'

ADD ITEM -> 'listname' 'price' 'description'

[(REM ITEM ->  del 'listname' 'price' 'description') || (REM ITEM ->  delete 'listname' 'price' 'description')] 

SHOW LIST -> show 'listname'

SHOW TOTAL LIST -> total 'listname'

"""


def main():
    queryString = "add sbornList"
    parsedQuery = Parser(queryString)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_LIST)
    print(parsedQuery.getListName() == "sbornlist")
    queryString = "Add sbornList"
    parsedQuery = Parser(queryString)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_LIST)
    print((parsedQuery.getListName() == "sbornList") == False)
    print("First test Completed : ADD_LIST\n")

    queryString = "sbornList 3 sbornDescription"
    parsedQuery = Parser(queryString)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_ITEM)
    print(parsedQuery.getListName() == "sbornlist")
    print(parsedQuery.getAmount() == 3.0)
    print(parsedQuery.getDescription() == "sbornDescription")
    print((parsedQuery.getDescription() == "sborndescription") == False)
    print("Second test Completed : ADD_ITEM\n")

''' queryString = "Add sbornList"
    parsedQuery = Parser(queryString)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_LIST)
    print((parsedQuery.getListName() == "sbornList") == False)
'''


if __name__ == '__main__':
    main()
