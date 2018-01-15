#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/01/2018 5:22 PM
# @Author  : Shark
# @Site    : 
# @File    : test_api.py
# @Software: PyCharm

import requests
import json

# headers = {'Content-Type': 'application/json'}

# test login api
# headers['Authorization'] = "admin:admin"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}


# sign = {"username":"sean10", "password":"default"}
# auth1 = requests.post("http://127.0.0.1:5000/author/api/signup", headers=headers,data=sign)
# print(auth1)


# test resource right check
# auth2 = requests.post("http://127.0.0.1:5000/author/api/resource")

# test login
# sign = {"username":"sean10", "password":"default"}
# login = requests.post("http://127.0.0.1:5000/author/",data=sign)
# print(login.text)

# test login with token
sign = {"token":"eyJ1c2VybmFtZSI6ICJzZWFuMTAiLCAic2FsdCI6ICIwLjgzMjM3MjU1MTA1NDUwMTciLCAiZXhwaXJlcyI6IDE1MTYwMDcxMTMuMTIyOTkzfehiOt53_QzWW_jJwhh1rZs="}
login = requests.post("http://127.0.0.1:5000/author/", data=sign)
print(login.text)


# test todo api
# p1 = requests.get("http://127.0.0.1:5000/todo/api/todos")
# print(p1.text)
#
#
# p3 = requests.get("http://127.0.0.1:5000/todo/api/todos/3")
# print(p3.text)
#
# payload = {'task': "new test"}
# print(payload)
# print(json.dumps(payload))
# headers = {'Content-Type': 'application/json'}
# p2 = requests.post("http://127.0.0.1:5000/todo/api/todos/2", data=json.dumps(payload), headers=headers)
# print(p2.text)

#
# p4 = requests.delete("http://127.0.0.1:5000/todo/api/todos/3")
# print(p4.text)

# payload = {'task': "new hello"}
# p5 = requests.put("http://127.0.0.1:5000/todo/api/todos/3", data=json.dumps(payload), headers=headers)
# print(p5.text)