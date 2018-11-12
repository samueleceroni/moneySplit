from list import List
from item import Item
from util import Util

class Chat:
    def __init__(self, name, key):
        if type(name) is not str:
            raise AttributeError
        self.__name = name
        self.__key = key
        self.__lists = {}       #{ 'lists_name' : [('price', 'description'),('price', 'description'),] }

    def addList(self, listname):
        if type(listname) is not str:
            raise AttributeError
        if(listname in self.__lists):
            raise ValueError
        self.__lists[listname] = List(listname)

    def remList(self, listname):
        if type(listname) is not str:
            raise AttributeError
        if(listname in self.__lists):
            del self.__lists[listname]
        else:
            raise ValueError

    def getListsName(self):
        rep = []
        for record in self.__lists:
            rep.append(record)
        rep.sort()
        return rep

    def getName(self):
        return self.__name

    def getKey(self):
        return self.__key

    def getList(self, listname):
        if(listname in self.__lists):
            return self.__lists[listname]
        else:
            raise ValueError

'''
def main():
    myChat = Chat("myNewChat","123456789")
    for i in range(10):
        myChat.addList("newList"+str(i+1))
        for j in range (10):
            myChat.getList("newList"+str(i+1)).addElement(Item("newItem" + str(j+1), j+1))

    for listed in myChat.getListsName():
        Util.log(myChat.getList(listed).toString())
    myChat.remList("newList1")


if __name__ == '__main__':
    main()
'''