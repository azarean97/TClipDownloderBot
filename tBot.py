from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

import json

with open('./myToken.text','r') as tokenfile:
    myToken = tokenfile.readline().strip('\n')
print(myToken)
myBotUsername = '@clipDownloaderBot'

#############




#############
def main():
    #start app
    application = Application.builder().token(myToken).build()
    #add commands

    #run
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()