from flask import Blueprint, jsonify

from APP.extentions import shitBuilder, shits

apiUser = Blueprint('apiUser', __name__)


def init_api_user(app):
    app.register_blueprint(blueprint=apiUser, url_prefix='/api/user/')


@apiUser.route('/login', methods=['GET', 'POST'])
@apiUser.route('/logout', methods=['GET', 'POST'])
def test():
    return jsonify(shitBuilder)


@apiUser.route('/info', methods=['GET', 'POST'])
def api_user_info():
    # role
    return jsonify(shits)
