from flask_restful import Resource


class ProjectWelcomeMessage(Resource):
    def get(self):
        return {
            'przedmiot': 'Projekt programistyczny',
            'kierunek': 'Informatyka',
            'grupa': 'Studia niestacjonarne',
            'rok': '2021/2022',
            'uczelnia': 'Uniwersytet Ekonomiczny',
            'autorzy': [
                'Artur Leśnik',
                'Alicja Pęgiel'
            ]
        }
