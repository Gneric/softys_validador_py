from utils.createApp import createApp
from api.routes.routes import Routes
from waitress import serve

# Creacion de la app / api
app, api = createApp(__name__)
# Instanciamiento de Rutas
rts = Routes()

# getToken
api.add_resource(rts._token, '/api/getToken')

# Roles
api.add_resource(rts._getRoles, '/api/protected/roles/getRoles')

# Structure
api.add_resource(rts._getGroups, '/api/protected/structure/getGroups')
api.add_resource(rts._getProcesses, '/api/protected/structure/getProcesses')
api.add_resource(rts._getValidations, '/api/protected/structure/getValidations')

api.add_resource(rts._getSingleProcess, '/api/protected/structure/getSingleProcess')
api.add_resource(rts._getSingleGroup, '/api/protected/structure/getSingleGroup')

api.add_resource(rts._upsertGroup, '/api/protected/structure/upsertGroup')
api.add_resource(rts._upsertProcess, '/api/protected/structure/upsertProcess')
api.add_resource(rts._upsertValidations, '/api/protected/structure/upsertValidations')

api.add_resource(rts._insertNewProcess, '/api/protected/structure/insertNewProcess')

api.add_resource(rts._removeGroup, '/api/protected/structure/removeGroup')
api.add_resource(rts._removeProcess, '/api/protected/structure/removeProcess')

# Templates
api.add_resource(rts._getTemplate, '/api/protected/templates/getTemplate')
api.add_resource(rts._getErrorTemplate, '/api/protected/templates/getErrorTemplate')

# Data
api.add_resource(rts._validateData, '/api/protected/dataVal/validateData')
api.add_resource(rts._insertData, '/api/protected/dataVal/insertData')

# Alerts
# # api.add_resource(rts._alerts, '/api/protected/alerts/getAlerts') # ?
#api.add_resource(rts._mailAlerts, '/api/protected/alerts/mailAlerts') # Mandar los 3 casos de alertas

# Maestros
# api.add_resource(rts._listDD,'/api/protected/masters/listDD') # Retorna listado de datos distribuidoras segun conexion
# api.add_resource(rts._crudDD,'/api/protected/masters/crudDD') # Recibe Array de objetos tipo distribuidora + una key: 'delete', 'add', 'update' la cual dictara que hara el procedure / retorn ok o listado de errores

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=3008, threads=8) # Solo para produccion
    app.run(host='0.0.0.0', port=3100, debug=True)