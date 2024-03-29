import os

BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')


def get_db_uri(dbconfig):
    engine = dbconfig.get('ENGINE') or 'mysql'
    driver = dbconfig.get('DRIVER') or 'pymysql'
    user = dbconfig.get('USER') or 'root'
    password = dbconfig.get('PASSWORD') or '789520'
    host = dbconfig.get('HOST') or 'localhost'
    port = dbconfig.get('PORT') or '3306'
    name = dbconfig.get('NAME') or 'library'
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'AFHIU2fqewkljhfadjsfklfaslf2hio'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        "ENGINE": 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '789520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'library'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        "ENGINE": 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '789520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'library'

    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DEBUG = True
    DATABASE = {
        "ENGINE": 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '789520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'library'

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        "ENGINE": 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '789520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'library'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig
}
