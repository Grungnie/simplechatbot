import microsoftbotframework.runcelery
from microsoftbotframework.msbot import MsBot
from tasks import *
import os

import trainchatbot

# Start celery workers
os.system('celery -A microsoftbotframework.runcelery.celery worker')

bot = MsBot()
#bot.add_process(hello_world)
bot.add_process(chat_bot_respond)
bot.run()
