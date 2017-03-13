if __name__ == "__main__":
    import microsoftbotframework.runcelery
    from microsoftbotframework.msbot import MsBot
    from tasks import *
    import subprocess

    import trainchatbot

    # Start celery workers
    subprocess.Popen('celery -A microsoftbotframework.runcelery.celery worker --concurrency=10', shell=True)#--without-heartbeat --without-gossip

    bot = MsBot()
    #bot.add_process(hello_world)
    bot.add_process(chat_bot_respond)
    bot.run()
