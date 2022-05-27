from flask import send_from_directory
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from os import getcwd
from os.path import join

class downloadTemplate(Resource):
    @jwt_required()
    def post(self):
        try:
            template_path = join(getcwd(), 'assets')
            return send_from_directory(template_path, 'plantilla_dts.xlsx', as_attachment=True)
        except:
            return { 'error': 'error en la generacion del archivo ProductosSinClasificar' }, 400


