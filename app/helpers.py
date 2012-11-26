import httplib
from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

class HttpResponse:
    @staticmethod
    def OK(data):
        response = jsonify(data)
        response.status_code = httplib.OK

        return response

    @staticmethod
    def UNAUTHORIZED(body_message='Please authenticate.'):
        message = {'message': body_message}
        response = jsonify(message)

        response.status_code = httplib.UNAUTHORIZED
        response.headers['WWW-Authenticate'] = 'Basic realm="Example"'

        return response

    @staticmethod
    def BAD_REQUEST(body_message):
        message = {'message': body_message}
        response = jsonify(message)

        response.status_code = httplib.BAD_REQUEST

        return response

    @staticmethod
    def CONFLICT(body_message):
        message = {'message': body_message}
        response = jsonify(message)

        response.status_code = httplib.CONFLICT

        return response


def make_json_app(import_name, **kwargs):
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app