from flask import Response
from flask_restful import Resource, reqparse

from modules.nlp_manager import ask_question_get_answer


class ChatbotAskQuestion(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        args = parser.parse_args()

        if len(args['question']) == 0:
            return Response("{ 'question' : 'empty' }", 422)

        return ask_question_get_answer(args['question'])
