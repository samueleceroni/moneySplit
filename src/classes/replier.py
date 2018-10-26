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
