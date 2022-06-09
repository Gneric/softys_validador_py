import json
import pandas as pd

from api.tools.validaciones import validateDF


def validateFile(excelFile, structure):
    df = pd.read_excel(excelFile, sheet_name='data')
    df_test = df.head(10)
    errors_found = validateDF(df_test, structure)
    if errors_found == []:
        data = json.loads(df_test.to_json(orient="records"))
        total = df['Precio Total sin IGV'].sum()
        return { 'result': 'ok', 'totales': total, 'data': data }, 200
    else:
        return { 'result': 'error', 'errors': errors_found }, 400
        
    