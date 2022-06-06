import json
import sys
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import pandas as pd

from api.services.mySqlConn import getWholeStructure

class getStructure(Resource):
    @jwt_required()
    def post(self):
        try:
            token = get_jwt_identity()
            dquoted = json.dumps(eval(token))
            json_token = json.loads(dquoted)
            clientID = json_token.get('clientID')
            structure = getWholeStructure(clientID)
            if structure == False:
                return { 'error': 'Error on structure return' }, 400
            else:
                return structure, 200
        except:
            print(sys.exc_info())