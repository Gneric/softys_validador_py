import sys
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api.routes.alerts.tools.requestAlertCustomTable import requestAlertMaestroCustomTable

class getAlerts(Resource):
    @jwt_required()
    def post(self):
        try:
            if request.content_type == None:
                return { "error" : "Content type error" }, 400
            if 'target_table' in request.json.keys():
                target_table = request.json.get('target_table', [])
                if target_table == "":
                    return { "error" : "La tabla enviada es un texto vacio" }, 400
                response = requestAlertMaestroCustomTable(target_table)
                return response
            else:
                return { "error" : "No se encontro tabla especificada" }, 400
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400