import pandas as pd

def createTemplate(structure):
    try:
        json_df = pd.read_json(structure)
        df = json_df[['columnNumber','columnName','columnType','optional','customValidation','customValidationQuery','errorMessage']]
        
        print(df)
    except Exception as err:
        print('Error in createTemplate :', err)