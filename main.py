from tasks import chat_bot_respond
from microsoftbotframework import MsBot
import logging


log_format = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
formatter = logging.Formatter(log_format)

streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
streamHandler.setFormatter(formatter)

logging.basicConfig(
    level=logging.INFO,
    format=log_format)

bot = MsBot()
bot.add_process(chat_bot_respond)

log = bot.logger
log.setLevel(logging.INFO)
log.addHandler(streamHandler)

if __name__ == '__main__':
    bot.run()
