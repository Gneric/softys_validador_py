import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from api.services.mySqlConn import checkRoles

class getRoles(Resource):
    @jwt_required()
    def post(self):
        try:
            token = get_jwt_identity()
            dquoted = json.dumps(eval(token))
            json_token = json.loads(dquoted)
            clientID = json_token.get('clientID')
            roles = checkRoles(clientID)
            if roles == '':
                return { 'error', 'error en el retorno de roles' }, 400
            return roles
        except:
            return { 'error', 'error en el retorno de roles' }, 400