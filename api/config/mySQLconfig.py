HOST = "51.222.82.147"
PORT = "3306"
USER = "root"
PWD = "V1d4S0ftw4r3!"
DB = "strtg_autoservice"
MULTIPLESTATEMENTS = True

mysql_procedures = {
    # DataCheck
    "checkUser": "CALL SP_UserCheck (%(user)s, %(pwd)s);",
    "checkProcessID": "CALL SP_verifyProcessID (%(procID)s);",
    "checkRoles": "CALL SP_checkRoles (%(roleNameInput)s);",
    "writeLog": "CALL SP_writeLog(%(username)s, %(endpoint)s, %(success)s, %(error_on)s, %(error_msg)s, %(actionTime)s);",
    # DataGet
    "getProcessStructure": "CALL SP_getProcessStructure (%(procID)s);",
    "getGroups": "CALL SP_getGroups (%(cliID)s);",
    "getProcesses": "CALL SP_getProcesses (%(grpID)s);",
    "getValidations": "CALL SP_getValidation (%(processID)s);",
    "getCheckValues": "CALL SP_getCheckValues (%(procID)s);",
    "getCheckCustomProcedure": "CALL SP_getCheckCustomProcedure (%(procID)s)",
    "getTargetTable": "CALL SP_getTargetTable (%(procID)s)",
    # DataGetSingle
    "getProcessInfo": "CALL SP_getProcessInfo (%(procID)s);",
    "getGroupInfo": "CALL SP_getGroupInfo (%(grpID)s);",
    # UpsertItem
    "upsertGroup": "CALL SP_upsertGroup (%(grpID)s, %(grpName)s, %(cliID)s, %(isEnbld)s);",
    "upsertProcess": "CALL SP_upsertProcess (%(procID)s, %(procTypeID)s, %(grpID)s, %(procName)s, %(isEnbld)s);",
    "upsertValidation": "CALL SP_upsertValidation ( %(valID)s, %(procID)s, %(clName)s, %(clNumber)s, %(clType)s, %(opt)s, %(val)s, %(customVal)s, %(customValQuery)s, %(errMsg)s);",
    # DeleteItem
    "deleteGroup": "CALL SP_deleteGroup (%(grpID)s);",
    "deleteProcess": "CALL SP_deleteProcess (%(procID)s);",
    "deleteValidation": "CALL SP_deleteValidations (%(procID)s);"
}