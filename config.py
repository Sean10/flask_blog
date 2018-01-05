
from flask_bootstrap import Bootstrap
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory, jsonify
import os

class config():

    # Load default config and override config from an environment variable
    DATABASE = os.path.join(os.getcwd(), 'flaskr.db')
    DEBUG = True
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'
    UPLOADED_FILES_DEST = "./data"
