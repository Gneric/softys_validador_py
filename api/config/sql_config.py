sql_config = {
    1: {
        "user": "db_admin",
        "password": "lKKjInmj7h3h5Yk@j0",
        "database": "STRATEGIO_CONTROL_SOFTYSI",
        "server": "51.222.152.125",
        "pool": {
          "max": 10,
          "min": 0,
          "idleTimeoutMillis": 30000
        },
        "options": {
          "encrypt": True, 
          "trustServerCertificate": True 
        }
    },
    2: {
        "user": "db_admin",
        "password": "lKKjInmj7h3h5Yk@j0",
        "database": "STRATEGIO_CONTROL_INTRADEVCO",
        "server": "51.222.152.125",
        "pool": {
          "max": 10,
          "min": 0,
          "idleTimeoutMillis": 30000
        },
        "options": {
          "encrypt": True, 
          "trustServerCertificate": True 
        }
    },
}

def getCredentials(id):
  return sql_config.get(id)

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={sql_config.get('server')};"
    f"DATABASE={sql_config.get('database')};"
    f"UID={sql_config.get('user')};PWD={sql_config.get('password')};"
)