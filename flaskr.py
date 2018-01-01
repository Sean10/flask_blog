# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~
    A microblog example application written as Flask tutorial with
    Flask and sqlite3.
    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory
from werkzeug import secure_filename
from flask_uploads import UploadSet, configure_uploads,\
 patch_request_class,IMAGES
from flask_bootstrap import Bootstrap
#from flask_wtf import

# create our little application :)
app = Flask(__name__)
bootstrap = Bootstrap(app)
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['UPLOADED_PHOTOS_DEST'] = "./data"

files = UploadSet('photos',IMAGES)
configure_uploads(app, files)
patch_request_class(app)  # 文件大小限制，默认为16MB

app.config['SECRET_KEY'] = 'a random string'


from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'mysite',
        View('Home', 'login'),
    )

nav.init_app(app)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = files.save(request.files['photo'])
        file_url = files.url(filename)
        # rec = Photo(filename=filename, user=g.user.id)
        # rec.store()
        flash("Photo saved.")
        return redirect(url_for("show",name=filename))
    return render_template("upload.html")

@app.route('/show')
def show_all():
    photos_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('show_all.html', photos_list=photos_list)

@app.route('/show/<filename>')
def show(filename):
    if filename is None:
        abort(404)
    file_url = files.url(filename)
    return render_template('show.html',file_url=file_url,filename=filename)

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    directory = './data'
    return send_from_directory(directory, filename, as_attachment=True)
