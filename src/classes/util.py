import datetime
import pickle

class Util:

    __logFileName = "log"

    def __getActualMoment():
        return datetime.datetime.now()

    def log(logMessage):
        with open('../../res/' + Util.__logFileName + '.txt', 'a') as logFile:
            logFile.write("[" + Util.getTimeDetailed() + "]: " +\
                          "{" + logMessage + "}\n\n")
    def getTime():
        return Util.__getActualMoment().strftime("%Y-%m-%d %H:%M")

    def getTimeDetailed():
        return Util.__getActualMoment().strftime("%Y-%m-%d %H:%M:%S")


class Backup():
    def save(object, databaseName):
        with open('../../res/' + databaseName + '.pkl', 'wb') as databaseFile:
            pickle.dump(object, databaseFile, pickle.HIGHEST_PROTOCOL)

    def load(databaseName):
        with open('../../res/' + databaseName + '.pkl', 'rb') as databaseFile:
            return pickle.load(databaseFile)


def main():
    Util.log("Util.__logFileName is private and is not accessible")
    print(Util.getTime())
    print(Util.getTimeDetailed())
    #print(Util.__getActualMoment())
    

if __name__ == '__main__':
    main()
