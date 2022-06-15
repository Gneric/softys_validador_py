from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api.tools.DataSend import sendData

class insertData(Resource):
    @jwt_required()
    def post(self):
        if request.content_type == None:
            return { "error" : "No se encontro data adjunta" }, 400
        if 'data' in request.json.keys():
            data = request.json.get('data', [])
            if len(data) < 1:
                return { "error" : "La data adjunta se encuentra vacia" }, 400     
                         
            response = sendData(data)
            return response
        else:
            return { "error" : "No se encontro data adjunta" }, 400

        
        
        
        
        
