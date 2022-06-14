import json, sys,  mysql.connector
from api.config.mySQLconfig import HOST, DB, USER, PWD, mysql_procedures
    
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

def getGroups(cliID):
    try: 
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getGroups.__name__)
        print(f'Executing {getGroups.__name__} with {cliID}')
        cursor.execute(query, { 'cliID': cliID })
        result = cursor.fetchall()
        structure = json.loads(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getGroups.__name__}', err, sys.exc_info())
        return False 

def getProcesses(grpID):
    try: 
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getProcesses.__name__)
        print(f'Executing {getProcesses.__name__} with {grpID}')
        cursor.execute(query, { 'grpID': grpID })
        result = cursor.fetchall()
        structure = json.loads(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getProcesses.__name__}', err, sys.exc_info())
        return False 

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
        return result
    except Exception as err:
        print(f'Error check {getProcessStructure.__name__}', err, sys.exc_info())
        return False

def getValidations(processID):
    try: 
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getValidations.__name__)
        print(f'Executing {getValidations.__name__} with {processID}')
        cursor.execute(query, { 'processID': processID })
        result = cursor.fetchall()
        structure = json.loads(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getValidations.__name__}', err, sys.exc_info())
        return False 

def getProcessInfo(processID):
    try: 
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getProcessInfo.__name__)
        print(f'Executing {getProcessInfo.__name__} with {processID}')
        cursor.execute(query, { 'procID': processID })
        result = cursor.fetchall()
        structure = json.loads(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getProcessInfo.__name__}', err, sys.exc_info())
        return False 

def getGroupInfo(groupID):
    try: 
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        cursor = conn.cursor()
        query = mysql_procedures.get(getGroupInfo.__name__)
        print(f'Executing {getGroupInfo.__name__} with {groupID}')
        cursor.execute(query, { 'groupID': grpID })
        result = cursor.fetchall()
        structure = json.loads(result[0][0])
        cursor.close()
        del cursor
        conn.close()
        return structure
    except Exception as err:
        print(f'Error check {getGroupInfo.__name__}', err, sys.exc_info())
        return False 