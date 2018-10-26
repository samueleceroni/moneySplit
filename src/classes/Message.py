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
