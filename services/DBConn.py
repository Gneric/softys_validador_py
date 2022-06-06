from array import array as arr
from operator import indexOf
import pyodbc

from api.config.sql_config import mysql_connection_string


def selectwParams(table, args : dict = {} ):
    if table == "": 
        return
    query = f'SELECT * FROM {table}'
    where = ' WHERE '
    rownum = 0
    for key, value in args.items():
        rownum += 1
        if rownum < len(args): 
            where = where + f' {key} {value} AND'
        else:
            where = where + f' {key} {value}'   

    cnxn = pyodbc.connect(mysql_connection_string)
    cursor = cnxn.cursor()
    cursor.execute(query + where)
    rows = cursor.fetchall()
    return rows
