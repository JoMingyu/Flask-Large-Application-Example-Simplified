from flask import Blueprint, request
from flask_restful import Api, Resource

from app.views import json_required

api = Api(Blueprint('sample_api', __name__))
api.prefix = '/prefix'


@api.resource('/sample')
class Sample(Resource):
    @json_required('name', 'age')
    def post(self):
        return request.json
