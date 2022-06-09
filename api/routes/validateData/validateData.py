import json
import sys
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request
from api.services.mySqlConn import checkProcessID, getProcessStructure

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
            
            processID = request.json.get('processID', None)
            if processID == "":
                return { 'error': 'processID enviado no aceptado' }, 400

            results = checkProcessID(processID)
            if results == False:
                return { 'error': 'El proceso ingresado no se encuentra disponible' }, 400

            structure = getProcessStructure(processID)
            if structure == False:
                return { 'error': 'Error en la busqueda del proceso' }, 400
                  
            response = validateFile(file, structure)
            return response
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400