from flask_restful import Resource


class ChatbotAskSpam(Resource):
    def post(self):
        return {
            'operation': 'success'
        }
