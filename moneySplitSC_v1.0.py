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


# Database is a dict of dict of list of tuples.
# Here is a guide line of how the database is implemented:
# database = { 'id_chat' : { 'lists_name' : [('price', 'description'),('price', 'description'),] } }

def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


def sendHelp():
    rep = sendWelcome("Opss.. Something went wrong")
    return rep

def sendWelcome(phrase):
    rep = str(phrase) + '\n\n'
    rep += "Here is a list of available commands:"
    rep += "\n\n"
    rep += "To add a new list:\nadd listname"
    rep += "\n\n"
    rep += "To remove an existing list:\nrem listname"
    rep += "\n\n"
    rep += "To add an item:\nlistname price description"
    rep += "\n\n"
    rep += "To show a list:\nshow listname"
    rep += "\n\n"
    rep += "To show the total of a list:\ntot listname || total listname"
    rep += "\n\n"
    rep += "To clear a list:\nclear listname || clr listname"
    rep += "\n\n"
    rep += "To list all created lists:\nls"
    rep += "\n\n"
    rep += "Enjoy Sborn :)\n"
    return rep


def addList(listname, id_chat, database):
    database[id_chat][listname] = []
    rep = "List created!"
    return rep


def remList(listname, id_chat, database):
    del database[id_chat][listname]
    rep = 'List removed!'
    return rep


def addItem(words, id_chat, database, is_one_list, first_is_number):
    description = ''
    if is_one_list == 0:
        listname = words[0]
    elif(is_one_list and first_is_number):
        listname = next(iter(database[id_chat].keys()))

    amount = float(words[1-(is_one_list and first_is_number)])
    
    for i, word in enumerate(words):
        if i > (1-(is_one_list and first_is_number)):
            description += word + ' '
    
    database[id_chat][listname].append((amount, description))
    rep = "List updated!"
    return rep


def showList(listname, id_chat, database):
    rep = 'Here is ' + listname + ' list:\n'
    for amount, description in database[id_chat][listname]:
        rep += str(amount) + ' ' + description + '\n'
    return rep


def showTotal(listname, id_chat, database):
    rep = 'Here is ' + listname + ' list total:\n'
    total = 0
    for amount, _ in database[id_chat][listname]:
        total += amount
    rep += str(total) + ' €'
    return rep


def clearList(listname, id_chat, database):
    rep = "List " + listname + " cleared!"
    database[id_chat][listname].clear()
    return rep


def add_chat(id_chat, database):
    database[id_chat] = {}
    return


def rem_chat(id_chat, database):
    if id_chat in database:
        del database[id_chat]
        rep = 'Chat eliminata. Puoi arrestare ed eliminare il bot!'
        return rep

def listLists(id_chat, database):
    rep = 'Here is the list of lists in this chat:\n'
    for listname in database[id_chat]:
        rep += listname +'\n'
    return rep

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


def ignore(update):
    return


def reply(update, database):

    # load database
    database = load_obj("database")

    text = update['message']['text']
    id_chat = update['message']['chat']['id']
    words = text.split(' ')
    is_one_list = 0
    first_is_number = 0
    rep = ''

    try:
        # if chatter never sent a message to this bot it creates its instance
        if id_chat not in database:
            add_chat(id_chat, database)
        # i try to do lower() to command and listname received to avoid trouble with casesensitive
        for i in range(len(words)):
            if i >= 2:
                break
            try:
                if isinstance(words[i], int) or isinstance(words[i], float):
                    break
                words[i] = words[i].lower()
            except:
                # except statement should happen only with an integer or something like that
                break

        if (len(database[id_chat]) == 1):
            is_one_list = 1
            
        try:
            float(words[0])
            first_is_number = 1
        except:
            pass

        # when not specifiend and when possible the listname is added automatically
        if ((is_one_list) and (len(words)==1) and (not first_is_number) and (words[0]!='add') and (words[0]!='sborn') and (words[0]!='ls') and (words[0] not in database[id_chat])):
            words.append(next(iter(database[id_chat].keys())))

        if ((len(database[id_chat])== 0) and words[0]!='sborn' and words[0]!='add' and words[0]!='ls') or ((len(words)== 1) and words[0]=='add'):
            rep = sendHelp();

        # add an item in one list
        elif (words[0] in database[id_chat]) or (is_one_list and first_is_number):
            rep = addItem(words, id_chat, database, is_one_list, first_is_number)

        elif words[0] == 'add':
            if words[1] not in database[id_chat]:
                rep = addList(words[1], id_chat, database)
            else:
                rep = "List already exist! Please enter another name."

        elif words[0] == 'rem':
            if words[1] in database[id_chat]:
                rep = remList(words[1], id_chat, database)
            else:
                rep = "List doesn't exist!"

        elif words[0] == 'show':
            if (words[1] in database[id_chat]):
                rep = showList(words[1], id_chat, database)
                rep += '\n'
                rep += showTotal(words[1], id_chat, database)
            else:
                rep = "List doesn't exist!"

        elif words[0] == 'tot' or words[0] == 'total':
            if words[1] in database[id_chat]:
                rep = showTotal(words[1], id_chat, database)
            else:
                rep = "List doesn't exist!"

        elif words[0] == 'clear' or words[0] == 'clr':
            if words[1] in database[id_chat]:
                rep = clearList(words[1], id_chat, database)
            else:
                rep = "List doesn't exist!"

        elif words[0] == 'sborn':
            rep = "You're a great Sborner!"
        
        elif words[0] == '/start':
            rep = sendWelcome("Hi! This is SplitMoney bot!")

        elif (words[0]=='ls'):
            rep = listLists(id_chat, database)

        else:
            rep = sendHelp()

    except Exception as exc:
        rep = sendHelp()
        now = datetime.datetime.now()
        print('Errore -> ' + str(exc) + ': ' + now.strftime("%Y-%m-%d %H:%M:%S"))
        print(update)

    update.message.reply_text(rep)

    # save the database in .pkl format
    save_obj(database, "database")
    
    # save a legible copy of database
    file = open("obj/database.txt", "w+")
    file.write(str(database))
    file.close()
    # print(database)


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

"""

AVAIABLE COMMAND:
ADD LIST -> add 'listname'

REM LIST -> rem 'listname'

ADD ITEM -> 'listname' 'price' 'description'

[(REM ITEM ->  del 'listname' 'price' 'description') || (REM ITEM ->  delete 'listname' 'price' 'description')] 

CLS LIST -> cls 'listname' || close 'listname'

SHOW LIST -> show 'listname'

SHOW TOTAL LIST -> total 'listname'

"""
