import json
import pandas as pd

from api.tools.validaciones import validateDF

excluded_string_columns = ['Fecha','Cantidad','Precio Unitario','Precio Total sin IGV']
float_columns = ['Precio Unitario','Precio Total sin']
def validateFile(excelFile):
    errors_found = []
    df = pd.read_excel(excelFile, sheet_name='data')
    
    # Transformando data a tipos necesarios
    for c in df.columns:
        if c not in excluded_string_columns: 
            df[c] = df[c].astype(str)
        elif 'precio' in c.lower(): 
            df[c] = df[c].astype(float)

    df_test = df.head(10)
    errors_found = validateDF(df_test)
    if errors_found == []:
        data = json.loads(df_test.to_json(orient="records"))
        total = df['Precio Total sin IGV'].sum()
        return { 'result': 'ok', 'totales': total, 'data': data }, 200
    else:
        return { 'result': 'error', 'errors': errors_found }, 400
        
    