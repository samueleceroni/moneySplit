import telegram as tel
import time
import datetime
import pickle

import tokens

token = tokens.try_troken
bot = tel.Bot(token)
databaseName = "database"

def main():
	print('started')
	print(bot.get_me())
	lastUpdateId = 0

	try:
		database = Backup.load(databaseName)
	except:
		Util.log("Warning -> noDatabaseFound, creating one...")
		database = Database()
		Backup.save(database, databaseName)

	while True:
		time.sleep(1)
		newUpdates, lastUpdateId = BotInterface.getUpdates(bot, lastUpdateId)

		for update in newUpdates:
			instruction = Parser(update) # if not able to parse, it parses an instruction to reply an error message
			Execute.run(instruction)

if __name__ == '__main__':
	main()