import api.routes.alerts.getAlerts as route_alertas
import api.routes.getToken.getToken as route_token
import api.routes.insertData.insertData as route_insertData
import api.routes.validateData.validateData as route_validateData
import api.routes.templates.getTemplate as route_template
import api.routes.structure.getStructure as route_getStructure
import api.routes.roles.getRoles as route_getRoles

# Importar todas rutas en una clase para que no se llene de imports main.py
class Routes():
    def __init__(self):
        self._token = route_token.getToken
        self._alerts = route_alertas.getAlerts
        
        self._insertData = route_insertData.insertData
        self._validateData = route_validateData.validateData

        self._getTemplate = route_template.downloadTemplate
        self._getGroups = route_getStructure.getListGroups
        self._getProcesses = route_getStructure.getListProcesses
        self._getValidations = route_getStructure.getListValidations

        self._getSingleProcess = route_getStructure.getSingleProcess
        self._getSingleGroup = route_getStructure.getSingleGroup

        # self._createGroup
        # self._createProcess

        # self._updateGroupInfo
        # self._updateProcessInfo
        # self._updateValidationInfo

        # self._disableGroup
        # self._disableProcess
        
        self._getRoles = route_getRoles.getRoles
