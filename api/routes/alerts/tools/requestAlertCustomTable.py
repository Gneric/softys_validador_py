import json

from api.constants.sql_tables_info import tables_info
from api.services.sqlConnection.sqlConn import executeProcedure

def requestAlertMaestroCustomTable(target_table):
    if target_table not in tables_info.keys():
        return { 'error': f'La tabla ingresada: {target_table}, no encontrada en el listado interno de tablas' }, 400
    chck = executeProcedure(target_table)
    if chck == False:
        return { 'error': 'Ocurrio un error en la obtencion de informacion' }, 400
    return { 'result': json.loads(chck) }, 200