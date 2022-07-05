import sys

empty_values_list = ["",None,"nan"]
def validateEmpty(value, column_name):
    if value in empty_values_list:
       return {
            'column': column_name,
            'error_type': 'Valor vacio',
            'error_message': f'El valor enviado se encuentra vacio'
        } 

# Validar type
def validateType(value, valueType, column_name):
    if valueType in ('string'):
        valueType = 'str'
    if valueType in ('date'):
        valueType = 'int'
    if value.__name__ != valueType:
        try:
            if valueType == 'float':
                float(value)
            if valueType == 'int':
                int(value)
            if valueType == 'string':
                str(value)
        except:
            return {
                'column': column_name,
                'error_type': 'Error en tipo de dato',
                'error_message': f'El tipo de dato es erroneo, se espero {valueType} pero se envio {value.__name__}'
            }

# Validar row
def validateDF(json_df, structure):
    errors = []
    index = 0
    for row in json_df:
        try:
            row_num = index + 1
            row_errors = []
            # Revision de data por item
            for column_name, value in row.items():
                filtered_structure = list(filter(lambda obj: obj.get('columnName') == column_name, structure))[0]
                optional = filtered_structure.get('optional')
                valueType = filtered_structure.get('columnType')

                if optional == 0 or (optional == 1 and value not in ("", 0, None)):                                                       
                    # Validaciones comunes
                    checkEmpty = validateEmpty(value, column_name)
                    if checkEmpty != False: 
                        row_errors.append(checkEmpty)
                    else:
                        checkType = validateType(type(value), valueType, column_name)
                        if checkType != False:
                            row_errors.append(checkType)

            # Custom Validations
            custom_val_structure = list(filter(lambda obj: obj.get('customValidation') == 1, structure))
            for cvs_row in custom_val_structure:
                csv_row_name = cvs_row.get('columnName')
                raw_query = cvs_row.get('customValidationQuery')
                error_message = cvs_row.get('errorMessage')
                query = 'True if ' + raw_query.replace("{","row.get('").replace("}","')") + ' else False '
                try:
                    result_query = eval(query)
                    if result_query == False:
                        row_errors.append({
                            'column': csv_row_name,
                            'error_type': 'customValidation Error',
                            'error_message': f'{error_message}'
                        })
                except:
                    row_errors.append({
                        'column': 'customValidation',
                        'error_type': 'Error en la query',
                        'error_message': 'La query ingresada por el fidelizador es erronea'
                    })

            row_errors = [i for i in row_errors if i]
            if len(row_errors) > 0:
                errors.append({ 'row': row_num, 'row_details': row, 'error_details': row_errors })
        except:
            print(sys.exc_info())
        finally:
            index = index + 1
    return errors