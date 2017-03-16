if __name__ == "__main__":
    import microsoftbotframework.runcelery
    from microsoftbotframework.msbot import MsBot
    from tasks import *
    import subprocess

    # Train the bot if it hasn't already
    import trainchatbot

    bot = MsBot()
    bot.add_process(chat_bot_respond)
    bot.run()
