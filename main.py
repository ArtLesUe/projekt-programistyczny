from flask import Flask
from flask_restful import Api

from rest_api.api_endpoint_hello import ProjectWelcomeMessage
from rest_api.api_endpoint_learn_spam import ChatbotLearnSpamData
from rest_api.api_endpoint_learn_question import ChatbotLearnQuestionData
from rest_api.api_endpoint_ask_question import ChatbotAskQuestion
from rest_api.api_endpoint_ask_spam import ChatbotAskSpam


app = Flask(__name__)
api = Api(app)

api.add_resource(ProjectWelcomeMessage, '/')
api.add_resource(ChatbotLearnSpamData, '/learn/spam')
api.add_resource(ChatbotLearnQuestionData, '/learn/question')
api.add_resource(ChatbotAskQuestion, '/ask/question')
api.add_resource(ChatbotAskSpam, '/ask/spam')

if __name__ == '__main__':
    app.run()
