sql_config = {
    1: {
        "user": "sa",
        "password": "2bhDcn2y",
        "database": "STRATEGIO_CONTROL_SOFTYSI",
        "server": "147.135.4.52",
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