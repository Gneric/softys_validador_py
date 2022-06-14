from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
import json, sys


class upsertGroup(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content Type Error" }, 400

            data = request.json.get('data', None)
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            
        except:
            print(sys.exc_info())

class upsertProcess(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "No se encontro archivo excel adjunto" }, 400

            data = request.json.get('data', None)
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            # result = (groupID)
            # if structure == False:
            #     return { 'error': 'Error on structure return' }, 400
            # else:
            #     return structure, 200
        except:
            print(sys.exc_info())

class upsertProcess(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "No se encontro archivo excel adjunto" }, 400

            data = request.json.get('data', None)
            if data == "":
                return { 'error': 'data enviada vacia' }, 400

            # result = (groupID)
            # if structure == False:
            #     return { 'error': 'Error on structure return' }, 400
            # else:
            #     return structure, 200
        except:
            print(sys.exc_info())