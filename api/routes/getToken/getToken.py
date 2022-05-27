from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask import request

from api.constants.api_user_config import config

class getToken(Resource):
    def post(self):
        try:
            if request.content_type == None:
                return { 'error': 'Content Type error' }, 400

            usr = request.json.get('user', None)
            pwd = request.json.get('password', None)

            if usr != config.get('user') or pwd != config.get('password'):
                return { 'error': 'credential error' }, 400

            access_token = create_access_token(identity=str(usr))
            
            return { 'result': { 'usr': usr, 'access_token': access_token } }, 200
        except Exception as err:
            print('Error getToken : ', err)
            return { 'error': 'unkown error' }, 400