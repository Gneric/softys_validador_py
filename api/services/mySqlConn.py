import json
import sys
import mysql.connector

from api.config.mySQLconfig import HOST, DB, USER, PWD, mysql_procedures

def checkUser(user, pwd):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(checkUser.__name__)
        print(f'Executing {checkUser.__name__} with {user} - {pwd} ')
        cursor.execute(query, { 'user': user , 'pwd': pwd })
        client = cursor.fetchone()
        clientID = client[0]
        print(type(clientID).__name__ == 'int')
        if type(clientID).__name__  != 'int':
            print('Cliente no es int')
            clientID = 0
        cursor.close()
        del cursor
        conn.close()
        return clientID
    except mysql.connector.Error as error:
        print("Failed in MySQL: {}".format(error))
    except Exception as err:
        print(f'Error {checkUser.__name__}', err, sys.exc_info())
        return 0

def checkProcessID(procID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(checkProcessID.__name__)
        print(f'Executing {checkProcessID.__name__} with {procID}')
        cursor.execute(query, { 'procID': procID })
        result = cursor.fetchall()
        if len(result) < 1:
            result = False
        else:
            result = True
        cursor.close()
        del cursor
        conn.close()
        return result
    except mysql.connector.Error as error:
        print("Failed in MySQL: {}".format(error))
    except Exception as err:
        print(f'Error check {checkProcessID.__name__}', err, sys.exc_info())
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
    
def getProcessStructure(procID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getProcessStructure.__name__)
        print(f'Executing {getProcessStructure.__name__} with {procID}')
        cursor.execute(query, { 'procID': procID })
        result = cursor.fetchall()
        cursor.close()
        del cursor
        conn.close()
        return result[0][0]
    except Exception as err:
        print(f'Error check {getProcessStructure.__name__}', err, sys.exc_info())
        return False

def getTemplateStructure(procID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getTemplateStructure.__name__)
        print(f'Executing {getTemplateStructure.__name__} with {procID}')
        cursor.execute(query, { 'procID': procID })
        result = cursor.fetchall()
        structure = json.dumps(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getTemplateStructure.__name__}', err, sys.exc_info())
        return False

def getWholeStructure(cliID):
    try: 
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getWholeStructure.__name__)
        print(f'Executing {getWholeStructure.__name__} with {cliID}')
        cursor.execute(query, { 'cliID': cliID })
        result = cursor.fetchall()
        structure = json.loads(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getWholeStructure.__name__}', err, sys.exc_info())
        return False 