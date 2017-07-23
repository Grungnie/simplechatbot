from microsoftbotframework import ReplyToActivity
import celery
from chatterbot import ChatBot
#from chatterbot.comparisons import jaccard_similarity, synset_distance, sentiment_comparison
import os
import subprocess

import logging
logger = logging.getLogger(__name__)


@celery.task()
def chat_bot_respond(message):
    if message["type"] == "message":
        chatbot = get_chatbot()
        if message['text'] == '!train_smart_harry':
            ReplyToActivity(fill=message,
                            text='I am learning!').send()
            train_smart_harry(chatbot)
            ReplyToActivity(fill=message,
                            text='I think I got smarter.').send()
        else:
            message_response = chatbot.get_response(message["text"]).text

            ReplyToActivity(fill=message,
                            text=message_response).send()


def train_smart_harry(chatbot):
    # Chatterbot Corpus
    process = subprocess.Popen("git clone https://github.com/gunthercox/chatterbot-corpus.git", shell=True)
    process.wait()
    chatbot.train('chatterbot-corpus.chatterbot_corpus.data.english')
    subprocess.Popen("rm -R chatterbot-corpus", shell=True)

    # Ubuntu Corpus
    #chatbot.train()

def get_chatbot():
    return ChatBot(
        'Smart Harry',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
        database=os.environ['MONGO_DATABASE_NAME'],
        database_uri=os.environ['MONGO_DATABASE_URI']
    )


# def get_chatbot():
#     return ChatBot(
#         'Smart Harry',
#         storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
#         #database=os.environ['MONGO_DATABASE_NAME'],
#         database='test_twitter',
#         database_uri=os.environ['MONGO_DATABASE_URI'],
#         logic_adapters=[
#             'chatterbot.logic.BestMatch',
#         ],
#         filters=["chatterbot.filters.RepetitiveResponseFilter"],
#         twitter_consumer_key=os.getenv("CONSUMER_KEY"),
#         twitter_consumer_secret=os.getenv("CONSUMER_SECRET"),
#         twitter_access_token_key=os.getenv("ACCESS_TOKEN"),
#         twitter_access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
#         trainer="chatterbot.trainers.TwitterTrainer",
#         logger=logger,
#     )
