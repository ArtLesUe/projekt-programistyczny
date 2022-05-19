from flask import Response
from flask_restful import Resource, reqparse

from modules.nlp_manager import ask_is_text_a_spam


class ChatbotAskSpam(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('textData', type=str, required=True)
        args = parser.parse_args()

        if len(args['textData']) == 0:
            return Response("{ 'textData' : 'empty' }", 422)

        return ask_is_text_a_spam(args['textData'])
