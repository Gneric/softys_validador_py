from utils.createApp import createApp
from api.routes.routes import Routes
from waitress import serve

# Creacion de la app / api
app, api = createApp(__name__)
# Instanciamiento de Rutas
rts = Routes()


# # Public
api.add_resource(rts._token, '/api/getToken') # En el token debe estar los datos de conexion y el role del usuario

# # Protected
# Roles
api.add_resource(rts._getRoles, '/api/protected/roles/getRoles')

# Structure
api.add_resource(rts._getGroups, '/api/protected/structure/getGroups')
api.add_resource(rts._getProcesses, '/api/protected/structure/getProcesses')
api.add_resource(rts._getValidations, '/api/protected/structure/getValidations')

api.add_resource(rts._getSingleProcess, '/api/protected/structure/getSingleProcess')
api.add_resource(rts._getSingleGroup, '/api/protected/structure/getSingleGroup')
# api.add_resource(rts._createItem, '/api/protected/structure/createItem') # Recibe un value con la tabla objetivo + un object con su estructura / retorna json de la estructura completa
# api.add_resource(rts._deleteItem, '/api/protected/structure/deleteItem') # Recibe un value con la tabla objetivo + id del objeto a eliminar / retorna json de la estructura completa
# api.add_resource(rts._updateItem, '/api/protected/structure/updateItem') # Recibe un value con la tabla objetivo + un object con su estructura / retorna json de la estructura completa

# Templates
api.add_resource(rts._getTemplate, '/api/protected/templates/getTemplate') # Recibe id de la estructura de validacion / retorna excel

# Data
api.add_resource(rts._validateData, '/api/protected/dataVal/validateData') # Recibe id de la estructura de validacion + data / retorna un listado de errors o un totalizado con ok
api.add_resource(rts._insertData, '/api/protected/dataVal/insertData') # Recibe el nombre de la tabla SQL a la que ingresara + data / retorna un ok o error

# Alerts
# # api.add_resource(rts._alerts, '/api/protected/alerts/getAlerts') # ?
#api.add_resource(rts._mailAlerts, '/api/protected/alerts/mailAlerts') # Mandar los 3 casos de alertas

# Maestros
# api.add_resource(rts._listDD,'/api/protected/masters/listDD') # Retorna listado de datos distribuidoras segun conexion
# api.add_resource(rts._crudDD,'/api/protected/masters/crudDD') # Recibe Array de objetos tipo distribuidora + una key: 'delete', 'add', 'update' la cual dictara que hara el procedure / retorn ok o listado de errores

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=3008, threads=8) # Solo para produccion
    app.run(host='0.0.0.0', port=3100, debug=True)