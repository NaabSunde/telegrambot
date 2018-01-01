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
    print("Your token has been written into 'token' file")

#accept token and close the file
tokenfile = open("token", "r")
usertoken = tokenfile.readline()
updater = Updater(usertoken)
tokenfile.close()


#useful information about bot
print("Starting bot with username: @"+Bot.get_me(Bot(usertoken)).username)





#bot
dispatcher = updater.dispatcher

def start(bot, update):
    update.message.reply_text("Hello {}, my name is Watari! I have few functions for now, but I hope my master will come up with more tasks for me!".format(update.message.from_user.first_name))

def chuck(bot, update):
    update.message.reply_text(ChuckNorris().random().joke.replace("Chuck Norris", update.message.from_user.first_name))



#function: timer

def alarm(bot, job):
    bot.send_message(job.context, text='Beep-boop!')

def timer(bot, update):
    update.message.reply_text("Use /set <seconds> to set a timer!")

def set_timer(bot, update, args, job_queue, chat_data):
    chat_id = update.message.chat_id
    try:
        due = int(args[0])
        if due < 0:
            update.message.reply_text("I'm sorry, I can't set timer to the past..")
            return

        # Add job to queue
        job = job_queue.run_once(alarm, due, context=chat_id)
        chat_data["job"] = job

        update.message.reply_text('Timer has been set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

def unset(bot, update, chat_data):
    if 'job' not in chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Timer has been unset!')

#handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("chuck", chuck))
dispatcher.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
dispatcher.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
dispatcher.add_handler(CommandHandler("timer", timer))
#keep bot runnin'!
print("Bot running freely!")
if __name__ =="__main__":
    updater.start_polling()
    updater.idle()

    

