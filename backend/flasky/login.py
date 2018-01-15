#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13/01/2018 10:46 PM
# @Author  : Shark
# @Site    : 
# @File    : login.py
# @Software: PyCharm

from . import auth, users, auth_code, oauth_redirect_uri, db
from .models import User

from datetime import datetime, timedelta
from flask import Blueprint, request, session, flash, redirect, url_for, make_response, abort, jsonify,g
import base64

author = Blueprint('author',__name__)

@author.route('/api/signup', methods = ['POST'])
def sign_up():
    print(request.headers)
    print(request.get_json())
    username = request.form['username']
    password = request.form['password']
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201

@author.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %r'  % g.user.username } )

@auth.verify_password
def verify_password(username_or_token, password):
    if password == None:
        user = User.verify_auth_token(username_or_token)
        return True

    user = User.query.filter_by(username = username_or_token).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)[0]
    return None

@author.route('/', methods=['POST'])
def login():
    # print(request.headers)
    print(request.form)
    print(request.cookies)
    username = request.form.get('username')
    password = request.form.get('password')
    token = request.form.get('token')
    print(token)
    if token != None:
        user = User.verify_auth_token(token)
        return "succeed",200
    # print(username,password)
    user = User.query.filter_by(username=username).first()
    print(user)
    if not user or not user.verify_password(password):
        return jsonify({"error":"failed to login"}), 204
    #return jsonify({"username":user.username}), 200
    # uid = dict()
    # uid['username'] = user.username
    res = make_response("succeed")
    res.set_cookie('token', user.generate_auth_token(), httponly=True)
    return res,200


    # error = None
    #
    # uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).decode().split(':')
    # print(uid,pw)
    # print(users.get(uid))
    # # uid = request.form['username']
    # # pw = request.form['password']
    # if pw in users.get(uid):
    #     return gen_token(uid)
    # else:
    #     return "error"

@author.route('/logout')
def logout():
    pass
    # session.pop('logged_in', None)
    # flash('You were logged out')
    # return redirect(url_for('flasky.show_entries'))

# @author.route('/oauth', methods=['GET', 'POST'])
# def oauth():
#     if request.method == "POST" and request.form['user']:
#         u = request.form['user']
#         p = request.form['pw']
#         print(u,p)
#         if users.get(u)[0] == p and oauth_redirect_uri:
#             uri = oauth_redirect_uri[0] + '?code=%s' % gen_auth_code(oauth_redirect_uri[0])
#             expire_date = datetime.now() + timedelta(minutes=1)
#             resp = make_response(redirect(uri))
#             resp.set_cookie('login', '_'.join([u,p]), expires=expire_date)
#             return resp
#             # print(uri)
#             # return redirect(uri)
#     if request.args.get('code'):
#         auth_info = auth_code.get(int(request.args.get('code')))
#         print(auth_info)
#         print(request.args.get("redirect_uri"))
#         if auth_info == request.args.get('redirect_uri'):
#             print("succeed")
#             # 可以在授权码的auth_code中存储用户id,存进token中
#             return gen_token(dict(client_id=request.args.get("client_id")))
#     if request.args.get('redirect_uri'):
#         print(request.args)
#         oauth_redirect_uri.append(request.args.get('redirect_uri'))
#         if request.cookies.get('login'):
#             u, p = request.cookies.get('login').split('_')
#             if users.get(u)[0] == p:
#                 uri = oauth_redirect_uri[0] + "?code=%s" % gen_auth_code(oauth_redirect_uri[0])
#                 return redirect(uri)
#     # print(oauth_redirect_uri)
#         return '''
#             <form action="" method="post">
#                 <p><input type=text name=user></p>
#                 <p><input type=text name=pw></p>
#                 <p><input type=submit value=Login></p>
#                 </form>
#         '''