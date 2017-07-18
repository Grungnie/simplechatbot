from microsoftbotframework import ReplyToActivity
import celery
from chatterbot import ChatBot
import os


@celery.task()
def chat_bot_respond_async(message):
    chat_bot_respond(message)


def chat_bot_respond(message):
    if message["type"]=="message":
        chatbot = ChatBot(
            'Smart Harry',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
            storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
            database=os.environ['MONGO_DATABASE_NAME'],
            database_uri=os.environ['MONGO_DATABASE_URI']
        )

        message_response = chatbot.get_response(message["text"]).text

        ReplyToActivity(fill=message,
                        text=message_response).send()

