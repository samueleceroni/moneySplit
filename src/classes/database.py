class Database:
    def __init__(self):
        self.__chatSet = {}
        self.__totChat = 0

    def addChat(self, idChat, chatName):
        if(not self.__chatSet.contains_key(idChat)):
            self.__chatSet[idChat] = Chat(chatName, idChat)
            self.__totChat++
            return True
        else:
            return False

    def removeChat(self, idChat):
        if(self.__chatSet.contains_key(idChat)):
            del self.__chatSet[idChat]
            self.__totChat--
            return True
        else:
            return False

    def checkChat(self, idChat):
        return self.__chatSet.contains_key(idChat)