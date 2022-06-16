import datetime
import json
import pandas as pd
from api.services.sqlConnection.sqlConn import insertTemporalData

from api.tools.validaciones import validateDF

def validateFile(excelFile, structure, credentials, processID):
    structure_data = json.loads(structure[0][0])
    structure_cols = [ x.get('columnName') for x in structure_data.get('validationData') ]
    df_structure = {}
    for x in structure_data.get('validationData'):
        df_structure.update({ x.get('columnName') : object })

    df = pd.read_excel(excelFile, sheet_name='data', dtype=df_structure)
    df_test = df.head(10)
    df_length = len(df_test)

    # De Pandas a JSON
    sjson_df = df_test.to_json(orient="records")
    json_df = json.loads(sjson_df)
    
    # Validacion de que la estructura sea la correcta
    file_cols = list(df_test.columns)
    
    if file_cols != structure_cols:
        return { 'error': 'El archivo excel no coincide con la estructura' }, 400

    errors_found = validateDF(json_df, structure_data.get('validationData'))
    if errors_found != []:
        return { 'result': 'error', 'errors': errors_found }, 400
    else:        
        result = insertTemporalData(df_test, credentials, processID)
        if result == 0:
            return { 'error': 'error en la carga de data temporal' }, 400
        return { 'result': 'ok', 'totales': df_length, 'processID': processID }, 200