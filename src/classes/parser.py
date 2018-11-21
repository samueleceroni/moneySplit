from commandsEnum import CommandsEnum

class Parser:
    # command
    # idChat
    # listname
    # amount
    # description
    # keyToDelete
    # supposeOnlyOneList

    def __init__ (self, messageReceived, idChat):
        if type(messageReceived) is not str:
            Util.log("ParseError: parameter is not a string")
            raise AttributeError
        self.__idChat = idChat    
        # if there is, delete '/' character
        if messageReceived[0]=='/':
            messageReceived = messageReceived[1:]
        # I split the entire text in words where separated by spaces
        self.__wordsText = Parser.__lowerUntilNumber(messageReceived.split(' '))

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
            self.__parseShowListsNames() #TODO
            return

        self.__parseAddItem() #TODO
        return

    def __parseAddList(self):
        # "add listname"
        self.__command = CommandsEnum.ADD_LIST
        for i in range(1,len(self.__wordsText)):
            self.__wordsText[i] = self.__wordsText[i].lower()
        self.__listname = Parser.__linkWordsFromVector(self.__wordsText[1:])
        if self.__listname == "":
            raise AttributeError("I can't remove the list if I haven't the listname, dude")
        return

    def __parseRemList(self):
        self.__command = CommandsEnum.REM_LIST
        self.__listname = Parser.__linkWordsFromVector(self.__wordsText[1:])
        if self.__listname == "":
            raise AttributeError("I can't remove the list if I haven't the listname, dude")
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
            self.__supposeOneList = True
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
        self.__listname = Parser.__linkWordsFromVector(self.__wordsText[1:-1])
        return
        
    def __parseShow(self):
        self.__command = CommandsEnum.SHOW_LIST
        self.__listname = Parser.__linkWordsFromVector(self.__wordsText[1:])
        self.__supposeOneList = True if self.__listname == "" else False
        return

    def __parseTotal(self):
        self.__command = CommandsEnum.SHOW_TOTAL
        self.__listname = Parser.__linkWordsFromVector(self.__wordsText[1:])
        self.__supposeOneList = True if self.__listname == "" else False
        return

    def __parseShowListsNames(self):
        self.__command = CommandsEnum.SHOW_ALL_LISTS_NAMES
        if len(self.__wordsText) > 1:
            raise AttributeError("Command ls takes no parameters dude!")
        return

    def __parseAddItem(self):
        self.__command = CommandsEnum.ADD_ITEM
        try:
            checkNum = float(self.__wordsText[0])
            self.__amount = checkNum
            self.__supposeOneList = True
            self.__description = Parser.__linkWordsFromVector(self.__wordsText[1:])
            return
        except ValueError:
            self.__supposeOneList = False
            pass
        #check if at least an element is the price
        for i in range(1, len(self.__wordsText) - 1):
            try:
                checkNum = float(self.__wordsText[i])
                self.__amount = checkNum
                self.__listname = Parser.__linkWordsFromVector(self.__wordsText[:i])
                self.__description = Parser.__linkWordsFromVector(self.__wordsText[i+1:])
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

    def __linkWordsFromVector(strVect):
        linkedWords = ''
        for word in strVect:
            linkedWords += (word + ' ')
        return linkedWords[:-1] # I remove the last space character
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

    def getSupposeOneList(self):
        return self.__supposeOneList

    def getItemIdToRem(self):
        return self.__itemNumToDelete
"""
AVAIABLE COMMAND:
ADD LIST -> add 'listname'

REM LIST -> rem 'listname'

ADD ITEM -> 'listname' 'price' 'description'

[(REM ITEM ->  del 'listname' 'price' 'description') || (REM ITEM ->  delete 'listname' 'price' 'description')] 

SHOW LIST -> show 'listname'

SHOW TOTAL LIST -> total 'listname'

"""

"""
def main():
    idSborn = "1"
    queryString = "add sbornList"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_LIST)
    print(parsedQuery.getListName() == "sbornlist")
    queryString = "Add sbornList"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_LIST)
    print((parsedQuery.getListName() == "sbornList") == False)
    print("First test Completed : ADD_LIST\n")

    queryString = "Remlist sbornList"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.REM_LIST)
    print(parsedQuery.getListName() == "sbornlist")
    print("Second test Completed : REM_LIST\n")

    queryString = "Remitem sbornList 3"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.REM_ITEM)
    print(parsedQuery.getListName() == "sbornlist")
    print(parsedQuery.getSupposeOneList() == False)
    queryString = "Remitem sbornList 3.5"
    try:
        parsedQuery = Parser(queryString, idSborn)
        print(True == False)
    except AttributeError:
        print(True == True)
    queryString = "Remitem sbornList 3"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.REM_ITEM)
    print(parsedQuery.getListName() == "sbornlist")
    print(parsedQuery.getSupposeOneList() == False)
    queryString = "Remitem 3"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.REM_ITEM)
    print(parsedQuery.getSupposeOneList() == True)
    print("Second test Completed : REM_ITEM\n")

    queryString = "show sbornList"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.SHOW_LIST)
    print(parsedQuery.getListName() == "sbornlist")
    print(parsedQuery.getSupposeOneList() == False)
    queryString = "show"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.SHOW_LIST)
    print(parsedQuery.getSupposeOneList() == True)
    print("Third test Completed : SHOW_LIST\n")

    queryString = "total sbornList sbuRm"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.SHOW_TOTAL)
    print(parsedQuery.getListName() == "sbornlist sburm")
    print(parsedQuery.getSupposeOneList() == False)
    queryString = "TOTAL"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.SHOW_TOTAL)
    print(parsedQuery.getSupposeOneList() == True)
    print("Third test Completed : SHOW_TOTAL\n")

    queryString = "sbornList 3 sbornDescription"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.ADD_ITEM)
    print(parsedQuery.getListName() == "sbornlist")
    print(parsedQuery.getAmount() == 3.0)
    print(parsedQuery.getDescription() == "sbornDescription")
    print((parsedQuery.getDescription() == "sborndescription") == False)
    print("Third test Completed : ADD_ITEM\n")

    queryString = "ls"
    parsedQuery = Parser(queryString, idSborn)
    print(parsedQuery.getCommand() == CommandsEnum.SHOW_ALL_LISTS_NAMES)
    queryString = "ls sborn"
    try:
        parsedQuery = Parser(queryString, idSborn)
        print(True == False)
    except AttributeError:
        print(True == True)
    print("Third test Completed : SHOW_ALL_LISTS_NAMES\n")


if __name__ == '__main__':
    main()
"""