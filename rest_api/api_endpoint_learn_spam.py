from flask_restful import Resource


class ChatbotLearnSpamData(Resource):
    def post(self):
        return {
            'operation': 'success'
        }
