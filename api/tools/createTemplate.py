import pandas as pd

def createTemplate(structure):
    try:
        print(structure)
        json_df = pd.read_json(structure)
        df = json_df[['columnNumber','columnName','columnType','optional','customValidation','customValidationQuery','errorMessage']]
        df_list = df.to_list()
        print(df_list)
    except Exception as err:
        print('Error in createTemplate :', err)