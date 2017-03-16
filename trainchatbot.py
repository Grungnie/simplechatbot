from chatterbot import ChatBot
import os

chatbot = ChatBot(
    'Smart Harry',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database=os.environ['MONGO_DATABASE_NAME'],
    database_uri=os.environ['MONGO_DATABASE_URI']
)

# Train based on the english corpus

chatbot.train('chatterbot.corpus.english')
chatbot = None