import json
import sys
import pyodbc

from api.config.mySQLconfig import mysql_procedures, mysql_connection_string

def checkUser(user, pwd):
    try:
        conn = pyodbc.connect(mysql_connection_string)
        cursor = conn.cursor()
        query = mysql_procedures.get(checkUser.__name__)
        print(f'Executing {checkUser.__name__} with {user} - {pwd} ')
        cursor.execute(query, (user, pwd))
        client = cursor.fetchone()
        clientID = client[0]
        print(type(clientID).__name__ == 'int')
        if type(clientID).__name__  != 'int':
            print('Cliente no es int')
            clientID = 0
        cursor.close()
        del cursor
        conn.commit()
        return clientID
    except Exception as err:
        if cursor: cursor.close()
        if conn: conn.close()
        print(f'Error {checkUser.__name__}', err, sys.exc_info())
        return 0

def checkProcessID(procID):
    try:
        conn = pyodbc.connect(mysql_connection_string)
        cursor = conn.cursor()
        query = mysql_procedures.get(checkProcessID.__name__)
        print(f'Executing {checkProcessID.__name__} with {procID}')
        cursor.execute(query, (procID))
        result = cursor.fetchall()
        if len(result) < 1:
            result = False
        else:
            result = True
        cursor.close()
        del cursor
        conn.close()
        return result
    except Exception as err:
        if cursor: cursor.close()
        if conn: conn.close()
        print(f'Error check {checkProcessID.__name__}', err, sys.exc_info())
        return False
    
def getProcessStructure(procID):
    try:
        conn = pyodbc.connect(mysql_connection_string)
        cursor = conn.cursor()
        query = mysql_procedures.get(getProcessStructure.__name__)
        print(f'Executing {getProcessStructure.__name__} with {procID}')
        cursor.execute(query, (procID))
        result = cursor.fetchval()
        cursor.close()
        del cursor
        conn.close()
        return result
    except Exception as err:
        if cursor: cursor.close()
        if conn: conn.close()
        print(f'Error check {getProcessStructure.__name__}', err, sys.exc_info())
        return False, _

def getTemplateStructure(procID):
    try:
        conn = pyodbc.connect(mysql_connection_string)
        cursor = conn.cursor()
        query = mysql_procedures.get(getTemplateStructure.__name__)
        print(f'Executing {getTemplateStructure.__name__} with {procID}')
        cursor.execute(query, (procID))
        result = cursor.fetchall()
        structure = json.dumps(result)
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        if cursor: cursor.close()
        if conn: conn.close()
        print(f'Error check {getTemplateStructure.__name__}', err, sys.exc_info())
        return False

def getWholeStructure(clientID):
    try: 
        conn = pyodbc.connect(mysql_connection_string)
        cursor = conn.cursor()
        query = mysql_procedures.get(getWholeStructure.__name__)
        print(f'Executing {getWholeStructure.__name__} with {clientID}')
        cursor.execute(query, (clientID))
        result = cursor.fetchval()
        structure = json.loads(result)
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        if conn:
            conn.close()
        print(f'Error check {getWholeStructure.__name__}', err, sys.exc_info())
        return False 