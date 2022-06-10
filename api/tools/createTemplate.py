import json
import os
import xlsxwriter


def createTemplate(structure):
    try:
        data = json.loads(structure[0][0])
        validata = data.get('validationData')
        processName = data.get("processName")
        processID = validata[0].get('processID')
        filename = f'{processID}_{processName}.xlsx'
        filepath = f'files/{filename}'

        # Delete if exists
        if os.path.exists(filepath):
            print(f'Deleting {filename}')
            os.remove(filepath)

        workbook = xlsxwriter.Workbook(filepath, {'in_memory': True})
        data_ws = workbook.add_worksheet('data')
        # Formato string
        text_format = workbook.add_format()
        text_format.set_num_format('@')
        # Formato int
        int_format = workbook.add_format()
        int_format.set_num_format('#')
        # Formato float
        float_format = workbook.add_format()
        float_format.set_num_format('#,##0.00')
        # Formato date
        date_format = workbook.add_format()
        date_format.set_num_format('d/mm/yyyy')

        format_selector = {
            'string': text_format,
            'int': int_format,
            'float': float_format,
            'date': date_format
        }
        
        for row in validata:
            data_ws.write(0, validata.index(row), row.get('columnName'))
            data_ws.set_column( 
                first_col=validata.index(row), 
                last_col=validata.index(row), 
                width=20, 
                cell_format=format_selector.get(row.get('columnType'))
            )

        
        workbook.close()
        return filename
    except Exception as err:
        print('Error in createTemplate :', err)
        return ''