import telegram as tel
import time
import datetime
import pickle

import tokens
# token to try this bot
#token = tokens.try_token

# future token
token = tokens.def_token

bot = tel.Bot(token)

'''
def get_updates(bot, last_update_id):
    updates = []
    try:
        for update in bot.get_updates(offset=(last_update_id + 1), timeout=20):
            last_update_id = update.update_id
            updates.append(update)
    except Exception as exc:
        now = datetime.datetime.now()
        print("Error -> "+ str(exc) + ': ' + now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(1)
    return updates, last_update_id
'''

def ignore(update):
    return

def main():
    print('started')
    print(bot.get_me())
    last_update_id = 0

    # try to load database from previous execution of the bot
    try:
        database = load_obj("database")
    except:
        database = {}
        # save the database in .pkl format
        save_obj(database, "database")

    while True:
        time.sleep(0.3)
        new_updates, last_update_id = get_updates(bot, last_update_id)

        for update in new_updates:
            try:
                reply(update, database)
                #ignore is used for testing and developing scope
                #ignore(update)
            except Exception as exc:
                now = datetime.datetime.now()
                print('Errore -> ' + str(exc) + ': ' + now.strftime("%Y-%m-%d %H:%M:%S"))
                print(update)

if __name__ == '__main__':
    main()
