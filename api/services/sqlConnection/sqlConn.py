import string, sys, urllib, pyodbc
import sqlalchemy as sa
import pandas as pd

from api.config.sql_config import connection_string
from api.constants.sql_tables_info import tables_info, carga_info

def insertTemporalData(df: pd.DataFrame, credentials, processID, dataTypes):
    try:
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={credentials.get('server')};"
            f"DATABASE={credentials.get('database')};"
            f"UID={credentials.get('user')};PWD={credentials.get('password')};"
        )
        connection_uri = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = sa.create_engine(connection_uri, fast_executemany=True)
        table_name = f'autoservice_{processID}_temp'
        df.to_sql(table_name, engine, if_exists='replace', index=False, schema='serv')
        return processID
    except:
        print("Unexpected error en func 'insertTemporalData': ", sys.exc_info())
        return 0

def selectTempIntoTable(credentials, processID, targetTable):
    try:
        control = credentials.get('database')
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={credentials.get('server')};"
            f"DATABASE={control};"
            f"UID={credentials.get('user')};PWD={credentials.get('password')};"
        )
        conn = pyodbc.connect(connection_string)
        with conn:
            cursor = conn.cursor()
            #query = f"INSERT INTO {control}.dbo.autoservice_{processID}_test SELECT * FROM {control}.serv.autoservice_{processID}_temp"
            cursor.execute("EXEC InsertAutoserviceData @targetTable=?, @fromTable=?", ( targetTable, f'autoservice_{processID}_temp' ))
            conn.commit()
        return 1
    except:
        print("Unexpected error en func 'selectTempIntoTable': ", sys.exc_info())
        return 0

def deleteTemporalTable(credentials, processID):
    try:
        control = credentials.get('database')
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={credentials.get('server')};"
            f"DATABASE={control};"
            f"UID={credentials.get('user')};PWD={credentials.get('password')};"
        )
        conn = pyodbc.connect(connection_string)
        with conn:
            cursor = conn.cursor()
            query = f"DROP TABLE {control}.serv.autoservice_{processID}_temp"
            cursor.execute(query)
            conn.commit()
        return 1
    except:
        print("Unexpected error en func 'deleteTemporalTable': ", sys.exc_info())
        return 0

# Execute procedure
def insertToTable(df : pd.DataFrame ):
    try:
        connection_uri = f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}"
        engine = sa.create_engine(connection_uri, fast_executemany=True)
        data_table_info = carga_info.get('insertData')
        table_name = data_table_info.get('table_name')
        db_cols = data_table_info.get('column_names')
        (df.rename(columns=dict(zip(df.columns, db_cols))).to_sql(table_name,engine,if_exists='append',index=False))
        return True
    except:
        print("Unexpected error en func 'insertToTable': ", sys.exc_info())
        return False

def executeProcedure(proc_name):
    try:
        conn = pyodbc.connect(connection_string)
        data = []
        with conn:
            cursor = conn.cursor()
            query = "EXEC " + proc_name
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.commit() 
            df = pd.DataFrame(data)
            df.columns = [column[0] for column in cursor.description]
            json_df = df.to_json(orient="records")
            return True
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        return sqlstate
    except:
        print("Unexpected error en func 'executeProcedure': ", sys.exc_info())
        return False

def executeNamedProcedure(credentials, procedure : string):
    try:
        conn_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={credentials.get('server')};"
            f"DATABASE={credentials.get('database')};"
            f"UID={credentials.get('user')};PWD={credentials.get('password')};"
        )
        conn = pyodbc.connect(conn_string)
        with conn:
            cursor = conn.cursor()
            query = "EXEC " + procedure
            cursor.execute(query)
            conn.commit() 
            return True, ''
    except pyodbc.Error as ex:
        sqlstate = ex.args[1]
        return False, sqlstate
    except:
        print("Unexpected error en func 'executeNamedProcedure': ", sys.exc_info())
        return False, ''


    
