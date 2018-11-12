import pickle

class Backup():
	def save(self, object, databaseName):
		with open('../../obj/' + name + '.pkl', 'wb') as f:
			pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)

	def load(self, databaseName):
		with open('../../obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def main():
	a = 3
	b = 4
	Backup.save(a,"aVar")
	Backup.save(a,"bVar")
	a = Backup.load("aVar")
	b = Backup.load("bVar")
	print a+b


if __name__ == '__main__':
    main()
