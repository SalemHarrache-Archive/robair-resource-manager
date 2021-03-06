# -*- coding: utf-8 -*-


class DevConfig(object):
    '''Dev configuration.'''

    SERVER_PATH = "http://localhost"
    SECRET_KEY = "secret_key"
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'security_salt'

    SQLALCHEMY_ECHO = True
    # SQLite Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/robair-portal.db'

    # Server
    DEBUG = True
    TESTING = False
    PORT = 9090
    HOST = "127.0.0.1"


class ProdConfig(DevConfig):
    '''Prod configuration.'''
    PORT = 7060
    SQLALCHEMY_ECHO = False
    # Database
    DBUSER = "robair"
    DBPASSWORD = "robair"
    DBNAME = "robair"
    DBHOST = "localhost"

    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s/%s" % (
        DBUSER, DBPASSWORD, DBHOST, DBNAME)
    SQLALCHEMY_ECHO = False
    # Debug
    DEBUG = False
    TESTING = False
