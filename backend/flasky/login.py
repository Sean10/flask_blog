#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 13/01/2018 10:46 PM
# @Author  : Shark
# @Site    : 
# @File    : login.py
# @Software: PyCharm

from ..flasky import auth, users

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)[0]
    return None