import api.routes.alerts.getAlerts as route_alertas
import api.routes.getToken.getToken as route_token
import api.routes.insertData.insertData as route_insertData
import api.routes.validateData.validateData as route_validateData
import api.routes.templates.getTemplate as route_template
import api.routes.structure.getStructure as route_getStructure

# Importar todas rutas en una clase para que no se llene de imports main.py
class Routes():
    def __init__(self):
        self._token = route_token.getToken
        self._alerts = route_alertas.getAlerts
        self._insertData = route_insertData.insertData
        self._validateData = route_validateData.validateData
        self._getTemplate = route_template.downloadTemplate
        self._getStructure = route_getStructure.getStructure

