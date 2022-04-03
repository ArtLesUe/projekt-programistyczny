from flask_restful import Resource


class ChatbotAskQuestion(Resource):
    def post(self):
        return {
            'operation': 'success'
        }
