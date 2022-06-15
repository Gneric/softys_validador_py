from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import json, sys

from api.services.mysqlConnection.insertData import insertNewProcess, upsertGroup, upsertProcess, upsertValidation


class upsertGroups(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            data = request.json.get('data', "")
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            token = get_jwt_identity()
            dquoted = json.dumps(eval(token))
            json_token = json.loads(dquoted)
            clientID = json_token.get('clientID')

            result = upsertGroup(data, clientID)
            if result == False:
                return { 'error': 'error en la creacion/actualizacion de grupo' }, 400

            return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())

class upsertProcesses(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            data = request.json.get('data', "")
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            result = upsertProcess(data)
            if result == False:
                return { 'error': 'error en la creacion/actualizacion de grupo' }, 400

            return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())

class upsertValidations(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            data = request.json.get('data', "")
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            result = upsertValidation(data)
            if result == False:
                return { 'error': 'error en la creacion/actualizacion de grupo' }, 400

            return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())

class newProcess(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            data = request.json.get('data', "")
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            result = insertNewProcess(data)
            if result == False:
                return { 'error': 'error en la creacion/actualizacion de grupo' }, 400

            return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())