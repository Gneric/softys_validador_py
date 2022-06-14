import string, sys, urllib, pyodbc
import sqlalchemy as sa
import pandas as pd

from api.config.sql_config import connection_string

from api.constants.sql_tables_info import tables_info, carga_info


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

def executeProcedure(target_table : string ):
    try:
        conn = pyodbc.connect(connection_string)
        tb_info = tables_info.get(target_table)
        proc_name = tb_info.get('procedure')
        data = []
        with conn:
            cursor = conn.cursor()
            query = "EXEC " + proc_name
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                data.append(list(row))
            conn.commit() 
            df = pd.DataFrame(data)
            df.columns = [column[0] for column in cursor.description]
            json_df = df.to_json(orient="records")
            return json_df
    except:
        print("Unexpected error en func 'executeProcedure': ", sys.exc_info())
        return False

def executeNamedProcedure(procedure : string):
    try:
        conn = pyodbc.connect(connection_string)
        with conn:
            cursor = conn.cursor()
            query = "EXEC " + procedure
            cursor.execute(query)
            conn.commit() 
            return True
    except:
        print("Unexpected error en func 'executeProcedure': ", sys.exc_info())
        return False


    
