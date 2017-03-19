from chatterbot import ChatBot
import os
import subprocess

chatbot = ChatBot(
    'Smart Harry',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database=os.environ['MONGO_DATABASE_NAME'],
    database_uri=os.environ['MONGO_DATABASE_URI']
)


# Pull down the full vocab and train
process = subprocess.Popen("git clone https://github.com/gunthercox/chatterbot-corpus.git", shell=True)
process.wait()
chatbot.train('chatterbot-corpus.chatterbot_corpus.data.english')
subprocess.Popen("rm -R chatterbot-corpus", shell=True)

chatbot = None