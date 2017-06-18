from microsoftbotframework import ReplyToActivity
import celery
from chatterbot import ChatBot
from chatterbot.conversation.session import ConversationSessionManager
import os


@celery.task()
def chat_bot_respond(message):
    if message["type"]=="message":
        global session_manager
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
