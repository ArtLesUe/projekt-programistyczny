from flask import Flask
from flask_restful import Api

from rest_api.api_endpoint_hello import ProjectWelcomeMessage
from rest_api.api_endpoint_learn_spam import ChatbotLearnSpamData
from rest_api.api_endpoint_learn_question import ChatbotLearnQuestionData
from rest_api.api_endpoint_ask_question import ChatbotAskQuestion


app = Flask(__name__)
api = Api(app)

api.add_resource(ProjectWelcomeMessage, '/')
api.add_resource(ChatbotLearnSpamData, '/learn/spam')
api.add_resource(ChatbotLearnQuestionData, '/learn/question')
api.add_resource(ChatbotAskQuestion, '/ask/question')

if __name__ == '__main__':
    app.run()
