from concurrent.futures.thread import _worker
import json
import pandas as pd
import xlsxwriter



def createTemplate(structure):
    try:
        print('----------------')
        data = json.loads(structure[0][0])
        validata = data.get('validationData')
        processName = data.get("processName")
        filename = f'{processName}.xlsx'
        workbook = xlsxwriter.Workbook(f'files/{filename}')
        data_ws = workbook.add_worksheet('data')
        # Formato texto
        text_format = workbook.add_format()
        text_format.set_num_format('@')
        # Formato entero
        int_format = workbook.add_format()
        int_format.set_num_format('#')
        # Formato numeric
        num_format = workbook.add_format()
        num_format.set_num_format('#,##0.00')
        # Formato fecha
        date_format = workbook.add_format()
        date_format.set_num_format('d/mm/yyyy')

        format_selector = {
            'string': text_format,
            'int': int_format,
            'numeric': num_format,
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
        print('----------------')
        return filename
    except Exception as err:
        print('Error in createTemplate :', err)
        return ''