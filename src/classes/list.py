from item import Item

class List:
    def __init__ (self, listname):
        if type(listname) is not str:
            raise AttributeError
        self.__listname = str(listname)
        self.__lastItem = 0
        self.__items = {}
        self.__totalAmount = 0.0
        
    def addElement(self, newItem):
        if type(newItem) is not Item:
            raise AttributeError
        self.__lastItem = self.__lastItem + 1
        self.__items[self.__lastItem] = newItem
        self.__totalAmount += newItem.getAmount()
        
    def remElement(self, id):
        if (id not in self.__items):
            raise UnboundLocalError
        self.__totalAmount -= self.__items[id].getAmount()
        del self.__items[id]

    def clear(self):
        self.__lastItem = 0
        self.__totalAmount = 0.0
        self.__items.clear()

    def toString(self):
        rep = "List " + self.__listname + '\n'
        rep += "Total: " + str(self.__totalAmount)
        for id in range(self.__lastItem):
            if(id in self.__items):
                rep += '\n'
                rep += (str(id) + ": ")
                rep += self.__items[id].toString()
        return rep

'''
from util import Util

def main():
    myList = List("newList")
    for i in range(10):
        nextItem = Item(str(i+1), float(i+1))
        myList.addElement(nextItem)
    Util.log(myList.toString())
    myList.remElement(5)
    Util.log(myList.toString())
    myList.clear()
    Util.log(myList.toString())


if __name__ == '__main__':
    main()
'''