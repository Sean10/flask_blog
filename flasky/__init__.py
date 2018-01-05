from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from flask_uploads import UploadSet, configure_uploads,\
 patch_request_class,IMAGES
from config import config
from flask_restful import Api
from flask_bootstrap import Bootstrap
import os


api = Api()
bootstrap = Bootstrap()
files = UploadSet('photos',IMAGES)

def create_app(config=None):
    app = Flask(__name__)

    bootstrap.init_app(app)
    api.init_app(app)


    app.config.from_object(config)
    app.config.from_envvar('FLASKY_SETTINGS', silent=True)

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