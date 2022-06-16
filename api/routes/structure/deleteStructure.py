from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
import json, sys

from api.services.mysqlConnection.deleteData import deleteGroup, deleteProcess, deleteValidation



class removeGroup(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            groupID = request.json.get('groupID', None)
            if groupID == "":
                return { 'error': 'groupID enviado no aceptado' }, 400

            result = deleteGroup(groupID)

            if result == False:
                return { 'error': f'Error on removing group {groupID}' }, 400
            else:
                return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400

class removeProcess(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            processID = request.json.get('processID', None)
            if processID == "":
                return { 'error': 'groupID enviado no aceptado' }, 400

            structure = deleteProcess(processID)
            if structure == False:
                return { 'error': f'Error on removing process {processID} ' }, 400
            else:
                return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400

class removeValidations(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            processID = request.json.get('processID', None)
            if processID == "":
                return { 'error': 'processID enviado no aceptado' }, 400

            structure = deleteValidation(processID)
            if structure == False:
                return { 'error': 'Error on structure return' }, 400
            else:
                return structure, 200
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400