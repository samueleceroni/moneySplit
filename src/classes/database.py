def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def add_chat(id_chat, database):
    database[id_chat] = {}
    return

def rem_chat(id_chat, database):
    if id_chat in database:
        del database[id_chat]
        rep = 'Chat eliminata. Puoi arrestare ed eliminare il bot!'
        return rep
