if __name__ == "__main__":
    from microsoftbotframework import MsBot
    from tasks import *

    bot = MsBot(debug=True, verify_jwt_signature=False)
    bot.add_process(chat_bot_respond)
    bot.run()
