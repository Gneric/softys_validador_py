from os import getcwd
import sys
from flask import send_from_directory
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request
from os.path import join

from api.services.mySqlConn import checkProcessID, getProcessStructure
from api.tools.createTemplate import createTemplate

from datetime import datetime

class downloadTemplate(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { 'error': 'Content Type error' }, 400          

            processID = request.json.get('processID', None)
            if processID == "":
                return { 'error': 'processID enviado no aceptado' }, 400

            results = checkProcessID(processID)
            if results == False:
                return { 'error': 'El proceso ingresado no se encuentra disponible' }, 400

            structure = getProcessStructure(processID)
            if structure == False:
                return { 'error': 'Error en la busqueda del proceso' }, 400
            
            xlsx = createTemplate(structure)
            if xlsx == '':
                return { 'error': 'Error en la creacion de la plantilla' }, 400

            data_path = join(getcwd(),'files')

            # Open a file with access mode 'a'
            with open(f"{data_path}/Archivos.txt", "a") as file_object:
                # Append 'hello' at the end of file
                file_object.write(f"\n Creacion de template - Archivo : {xlsx} - {datetime.now()}")

            result = send_from_directory(data_path, xlsx, as_attachment=True, environ=request.environ)
            return result
        except:
            print(sys.exec_prefix())
            return { 'error': 'error en endpoint downloadTemplate' }, 400


