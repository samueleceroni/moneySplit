import telegram as tel
import time
import datetime

#insert here your token
token = ""

bot = tel.Bot(token)

sam = []
paolo = []


def AddToList (words):
    value = float (words[1])
    cause = ''
    for i, word in enumerate(words):
        if i !=0 and i != 1:
            cause += word + ' '
    if words[0] == '.sam':
        sam.append((value, cause))
    if words[0] == '.paolo':
        paolo.append((value, cause))


def show(words, update):
    rep = ''
    if words [1] == 'sam':
        rep = update['message']['chat']['first_name'] + ', ecco la lista di sam:\n'
        for value, cause in sam :
            rep += str(value) + '   ' + cause + '\n'


    elif words [1] == 'paolo':
        rep = update['message']['chat']['first_name'] + ', ecco la lista di paolo:\n'
        for value, cause in paolo :
            rep += str(value) + '   ' + cause + '\n'

    else:
        rep = 'Utente non valido.'

    update.message.reply_text(rep)

def total(words, update):
    rep = ''
    tot = 0
    if words[1] == 'sam':
        rep = update['message']['chat']['first_name'] + ', ecco il totale di sam:\n'
        for value, _ in sam:
            tot += value
        rep += str(tot)


    elif words[1] == 'paolo':
        rep = update['message']['chat']['first_name'] + ', ecco il totale di paolo:\n'
        for value, _ in paolo:
            tot += value
        rep += str(tot)

    else:
        rep = 'Utente non valido.'

    update.message.reply_text(rep)

def close(words):
    if words[1] == 'sam':
        sam.clear()
    if words[1] == 'paolo':
        paolo.clear()


def reply(update):
    text = update ['message']['text']
    if text[0] != '.':
        return

    words = text.split(' ')


    if words [0] == '.sam' or words[0] == '.paolo':
        try:
            float(words[1])
        except ValueError:
            update.message.reply_text('Sintassi Errata')
            return
        AddToList(words)
        update.message.reply_text(update['message']['chat']['first_name'] + ' ha aggiornato la lista di ' + words[0])

    elif words[0] == '.mostra':
        show(words, update)
        total(words, update)

    elif words[0] == '.totale':
        total(words, update)

    elif words[0] == '.chiudi':
        update.message.reply_text(update['message']['chat']['first_name'] + ' ha chiuso la lista di ' + words[1])
        close(words)

    else: update.message.reply_text('Comando non trovato')


def get_updates(bot, last_update_id):
    updates = []
    try:
        for update in bot.get_updates(offset=(last_update_id + 1), timeout = 999999):
            last_update_id = update.update_id
            updates.append(update)
    except:
        now = datetime.datetime.now()
        print("Server/Connection Error..." + now.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(1)
    return updates, last_update_id

def ignore(update):
    return

def main():
    print('started')
    print(bot.get_me())
    last_update_id = 0
    while True:
        #print('updating')
        time.sleep(0.3)
        new_updates, last_update_id = get_updates(bot, last_update_id)
        for update in new_updates:
            try:
                 reply(update)
                 #ignore(update)
            except:
                 now = datetime.datetime.now()
                 print('Errore... ' + now.strftime("%Y-%m-%d %H:%M:%S") )


if __name__ == '__main__':
    main()

"""
.sam "num" "causale"
.paolo "num" "causale"

.mostra "nomelista"
.totale "nomelista"
.chiudi "nomelista"

"""

