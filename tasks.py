from microsoftbotframework.response import Response
import celery
from chatterbot import ChatBot
from chatterbot.conversation.session import ConversationSessionManager

# @celery.task()
# def respond_to_conversation_update(message):
#     if message["type"]=="conversationUpdate":
#         response = Response(message)
#         message_response = 'Have fun with the Microsoft Bot Framework'
#         response.reply_to_activity(message_response,recipient={"id":response["conversation"]["id"]})


def hello_world(message):
    if message["type"] == "message" and message["text"] == 'hello world':
        response = Response(message)
        response.reply_to_activity('Hi!')


# @celery.task()
def chat_bot_respond(message):
    if message["type"]=="message":
        global session_manager
        chatbot = ChatBot(
            'Smart Harry',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
#            storage_adapter="chatterbot.storage.MongoDatabaseAdapter"
        )

        response = Response(message)

        message_response = chatbot.get_response(message["text"]).text
        response.reply_to_activity(message_response)
