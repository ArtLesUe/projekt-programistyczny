from flask import Response
from flask_restful import Resource, reqparse

from modules.nlp_manager import learn_question_new_data


class ChatbotLearnQuestionData(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', type=str, required=True)
        parser.add_argument('answer', type=str, required=True)
        args = parser.parse_args()

        if len(args['question']) < 5:
            return Response("{ 'question' : 'too short, minimum 5 chars' }", 422)

        if len(args['answer']) < 5:
            return Response("{ 'answer' : 'too short, minimum 5 chars' }", 422)

        learn_question_new_data(args['question'], args['answer'])

        return {
            'operation': 'success'
        }
