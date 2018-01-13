#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/01/2018 5:22 PM
# @Author  : Shark
# @Site    : 
# @File    : test_api.py
# @Software: PyCharm

import requests
import json

headers = {'Content-Type': 'application/json'}
p1 = requests.get("http://127.0.0.1:5000/todo/api/todos")
print(p1.text)
#
#
# p3 = requests.get("http://127.0.0.1:5000/todo/api/todos/3")
# print(p3.text)

# payload = {'task': "new test"}
# print(payload)
# print(json.dumps(payload))
# headers = {'Content-Type': 'application/json'}
# p2 = requests.post("http://127.0.0.1:5000/todo/api/todos/2", data=json.dumps(payload), headers=headers)
# print(p2.text)

#
# p4 = requests.delete("http://127.0.0.1:5000/todo/api/todos/2")
# print(p4.text)
# payload = {'task': "new test"}
# p5 = requests.put("http://127.0.0.1:5000/todo/api/todos/3", data=json.dumps(payload), headers=headers)
# print(p5.text)