HOST = "147.135.4.60"
PORT = "3306"
USER = "root"
PWD = "V1d4S0ftw4r3!"
DB = "strtg_autoservice"
MULTIPLESTATEMENTS = True

mysql_connection_string = ("DRIVER={MySQL ODBC 8.0 ANSI Driver};"+f"SERVER={HOST};DATABASE={DB};UID={USER}; PWD={PWD};")
mysql_procedures = {
    "checkUser": "CALL SP_UserCheck (?, ?);",
    "checkProcessID": "CALL SP_verifyProcessID (?);",
    "getProcessStructure": "CALL SP_getProcessStructure (?);",
    "getWholeStructure": "CALL SP_getJSONStructure (?);",
}