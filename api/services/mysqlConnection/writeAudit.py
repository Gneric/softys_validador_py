import json, sys,  mysql.connector
from api.config.mySQLconfig import HOST, DB, USER, PWD, mysql_procedures

def writeLog(username, endpoint, success, error_on, error_msg, actionTime):
    try:
        conn = mysql.connector.connect(host=HOST,database=DB,user=USER,password=PWD, autocommit=True)
        query = mysql_procedures.get(writeLog.__name__)
        cursor = conn.cursor()
        cursor.execute(query, { 
            'usr': username, 
            'url': endpoint, 
            'sucessb': success, 
            'errorfunction':  error_on,
            'msg':  error_msg,
            'dtime':  actionTime 
        })
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        return True
    except Exception as err:
        print(f'Error logging {writeLog.__name__}', err, sys.exc_info())
        return False