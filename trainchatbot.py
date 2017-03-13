from chatterbot import ChatBot
import chatterbot

chatbot = ChatBot(
    'Smart Harry',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
)

# Train based on the english corpus

chatbot.train('chatterbot.corpus.english')
chatbot = None