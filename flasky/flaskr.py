# -*- coding: utf-8 -*-


import os
from sqlite3 import dbapi2 as sqlite3

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory, Blueprint, current_app
from werkzeug import secure_filename
from flask_restful import Resource, reqparse
#from flask_wtf import
from flasky import files

main = Blueprint('flasky', __name__)

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
    rv = sqlite3.connect(current_app.config['DATABASE'][0])
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



@main.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


# @main.route('/add', methods=['POST'])
# def add_entry():
#     if not session.get('logged_in'):
#         abort(401)
#     db = get_db()
#     db.execute('insert into entries (title, text) values (?, ?)',
#                [request.form['title'], request.form['text']])
#     db.commit()
#     flash('New entry was successfully posted')
#     return redirect(url_for('show_entries'))
#
#
@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != main.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != main.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
#
@main.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        filename = files.save(request.files['photo'])
        file_url = files.url(filename)
        # rec = Photo(filename=filename, user=g.user.id)
        # rec.store()
        flash("Photo saved.")
        return redirect(url_for("show",name=filename))
    return render_template("upload.html")

@main.route('/show')
def show_all():
    photos_list = os.listdir(current_app.config['UPLOADED_PHOTOS_DEST'][0])
    return render_template('show_all.html', photos_list=photos_list)

@main.route('/show/<filename>')
def show(filename):
    if filename is None:
        abort(404)
    file_url = files.url(filename)
    return render_template('show.html', file_url=file_url, filename=filename)

@main.route('/download/<filename>', methods=['GET'])
def download(filename):
    directory = './data'
    return send_from_directory(directory, filename, as_attachment=True)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
