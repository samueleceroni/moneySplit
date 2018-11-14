from chat import Chat

class Database:
    def __init__(self):
        self.__chatSet = {}
        self.__totChat = 0

    def addChat(self, chatName, idChat):
        if type(idChat) is not str:
            raise AttributeError
        if type(chatName) is not str:
            raise AttributeError
        if idChat not in self.__chatSet:
            self.__chatSet[idChat] = Chat(chatName, idChat)
            self.__totChat += 1
        else:
            raise ValueError

    def removeChat(self, idChat):
        if type(idChat) is not str:
            raise AttributeError
        if idChat in self.__chatSet:
            del self.__chatSet[idChat]
            self.__totChat -= 1
        else:
            raise ValueError

    def checkChat(self, idChat):
        if type(idChat) is not str:
            raise AttributeError
        return idChat in self.__chatSet

    def getChat(self, idChat):
        if type(idChat) is not str:
            raise AttributeError
        if idChat not in self.__chatSet:
            raise ValueError
        return self.__chatSet[idChat]

'''
from item import Item
from util import Util
from util import Backup
import time

def main():
    myDatabase = Database()
    for k in range (10):
        myDatabase.addChat("myNewChat"+str(k),"123456789"+str(k))
        myChat = myDatabase.getChat("123456789"+str(k))
        #Util.log(myChat.getName())
        #Util.log(myChat.getKey())
        for i in range(10):
            myChat.addList("newList"+str(i+1))
            for j in range (10):
                myChat.getList("newList"+str(i+1)).addElement(Item("newItem" + str(j+1), j+1))
        #for listed in myChat.getListsName():
        #    Util.log(myChat.getList(listed).toString())

    thisMoment = time.time()
    Backup.save(myDatabase, "dat")
    myDatabase = Backup.load("dat")
    nextMoment = time.time()
    Util.log(str(nextMoment-thisMoment))

    for k in range (10):
        myChat = myDatabase.getChat("123456789"+str(k))
        Util.log(myChat.getName())
        Util.log(myChat.getKey())
        for listed in myChat.getListsName():
            Util.log(myChat.getList(listed).toString())


if __name__ == '__main__':
    main()
'''