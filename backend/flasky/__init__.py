from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from flask_uploads import UploadSet, configure_uploads,\
 patch_request_class,IMAGES, TEXT, DOCUMENTS, DATA, AUDIO
# from ..config import configx
from flask_restful import Api
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore,Security, UserMixin,RoleMixin
import os


api = Api()
bootstrap = Bootstrap()
# db = SQLAlchemy()
DEFAULT = TEXT + DOCUMENTS + IMAGES + DATA + AUDIO
files = UploadSet('files',DEFAULT)
users = {
    "admin": ["default"]
}

# roles_users = db.Table('roles_users',
#         db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
#         db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
#
# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     description = db.Column(db.String(255))
#
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean())
#     confirmed_at = db.Column(db.DateTime())
#     last_login_at = db.Column(db.DateTime())
#     current_login_at = db.Column(db.DateTime())
#     last_login_ip = db.Column(db.String(63))
#     current_login_ip = db.Column(db.String(63))
#     login_count = db.Column(db.Integer)
#     roles = db.relationship('Role', secondary=roles_users,
#                             backref=db.backref('users', lazy='dynamic'))
#     def __repr__(self):
#         return '<User %r>' % self.email
#
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# security = Security()

auth_code = {

}
oauth_redirect_uri = []

def create_app(config=None):
    app = Flask(__name__)

    bootstrap.init_app(app)
    api.init_app(app)
    # db.init_app(app)
    # security.init_app(app, user_datastore)


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