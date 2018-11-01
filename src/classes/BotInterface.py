import time
import Util

class BotInterface:
    def getUpdates(self, last_update_id):
        updates = []
        try:
            for update in bot.get_updates(offset=(last_update_id + 1), timeout=20):
                last_update_id = update.update_id
                updates.append(update)
        except Exception as exc:
            Util.log("Error -> "+ str(exc))
            time.sleep(1)
        return updates, last_update_id

    def ignore(self, update):
        return