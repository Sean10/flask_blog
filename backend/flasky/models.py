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

import random
import json
import base64
import hmac
import time

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
    """
    用户信息模型
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True, server_default='', index=True)
    password_hash = db.Column(db.String(255), nullable=False, server_default='0')
    token = db.Column(db.String(255), nullable=False, server_default="")

    def __repr__(self):
        return '<Username %r, Password %r>' % (self.username, self.password_hash)

    def hash_password(self, password):
        """
        对密码进行MD5 Hash
        :param password:
        :return:
        """
        self.password_hash = pwd_context.encrypt(password)
        # self.password = password

    def verify_password(self, password):
        """
        密码验证
        :param password:
        :return:
        """
        return pwd_context.verify(password, self.password_hash)
        # return password == self.password

    @staticmethod
    def encode_token_bytes(data):
        """
        加密为base64 token
        :param data:
        :return:
        """
        return base64.urlsafe_b64encode(data)

    @staticmethod
    def decode_token_bytes(data):
        """
        解密base64 token
        :param data:
        :return:
        """
        return base64.urlsafe_b64decode(data)

    def generate_auth_token(self, expiration=600):
        '''
        生成认证token
        :param uid: dict type
        :return: base64 str
        '''
        data = dict()
        data['username'] = self.username
        if "salt" not in data:
            data["salt"] = str(random.random())
        if "expires" not in data:
            data["expires"] = time.time() + expiration
        payload = json.dumps(data).encode("utf-8")
        # 生成签名
        sig = self._get_signature(payload)
        self.token = self.encode_token_bytes(payload + sig)
        return self.token
        # token = base64.b64encode((":".join([str(uid), str(random.random()), str(time.time() + 7200)])).encode('utf-8'));
        # users[uid].append(token)
        # return token

    @staticmethod
    def verify_auth_token(token):
        """
        解析token
        :param token:
        :return:
        """
        decoded_token = User.decode_token_bytes(token)
        payload = decoded_token[:-16]
        sig = decoded_token[-16:]
        # 生成签名
        expected_sig = User._get_signature(payload)
        if sig != expected_sig:
            return {}
        data = json.loads(payload.decode("utf-8"))
        if data.get('expires') >= time.time():
            user = User.query.filter_by(username=data.get('username'))
            return user
        return None

    @staticmethod
    def _get_signature(value):
        """
        HMAC加密
        :param value:
        :return:
        """
        return hmac.new(b'secret123456', value).digest()



class TodoList(db.Model):
    """
    TodoList 模型
    """
    __tablename__ = "todolist"
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    task = db.Column(db.String(255), nullable=False, server_default='')
    user = db.Column(db.String(32), nullable=False, server_default='')

    def __repr__(self):
        return 'id: %r, task: %r user: %r' % (self.id, self.task, self.user)

