import json, sys,  mysql.connector
import os
from api.config.mySQLconfig import HOST, DB, USER, PWD, mysql_procedures

def upsertGroup(data, clientID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD, autocommit=True)
        query = mysql_procedures.get(upsertGroup.__name__)
        groupID = data.get('groupID', 999999999)
        groupName = data.get('groupName')
        isEnabled = data.get('isEnabled')
        print(f'Executing {upsertGroup.__name__} with {data} and {clientID}')
        cursor = conn.cursor()
        cursor.execute(query, { 'grpID': groupID, 'grpName': groupName, 'cliID': clientID, 'isEnbld':  isEnabled })
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return True
    except Exception as err:
        print(f'Error check {upsertGroup.__name__}', err, sys.exc_info())
        return False

def upsertProcess(data):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD, autocommit=True)
        query = mysql_procedures.get(upsertProcess.__name__)        
        print(f'Executing {upsertProcess.__name__} with {data}')
        cursor = conn.cursor()
        cursor.execute(query, { 
            'procID': data.get('processID', 999999999), 
            'procTypeID': data.get('processTypeID', ''), 
            'grpID': data.get('groupID', ''),
            'procName': data.get('processName', ''),
            'target': data.get('targetTable', ''),
            'isEnbld': data.get('isEnabled', )
        })
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return True
    except Exception as err:
        print(f'Error check {upsertProcess.__name__}', err, sys.exc_info())
        return False
    
def upsertValidation(data, processID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        query = mysql_procedures.get(upsertValidation.__name__)
        print(f'Executing {upsertValidation.__name__} for  {processID}')
        val = [{
                'valID': row.get('validationStructureID', 999999999),
                'procID': processID, 
                'clName': row.get('columnName'), 
                'clNumber': row.get('columnNumber'),
                'clType': row.get('columnType'),
                'opt': row.get('optional'),
                'val': row.get('checkValue'),
                'customVal': row.get('customValidation'),
                'customValQuery': row.get('customValidationQuery'),
                'errMsg': row.get('errorMessage')
            } for row in data ]
        cursor = conn.cursor()
        cursor.executemany(query, val)
        cursor.close()
        conn.commit()
        return True
    except Exception as err:
        print(f'Error check {upsertValidation.__name__}', err, sys.exc_info())
        return False
        

def insertNewProcess(data):
    try:
        print(f'Executing {insertNewProcess.__name__} with {data}')
        validation_structure = data.get('validationStructure', '')
        if validation_structure == "":
            return False           
            
        result = upsertProcess({
            'processTypeID': data.get('processTypeID'),
            'grpID': data.get('groupID', ''), 
            'processName': data.get('processName'),
            'target': data.get('targetTable'),
            'isEnabled': data.get('isEnabled')
        })
        if result != True:
            return False 
        
        result_val = upsertValidation(validation_structure)
        if result != True:
            return False
        
        return True
    except Exception as err:
        print(f'Error check {insertNewProcess.__name__}', err, sys.exc_info())
        return False


