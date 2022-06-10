import json
import sys
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import pandas as pd

from api.services.mySqlConn import getGroups, getProcesses, getValidations

class getListGroups(Resource):
    @jwt_required()
    def post(self):
        try:
            token = get_jwt_identity()
            dquoted = json.dumps(eval(token))
            json_token = json.loads(dquoted)
            clientID = json_token.get('clientID')
            structure = getGroups(clientID)
            if structure == False:
                return { 'error': 'Error on structure return' }, 400
            else:
                return structure, 200
        except:
            print(sys.exc_info())

class getListProcesses(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "No se encontro archivo excel adjunto" }, 400

            groupID = request.json.get('groupID', None)
            if groupID == "":
                return { 'error': 'groupID enviado no aceptado' }, 400

            structure = getProcesses(groupID)
            if structure == False:
                return { 'error': 'Error on structure return' }, 400
            else:
                return structure, 200
        except:
            print(sys.exc_info())

class getListValidations(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "No se encontro archivo excel adjunto" }, 400

            processID = request.json.get('processID', None)
            if processID == "":
                return { 'error': 'processID enviado no aceptado' }, 400

            structure = getValidations(processID)
            if structure == False:
                return { 'error': 'Error on structure return' }, 400
            else:
                return structure, 200
        except:
            print(sys.exc_info())