from flask import Response
from flask_restful import Resource, reqparse

from modules.nlp_manager import learn_spam_new_data


class ChatbotLearnSpamData(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('textData', type=str, required=True)
        parser.add_argument('isSpam', type=str, required=True)
        args = parser.parse_args()

        if len(args['textData']) == 0:
            return Response("{ 'textData' : 'empty' }", 422)

        if args['isSpam'] != "spam" and args['isSpam'] != 'not-spam':
            return Response("{ 'isSpam' : 'only spam/not-spam allowed' }", 422)

        learn_spam_new_data(args['textData'], args['isSpam'] == "spam")

        return {
            'operation': 'success'
        }
