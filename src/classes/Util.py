import datetime

logFileName="log"

class Util:
	def log(logMessage):
		now = datetime.datetime.now()
		with open('../../res/' + logFileName + '.txt', 'a') as logFile:
			logFile.write("[" + now.strftime("%Y-%m-%d %H:%M:%S" + "]: " + logMessage + '\n'))


def main():
	Util.log(logFileName)

if __name__ == '__main__':
	main()
