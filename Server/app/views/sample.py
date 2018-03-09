from flask import Blueprint
from flask_restful import Api, Resource

api = Api(Blueprint('sample_api', __name__))
api.prefix = '/prefix'


@api.resource('/sample')
class Sample(Resource):
    def get(self):
        return {
            'at': self.now,
            'msg': 'hello!'
        }
