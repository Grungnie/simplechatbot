from chatterbot import ChatBot
import os

chatbot = ChatBot(
    'Smart Harry',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
    database=os.environ['MONGO_DATABASE_NAME'],
    database_uri=os.environ['MONGO_DATABASE_URI']
)

if os.environ['ENVIRONMENT'] == 'PROD':
    # Pull down the full vocab and train
    import subprocess
    process = subprocess.Popen("git clone https://github.com/gunthercox/chatterbot-corpus.git", shell=True)
    process.wait()
    chatbot.train('chatterbot-corpus.chatterbot_corpus.data.english')
    subprocess.Popen("rm -R chatterbot-corpus", shell=True)
else:
    # Train based on the local corpus
    chatbot.train('chatterbot.corpus.english')

chatbot = None