from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def init_extentions(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    Bootstrap(app)
    DebugToolbarExtension(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    moment = Moment()
    csrf = CSRFProtect()
