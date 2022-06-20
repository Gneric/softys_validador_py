import api.routes.alerts.getAlerts as route_alertas
import api.routes.getToken.getToken as route_token
import api.routes.data.insertData as route_upsertData
import api.routes.validateData.validateData as route_validateData
import api.routes.templates.getTemplate as route_template
import api.routes.structure.getStructure as route_getStructure
import api.routes.structure.upsertStructure as route_upsertStructure
import api.routes.structure.deleteStructure as route_deleteStructure
import api.routes.roles.getRoles as route_getRoles

# Importar todas rutas en una clase para que no se llene de imports main.py
class Routes():
    def __init__(self):
        self._token = route_token.getToken
        self._alerts = route_alertas.getAlerts
        
        self._insertData = route_upsertData.insertData
        self._validateData = route_validateData.validateData

        self._getTemplate = route_template.downloadTemplate
        self._getErrorTemplate = route_template.GenerateErrorTemplate
        self._getGroups = route_getStructure.getListGroups
        self._getProcesses = route_getStructure.getListProcesses
        self._getValidations = route_getStructure.getListValidations

        self._getSingleProcess = route_getStructure.getSingleProcess
        self._getSingleGroup = route_getStructure.getSingleGroup

        self._upsertGroup = route_upsertStructure.upsertGroups
        self._upsertProcess = route_upsertStructure.upsertProcesses
        self._upsertValidations = route_upsertStructure.upsertValidations

        self._insertNewProcess = route_upsertStructure.newProcess

        self._removeGroup = route_deleteStructure.removeGroup
        self._removeProcess = route_deleteStructure.removeProcess
        self._removeValidations = route_deleteStructure.removeValidations
        
        self._getRoles = route_getRoles.getRoles
