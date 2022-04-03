from flask_restful import Resource


class ChatbotLearnQuestionData(Resource):
    def post(self):
        return {
            'operation': 'success'
        }
