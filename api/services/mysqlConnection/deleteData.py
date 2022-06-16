import sys,  mysql.connector
from api.config.mySQLconfig import HOST, DB, USER, PWD, mysql_procedures

def deleteGroup(groupID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD, autocommit=True)
        query = mysql_procedures.get(deleteGroup.__name__)
        print(f'Executing {deleteGroup.__name__} with {groupID}')
        cursor = conn.cursor()
        cursor.execute(query, { 'grpID': groupID })
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return True
    except Exception as err:
        print(f'Error check {deleteGroup.__name__}', err, sys.exc_info())
        return False

def deleteProcess(procID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD, autocommit=True)
        query = mysql_procedures.get(deleteProcess.__name__)
        print(f'Executing {deleteProcess.__name__} with {procID}')
        cursor = conn.cursor()
        cursor.execute(query, { 'procID': procID })
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return True
    except Exception as err:
        print(f'Error check {deleteProcess.__name__}', err, sys.exc_info())
        return False

def deleteValidation(procID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD, autocommit=True)
        query = mysql_procedures.get(deleteValidation.__name__)
        print(f'Executing {deleteValidation.__name__} with {procID}')
        cursor = conn.cursor()
        cursor.execute(query, { 'procID': procID })
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return True
    except Exception as err:
        print(f'Error check {deleteValidation.__name__}', err, sys.exc_info())
        return False
