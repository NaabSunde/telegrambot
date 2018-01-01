from telegram.ext import Updater, CommandHandler
import os

#setup

#check if file is missing (=needs to be written)
while os.path.isfile("token") == 0:
    tokenfile = open("token", "x")
    usertokeninput = input("What is your bot's token?")
    tokenfile.write(usertokeninput)

#check if file is there, but it is empty (could be caused by ctrl+c while in setup)
while os.stat("token").st_size == 0:
    tokenfile = open("token", "x")
    usertokeninput = input("What is your bot's token?")
    tokenfile.write(usertokeninput)

#accept token and close the file
tokenfile = open("token", "r")
usertoken = tokenfile.readline()
updater = Updater(usertoken)
tokenfile.close()


#bot



def start(bot, update):
    update.message.reply_text(
        "Hello {}, my name is Watari! I have yet found a purpose for my existence, but I hope I'll soon find it!".format(update.message.from_user.first_name))



#handlers
updater.dispatcher.add_handler(CommandHandler('start', start))


#keep bot runnin'!
updater.start_polling()
updater.idle()
