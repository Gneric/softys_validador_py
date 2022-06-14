import pandas as pd

from api.services.sqlConnection.sqlConn import insertToTable, executeNamedProcedure

from api.constants.sql_tables_info import carga_info

def sendData(data):
    try:
        df = pd.DataFrame(data)
        sendCheck = insertToTable(df)
        if sendCheck == False:
            return { 'error', 'error en la insercion de data' }, 400
        else:
            info = carga_info.get('insertData')
            proc_check = executeNamedProcedure(info.get('procedure_name'))
            if proc_check == False:
                return { 'error', 'error en la insercion de data' }, 400
            return { 'result': 'ok' }, 200
    except:
        return { 'error': 'error en el envio e insercion de data' }, 400
    

