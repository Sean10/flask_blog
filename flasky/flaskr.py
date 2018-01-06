# -*- coding: utf-8 -*-


import os
from sqlite3 import dbapi2 as sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory, Blueprint, current_app, jsonify
#from werkzeug import secure_filename
from flask_restful import Resource, reqparse
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
import time
import hashlib
import base64

from flasky import files, users
from flasky.utils import  gen_token, verify_token

flasky = Blueprint('flasky', __name__)




# 文件大小限制，默认为16MB

# parser = reqparse.RequestParser()
#
#
# class Flasky(Resource):
#     def show_entries(self):
#         db = get_db()
#         cur = db.execute('select title, text from entries order by id desc')
#         entries = cur.fetchall()
#         return render_template('show_entries.html', entries=entries)
#
# api.add_resource(Flasky, '/')

def connect_db():
    """Connects to the specific database."""
    print(current_app.config['DATABASE'])
    print(type(current_app.config['DATABASE']))
    rv = sqlite3.connect(current_app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current mainlication context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db



@flasky.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@flasky.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))



@flasky.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html', error=error)

    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).decode().split(':')
    print(uid,pw)
    print(users.get(uid))
    # uid = request.form['username']
    # pw = request.form['password']
    if pw in users.get(uid):
        return gen_token(uid)
    else:
        return "error"

    # error = None
    #
    #
    # if request.method == 'POST':
    #     if request.form['username'] not in users.keys():
    #         error = 'Invalid username'
    #     elif request.form['password'] != users[request.form['username']][0]:
    #         error = 'Invalid password'
    #     else:
    #         session['logged_in'] = True
    #         flash('You were logged in')
    #         return redirect(url_for('flasky.show_entries'))
    # return render_template('login.html', error=error)


@flasky.route('/test', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token):
        return 'data'
    else:
        return "error"

@flasky.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('flasky.show_entries'))
#

class UploadForm(FlaskForm):
    file = FileField(validators=[
        FileAllowed(files, u'只能上传文件！'),
        FileRequired(u'文件未选择！')])
    #print("ERROR\n")
    submit = SubmitField(u'上传')


@flasky.route('/upload', methods=['GET','POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        for filedata in request.files.getlist('file'):
            name = hashlib.md5(('admin' + str(time.time())).encode('UTF-8')).hexdigest()[:15]
            filename = files.save(filedata, name=name+'.')
            flash("Succeed to upload")
            #file_url = files.url(filename)
    else:
        #file_url = None
        filename = None
    return render_template('upload.html', form=form,name=filename)

@flasky.route('/show')
def show_all():
    photos_list = os.listdir(current_app.config['UPLOADED_FILES_DEST'])
    return render_template('show_all.html', photos_list=photos_list)

@flasky.route('/show/<filename>')
def show(filename):
    if filename is None:
        abort(404)
    file_url = files.url(filename)
    return render_template('show.html', file_url=file_url, filename=filename)

@flasky.route('/download/<filename>', methods=['GET'])
def download(filename):
    directory = os.path.join(os.getcwd(),current_app.config['UPLOADED_FILES_DEST'])
    # print(directory)
    # print(filename)
    return send_from_directory(directory, filename, as_attachment=True)

@flasky.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@flasky.route('/course', methods=['GET'])
def course():
    return render_template("course.html")


@flasky.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
