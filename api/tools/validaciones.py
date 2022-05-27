import pandas as pd
import json
import sys

from api.constants.data_types import data_examples

empty_values_list = ["",None,"nan"]
def validateEmpty(value, column_name):
    if value in empty_values_list:
       return {
            'column': column_name,
            'error_type': 'Valor vacio',
            'error_message': f'El valor enviado se encuentra vacio'
        } 

# Validar type
def validateType(value, example, column_name):
    if value != example:
        return {
            'column': column_name,
            'error_type': 'Error en tipo de dato',
            'error_message': f'El tipo de dato es erroneo, se espero {example.__name__} pero se envio {value.__name__}'
        }

def validateTotal(price, qty, total, column_name):
    if price * qty != total:
        return {
            'column': column_name,
            'error_type': 'Error en totalizado',
            'error_message': 'El totalizado sin IGV no concuerda con la cantidad * precio Unitario'
        }
    else:
        return False

def validateDevolution(doc, total, column_name):
    if 'NC' in doc and total > 0:
        return {
            'column': column_name, 
            'error_type': 'Nota de credito con totalizado erroneo', 
            'error_message': 'Las notas de credito solo puede contener totalizados negativos'
        }
    else:
        return False

# Validar row
def validateDF(df: pd.DataFrame):
    errors = []
    sjson_df = df.to_json(orient="records")
    json_df = json.loads(sjson_df)
    index = 0
    for row in json_df:
        try:
            row_num = index + 1
            row_errors = []

            # Revision de data por item
            for column_name, value in row.items():
                optional = data_examples.get(column_name).get('optional')
                example = data_examples.get(column_name).get('example')

                if optional == False or (optional == True and value != ""):
                    checkEmpty = validateEmpty(value, column_name)
                    if checkEmpty != False: 
                        row_errors.append(checkEmpty)
                    checkType = validateType(type(value), type(example), column_name)
                    if checkType != False: 
                        row_errors.append(checkType)

            # Revision de data por fila
            check_dev = validateDevolution(row.get('Nro Factura'), row.get('Precio Total sin IGV'), 'Precio Total sin IGV')
            # print(f'validateDevolution : {check_dev}')
            if check_dev != False: 
                row_errors.append(check_dev)

            check_total = validateTotal(row.get('Precio Unitario'), row.get('Cantidad'), row.get('Precio Total sin IGV'), 'Precio Total sni IGV')
            # print(f'validateTotal : {check_total}')
            if check_total != False: 
                row_errors.append(check_total)

            row_errors = [i for i in row_errors if i]
            if len(row_errors) > 0:
                errors.append({ 'row': row_num, 'row_details': row, 'error_details': row_errors })
        except:
            print(sys.exc_info())
        finally:
            index = index + 1
    return errors