import microsoftbotframework.runcelery
from microsoftbotframework.msbot import MsBot
from tasks import *

bot = MsBot()
#bot.add_process(respond_to_conversation_update)
bot.add_process(chat_bot_respond)
bot.run()
