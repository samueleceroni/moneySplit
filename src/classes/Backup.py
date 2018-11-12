import pickle

class Backup():
	def save(object, databaseName):
		with open('../../obj/' + databaseName + '.pkl', 'wb') as f:
			pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)

	def load(databaseName):
		with open('../../obj/' + databaseName + '.pkl', 'rb') as f:
			return pickle.load(f)

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
