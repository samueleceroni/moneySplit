class Backup():
	def save(self, object, name):
		with open('../../obj/' + name + '.pkl', 'wb') as f:
			pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)

	def load(self, name):
		with open('../../obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
