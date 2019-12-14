from flask import Blueprint

apiAdmin = Blueprint('apiAdmin', __name__)


def init_api_user(app):
    app.register_blueprint(blueprint=apiAdmin, url_prefix='/api/admin/')