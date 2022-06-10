import datetime
import json
import pandas as pd

from api.tools.validaciones import validateDF

def validateFile(excelFile, structure):
    structure_data = json.loads(structure[0][0])
    df = pd.read_excel(excelFile, sheet_name='data')
    df_test = df.head(10)

    # De Pandas a JSON
    sjson_df = df_test.to_json(orient="records", date_format='iso')
    json_df = json.loads(sjson_df)
    
    # Validacion de que la estructura sea la correcta
    file_cols = list(df_test.columns)
    structure_cols = [ x.get('columnName') for x in structure_data.get('validationData') ]
    if file_cols != structure_cols:
        return { 'error': 'El archivo excel no coincide con la estructura' }, 400

    errors_found = validateDF(json_df, structure_data.get('validationData'))
    if errors_found == []:
        total = len(df_test)
        return { 'result': 'ok', 'totales': total, 'data': json_df }, 200
    else:
        return { 'result': 'error', 'errors': errors_found }, 400