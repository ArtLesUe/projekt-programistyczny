from flask import Flask
from flask_restful import Api

from rest_api.api_endpoint_hello import ProjectWelcomeMessage


app = Flask(__name__)
api = Api(app)

api.add_resource(ProjectWelcomeMessage, '/')

if __name__ == '__main__':
    app.run()
