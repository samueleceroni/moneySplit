import datetime
from util import Util

class Item:
    def __init__(self, description, amount):
        if type(description) is not str:
            raise AttributeError
        self.__description = description
        try:
            self.__amount = float(amount)
        except AttributeError:
            raise AttributeError
        #self.__time = Util.getDetailedTime()
        self.__time = Util.getTime()

    def getDescription(self):
        return self.__description

    def getAmount(self):
        return self.__amount

    def getTime(self):
        return self.__time

    def toStringVerbose(self):
        return "[" + str(self.__time) + "]: " + self.toString()

    def toString(self):
        return str(self.__amount) + "€ " + self.__description

'''
def main():
    myItem = Item("prova", "1.0")
    Util.log(str(myItem.getDescription()))
    Util.log(str(myItem.getAmount()))
    Util.log(myItem.getTime())
    Util.log(myItem.toString())
    Util.log(myItem.toStringVerbose())



if __name__ == '__main__':
    main()
'''