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