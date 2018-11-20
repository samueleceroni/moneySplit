import time
import datetime
import pickle
import engine
from botinterface import BotInterface

# token to try this bot
#token = tokens.try_token

# future token

#seconds to wait to check for new updates
intervalTime = 1


def processUpdate(update):
    updateMessage = update['message']['text']
    updateIdChat = update['message']['chat']['id']
    replyMessage = ""
    # try to parse message
    try:
        updateParsed = Parser(updateMessage, updateIdChat)
    except (ValueError, AttributeError) as errMessage:
        replyMessage = errMessage
        return replyMessage
    except Exception as excError:
        Util.log(excError + ' ' + updateMessage)
        replyMessage = "Ops, something went wrong"
        return replyMessage

    # try to execute the parsed message
    try:
        replyMessage = engine.excecuteCommand(updateParsed)
    except (ValueError, AttributeError) as errMessage:
        replyMessage = errMessage
        return replyMessage
    except Exception as excError:
        Util.log(excError  + ' ' + updateMessage)
        replyMessage = "Ops, something went wrong"
        return replyMessage

    # return the obtained message
    if replyMessage == '':
        replyMessage = "Ops, something went wrong"
    return replyMessage


def ignore(update):
    return

def main():
    print('started')
    print(bot.get_me())
    lastUpdateId = 0

    while True:
        time.sleep(intervalTime)
        newUpdates, lastUpdateId = BotInterface.get_updates(lastUpdateId)

        for update in newUpdates:
            replyMessage = processUpdate(update)
            BotInterface.reply(update, replyMessage)

if __name__ == '__main__':
    main()
