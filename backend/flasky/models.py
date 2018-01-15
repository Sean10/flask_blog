#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13/01/2018 3:15 PM
# @Author  : Shark
# @Site    : 
# @File    : models.py
# @Software: PyCharm

from . import db
from passlib.apps import custom_app_context as pwd_context
from marshmallow import Schema, fields, pprint

class marUser(object):
    def __init__(self, id, task, user):
        self.id = id
        self.task = task
        self.user = user

class marUserSchema(Schema):
    id = fields.Int()
    task = fields.Str()
    user = fields.Str()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    # password = db.Column(db.String(32), nullable=False, server_default='0')
    password_hash = db.Column(db.String(255), nullable=False, server_default='0')

    def __repr__(self):
        return '<Username %r, Password %r>' % (self.username, self.password_hash)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        # self.password = password

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
        # return password == self.password

    # def generate_auth_token(self, expiration=600):
    #     s = marUserSchema()


class TodoList(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    task = db.Column(db.String(255), nullable=False, server_default='')
    user = db.Column(db.String(32), nullable=False, server_default='')

    def __repr__(self):
        return 'id: %r, task: %r user: %r' % (self.id, self.task, self.user)

