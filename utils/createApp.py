from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended.utils import (
    create_refresh_token,
    decode_token
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token
)

from constants import api_config



def createApp(__name__):

    app = Flask(__name__)
    app.config.from_object(api_config)
    jwt = JWTManager(app)
    CORS(app, expose_headers=["filename"], resources={r"*": {"origins": "*"}})

    @app.route("/api/refresh", methods=["POST"])
    def refresh():
        token = request.json.get('refreshToken', '')
        payload = decode_token(token)['sub']
        hasura_token = {}
        hasura_token["hasura_claims"] = decode_token(token)['hasura_claims']
        print(payload)
        if token == '':
            return { 'error': 'token no enviado' }, 401
        access_token = create_access_token(identity=payload, additional_claims=hasura_token)
        refresh_token = create_refresh_token(identity=payload, additional_claims=hasura_token)
        return { "accessToken" : access_token, "refreshToken": refresh_token }

    @jwt.token_verification_failed_loader
    def token_verification_failed_loader_callback(jwt_header, jwt_payload):
        response = { "error" : "token invalido" }, 401
        return response

    @jwt.invalid_token_loader
    def invalid_token_loader_callback(jwt_header):
        response = { "error" : "token invalido" }, 401
        return response

    @jwt.unauthorized_loader
    def unauthorized_loader_callback(jwt_header):
        response = { "error" : "token invalido" }, 401
        return response

    @jwt.expired_token_loader
    def expired_token_loader_callback(jwt_header, two):
        response = { "error" : "token expirado" }, 401
        return response

    @jwt.needs_fresh_token_loader
    def needs_fresh_token_loader(jwt_header):
        response = { "error" : "token invalido" }, 401
        return response

    api = Api(app)
    return app, api
    