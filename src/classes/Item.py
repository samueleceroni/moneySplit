import datetime

class Item:
    def __init__(self, description, amount):
        self.__description = description
        self.__amount = amount
        #self.__time = now.strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        self.__time = now.strftime("%Y-%m-%d %H:%M")

    def getDescription(self):
        return self.__description

    def getAmount(self):
        return self.__amount

    def getTime(self):
        return self.__time

    def toStringVerbose(self):
        rep = "[" + str(self.__time) + "]: "
        rep += self.toString()

    def toString(self):
        return str(self.__amount) + "€ " + self.__description


def main():
    myItem = Item("prova", 1.0)
    print(str(myItem.getDescription()) + "\n")
    print(str(myItem.getAmount()) + "\n")
    print(myItem.getTime() + "\n")
    print(myItem.toString() + "\n")
    print(myItem.toStringVerbose() + "\n")



if __name__ == '__main__':
    main()
