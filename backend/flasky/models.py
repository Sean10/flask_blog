#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13/01/2018 3:15 PM
# @Author  : Shark
# @Site    : 
# @File    : models.py
# @Software: PyCharm

from . import db

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)


    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    role_id = db.Column(db.Integer, nullable=False, server_default='0')
    def __repr__(self):
        return '<User %r,Role id %r>' %(self.username,self.role_id)

class UserPW(db.Model):
    __tablename__ = "usernamepassword"
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    password = db.Column(db.String(32), nullable=False, server_default='0')

    def __repr__(self):
        return '<Username %r, Password %r>' % (self.username, self.password)

