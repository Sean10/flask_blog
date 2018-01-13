
import pymysql
import os

class config():

    # Load default config and override config from an environment variable
    DATABASE = os.path.join(os.getcwd(), 'flaskr.db')
    DEBUG = True
    SECRET_KEY = 'development key'
    UPLOADED_FILES_DEST = "./data"
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost:3306/test_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
