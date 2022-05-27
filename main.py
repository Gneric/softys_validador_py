from utils.createApp import createApp
from api.routes.routes import Routes
from waitress import serve

# Creacion de la app / api
app, api = createApp(__name__)
# Instanciamiento de Rutas
rts = Routes()


# # Public
api.add_resource(rts._token, '/api/getToken')

# # Protected
# Templates
api.add_resource(rts._getTemplate, '/api/protected/getTemplate')
# Data
api.add_resource(rts._validateData, '/api/protected/validateData')
api.add_resource(rts._insertData, '/api/protected/insertData')
# Alerts
api.add_resource(rts._alerts, '/api/protected/getAlerts')

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=3100, threads=8) # Solo para produccion
    app.run(host='0.0.0.0', port=3100, debug=True)