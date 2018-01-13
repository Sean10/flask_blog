from flask import Flask
from werkzeug.utils import find_modules, import_string
from flask_uploads import UploadSet, configure_uploads,\
 patch_request_class,IMAGES, TEXT, DOCUMENTS, DATA, AUDIO
from flask_restful import Api
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_security import SQLAlchemyUserDatastore,Security, UserMixin,RoleMixin
import os

api = Api()
bootstrap = Bootstrap()
db = SQLAlchemy()
auth = HTTPBasicAuth()
DEFAULT = TEXT + DOCUMENTS + IMAGES + DATA + AUDIO
files = UploadSet('files',DEFAULT)
users = {
    "admin": ["admin"]
}

auth_code = {

}
oauth_redirect_uri = []

def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object(config)
    app.config.from_envvar('FLASKY_SETTINGS', silent=True)

    bootstrap.init_app(app)
    api.init_app(app)
    # with app.app_context():
    app.app_context().push();
    db.init_app(app)

    configure_uploads(app, files)
    patch_request_class(app)

    return app

def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('flasky'):
        mod = import_string(name)
        if hasattr(mod, 'main'):
            app.register_blueprint(mod.bp)
    return None





