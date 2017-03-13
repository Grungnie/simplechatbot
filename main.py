import microsoftbotframework.runcelery
from microsoftbotframework.msbot import MsBot
from tasks import *

import trainchatbot

bot = MsBot()
#bot.add_process(hello_world)
bot.add_process(chat_bot_respond)
bot.run()
