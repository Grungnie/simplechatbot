from chatterbot import ChatBot
import chatterbot

chatbot = ChatBot(
    'Smart Harry',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database='heroku_503f2tll',
    database_uri='mongodb://createuser:MatthewBrown@ds129600.mlab.com:29600/heroku_503f2tll'
)

# Train based on the english corpus

chatbot.train('chatterbot.corpus.english')
chatbot = None