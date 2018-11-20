import telegram as tel
import tokens
import time
import Util

token = tokens.def_token

bot = tel.Bot(token)

class BotInterface:
    def getUpdates(last_update_id):
        updates = []
        try:
            for update in bot.get_updates(offset=(last_update_id + 1), timeout=20):
                last_update_id = update.update_id
                updates.append(update)
        except Exception as exc:
            Util.log("Error -> "+ str(exc))
            time.sleep(1)
        return updates, last_update_id

    def ignore(update):
        return

    def reply(update, repMessage):
        update.message.reply_text(repMessage) #TODO change to send message
