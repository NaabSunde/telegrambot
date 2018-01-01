import os
from telegram import *
from telegram.ext import *
from chuck import ChuckNorris

#setup

#check if file is missing (=needs to be written)
if os.path.isfile("token") == 0 or os.stat("token").st_size == 0:
    tokenfile = open("token", "w")
    usertokeninput = input("What is your bot's token? ")
    tokenfile.write(usertokeninput)


#accept token and close the file
tokenfile = open("token", "r")
usertoken = tokenfile.readline()
updater = Updater(usertoken)
tokenfile.close()

#useful information about bot
print("Token:",usertoken)

print(Bot.get_me(Bot(usertoken)))

#bot

def start(bot, update):
    update.message.reply_text("Hello {}, my name is {}! I have yet found a purpose for my existence, but I hope I'll soon find it!".format(update.message.from_user.first_name, Bot.get_me(Bot(usertoken)).first_name))

def chuck(bot, update):
    update.message.reply_text(
ChuckNorris().random().joke.replace("Chuck Norris", update.message.from_user.first_name))



#handlers
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("chuck", chuck))

#keep bot runnin'!
if __name__ =="__main__":
    updater.start_polling()
    updater.idle()

    

