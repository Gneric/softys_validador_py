import json
import sys
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from api.services.mysqlConnection.checkData import getCheckCustomProcedure
from api.services.mysqlConnection.getData import getTargetTable
from api.services.sqlConnection.sqlConn import deleteTemporalTable, executeProcedure, selectTempIntoTable

from api.tools.DataSend import sendData

class insertData(Resource):
    @jwt_required()
    def post(self):
        try:
            token = get_jwt_identity()
            dquoted = json.dumps(eval(token))
            json_token = json.loads(dquoted)
            credentials = json_token.get('credentials')

            if request.content_type == None:
                return { 'error': 'Content Type error' }, 400

            processID = request.json.get('processID', "")
            if processID == "":
                return { 'error': 'processID enviado vacio' }, 400
            targetTable = getTargetTable(processID)

            result = selectTempIntoTable(credentials, processID, targetTable)
            if result != 1:
                return { 'error': 'error en la insercion de data' }, 400
            del_res = deleteTemporalTable(credentials, processID)
            if del_res != 1:
                return { 'error': 'error eliminando la tabla temporal' }, 400

            customProcedures = getCheckCustomProcedure(processID)
            if customProcedures != '':
                check = executeProcedure(customProcedures)
                if check != True:
                    return { 'error': f'error executing {customProcedures}' }, 400

            return { 'result': 'ok' }, 200
        except:
            print(sys.exc_info())
            return { 'error': 'unkown error' }, 400