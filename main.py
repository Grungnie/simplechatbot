if __name__ == "__main__":
    from microsoftbotframework import MsBot
    from tasks import *
    import os

    # Train the bot if it hasn't already
    import trainchatbot

    bot = MsBot(port=int(os.environ['PORT']), debug=True)
    bot.add_process(chat_bot_respond_async)
    bot.run()
