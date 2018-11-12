import pickle

class Backup():
	def save(object, databaseName):
		with open('../../res/' + databaseName + '.pkl', 'wb') as databaseFile:
			pickle.dump(object, databaseFile, pickle.HIGHEST_PROTOCOL)

	def load(databaseName):
		with open('../../res/' + databaseName + '.pkl', 'rb') as databaseFile:
			return pickle.load(databaseFile)

# TODO how to handle excpetion FileNotFoundException ? return null or try handle exceptions?

def main():
	a = 3
	b = 4
	Backup.save(a,"aVar")
	Backup.save(b,"bVar")
	a = Backup.load("aVar")
	b = Backup.load("bVar")
	print (a+b)


if __name__ == '__main__':
	main()
