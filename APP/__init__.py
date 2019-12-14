from flask import Flask

from APP.blueprints.admin import init_admin
from APP.blueprints.api.user import init_api_user
from APP.extentions import init_extentions
from APP.setting import envs
from APP.blueprints.auth import init_auth
from APP.blueprints.home import init_home
from APP import setting


def create_app():
    app = Flask(__name__, template_folder=setting.TEMPLATE_FOLDER)
    app.config.from_object(envs.get('develop'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_blueprint(app)
    init_extentions(app)
    return app


def init_blueprint(app):
    init_auth(app)
    init_home(app)
    init_api_user(app)
    init_admin(app)
    init_api_user(app)
