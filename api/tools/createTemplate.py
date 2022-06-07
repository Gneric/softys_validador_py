import json
import pandas as pd
import xlsxwriter

def createTemplate(structure):
    try:
        print('----------------')
        data = json.loads(structure[0][0])
        validata = data.get('validationData')
        processName = data.get("processName")
        workbook = xlsxwriter.Workbook(f'files/{processName}.xlsx')
        data_ws = workbook.add_worksheet('data')
        print('createTemplate structure : ', )
        for row in validata:
            data_ws.write(1, validata.index(row)+1, row.get('columnName'))
        workbook.close()
        print('----------------')
        return True
    except Exception as err:
        print('Error in createTemplate :', err)
        return False