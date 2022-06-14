import json, sys,  mysql.connector
from api.config.mySQLconfig import HOST, DB, USER, PWD, mysql_procedures
    
def upsertGroupInfo(jsonData):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        query = mysql_procedures.get(upsertGroupInfo.__name__)
        print(f'Executing {upsertGroupInfo.__name__} with {len(jsonData)} rows')
        for row in jsonData:
            cursor = conn.cursor() 
            cursor.execute(query, { 'rowData': row })
            result = cursor.fetchall()
            structure = json.dumps(result[0][0])
            cursor.close()
            del cursor
            conn.close()
        return structure
    except Exception as err:
        print(f'Error check {upsertGroupInfo.__name__}', err, sys.exc_info())
        return False

def createNewGroup(data, clientID):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD)
        query = mysql_procedures.get(createNewGroup.__name__)
        for row in data:
            cursor = conn.cursor()
            cursor.execute(query, { 'grpName': row.get('groupName'), 'cliID': clientID, 'isEnabled': 1 })
            result = cursor.fetchall()
            cursor.close()
            del cursor
            conn.close()
        return True
    except Exception as err:
        print(f'Error check {createNewGroup.__name__}', err, sys.exc_info())
        return False

    

