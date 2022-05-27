import sys
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request

from api.tools.readExcelFile import validateFile

class validateData(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "No se encontro archivo excel adjunto" }, 400
            if 'excel_file' in request.files.keys():
                file = request.files.get('excel_file')
            else:
                return { "error" : "No se encontro archivo excel adjunto" }, 400
            response = validateFile(file)
            return response
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400