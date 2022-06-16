HOST = "147.135.4.60"
PORT = "3306"
USER = "root"
PWD = "V1d4S0ftw4r3!"
DB = "strtg_autoservice"
MULTIPLESTATEMENTS = True

mysql_procedures = {
    # DataCheck
    "checkUser": "CALL SP_UserCheck (%(user)s, %(pwd)s);",
    "checkProcessID": "CALL SP_verifyProcessID (%(procID)s);",
    "checkRoles": "CALL SP_getRoles (%(cliID)s);",
    # DataGet
    "getProcessStructure": "CALL SP_getProcessStructure (%(procID)s);",
    "getWholeStructure": "CALL SP_getJSONStructure (%(cliID)s);",
    "getGroups": "CALL SP_getGroups (%(cliID)s);",
    "getProcesses": "CALL SP_getProcesses (%(grpID)s);",
    "getValidations": "CALL SP_getValidation (%(processID)s);",
    # DataGetSingle
    "getProcessInfo": "CALL SP_getProcessInfo (%(procID)s);",
    "getGroupInfo": "CALL SP_getGroupInfo (%(grpID)s);",
    # UpsertItem
    "upsertGroup": "CALL SP_upsertGroup (%(grpID)s, %(grpName)s, %(cliID)s, %(isEnbld)s);",
    "upsertProcess": "CALL SP_upsertProcess (%(procID)s, %(procTypeID)s, %(grpID)s, %(procName)s, %(isEnbld)s);",
    "upsertValidation": "CALL SP_upsertValidation ( %(valID)s, %(procID)s, %(clName)s, %(clNumber)s, %(clType)s, %(opt)s, %(customVal)s, %(customValQuery)s, %(errMsg)s);",
    # DeleteItem
    "deleteGroup": "CALL SP_deleteGroup (%(grpID)s);",
    "deleteProcess": "CALL SP_deleteProcess (%(procID)s);",
    "deleteValidation": "CALL SP_deleteValidations (%(procID)s);"
}