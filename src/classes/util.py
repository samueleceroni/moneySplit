import datetime

class Util:

	__logFileName = "log"

	def log(logMessage):
		now = datetime.datetime.now()
		with open('../../res/' + Util.__logFileName + '.txt', 'a') as logFile:
			logFile.write("[" + now.strftime("%Y-%m-%d %H:%M:%S" + "]: " +\
						  "{" + logMessage + "}\n\n"))

def main():
	Util.log("Util.__logFileName is private and is not accessible")

if __name__ == '__main__':
	main()
