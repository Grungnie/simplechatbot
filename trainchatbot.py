from chatterbot import ChatBot
import chatterbot
import pickle

build = False

chatbot = ChatBot(
    'Smart Harry',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
)

    # Train based on the english corpus
if build:
    chatbot.train('chatterbot.corpus.english')

# Get a response to an input statement
print(chatbot.get_response("Hello, how are you today?"))
print(chatbot.get_response("joke"))
