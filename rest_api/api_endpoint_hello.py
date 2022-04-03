from flask_restful import Resource


class ProjectWelcomeMessage(Resource):
    def get(self):
        return {
            'hello': 'world'
        }
