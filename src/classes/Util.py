import datetime

class Util:
	def log(logMessage):
		now = datetime.datetime.now()
		print("[" + now.strftime("%Y-%m-%d %H:%M:%S" + "]: " + logMessage + '\n'))