#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 10/01/2018 5:22 PM
# @Author  : Shark
# @Site    : 
# @File    : test_api.py
# @Software: PyCharm

import unittest
import requests
import datetime
import json

# 测试报告邮件内容
text = ""

# 用例统计
num_success = 0
num_fail = 0



    # 发生邮件测试报告
    # Send_email.send_email(text)
def test_success():
    global num_success
    num_success += 1
    print_out(u"测试结果：通过\n")


# 测试不通过
def test_fail(txt):
    global num_fail
    num_fail += 1
    print_out(u"测试结果：不通过 \n错误信息： " + txt + "\n")


# 邮件内容写入 & 客户端输出
def print_out(message):
    global text
    text += "\n" + message
    print(message)


# 返回值判断
def test_result(result, code):
    if result == code:
        test_success()
        return "pass"
    else:
        txt = u"期望返回值:" + str(code) + u" 实际返回值:" + str(result)
        test_fail(txt)
        return "fail"



class test_API(unittest.TestCase):
    # def __init__(self):
    #     self.url = "http://localhost:5000"
    #     self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def setUp(self):
        self.url = "http://localhost:5000"
        self.form_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.json_headers = {'Content-Type': 'application/json'}



    def tearDown(self):
        print("Test has done!")

    def test_signup(self):
        sign = {"username": "sean10", "password": "default"}
        auth1 = requests.post("http://127.0.0.1:5000/author/api/signup", headers=self.form_headers, data=sign)
        info = auth1.text
        # assert(info['username'] == sign['username'])
        # self.assertEqual(auth1.status_code, 201)
        test_result(auth1.status_code, 201)

    def test_login_success(self):
        info = {"username":"sean10", "password":"default"}
        login = requests.post("http://127.0.0.1:5000/author/",data=info)
        print(login.text)
        res = login.text
        print(res)
        # assert(login[''] == 'succeed')
        # self.assertEqual(login.status_code, 200)
        test_result(login.status_code, 200)

    # test login with token
    def test_login_token(self):
        sign = {
            "token": "eyJ1c2VybmFtZSI6ICJzZWFuMTAiLCAic2FsdCI6ICIwLjgzMjM3MjU1MTA1NDUwMTciLCAiZXhwaXJlcyI6IDE1MTYwMDcxMTMuMTIyOTkzfehiOt53_QzWW_jJwhh1rZs="}
        login = requests.post("http://127.0.0.1:5000/author/", data=sign)
        print(login.text)
        test_result(login.status_code, 200)

    # test todo api
    def test_get_todoList(self):
        p1 = requests.get("http://127.0.0.1:5000/todo/api/todos")
        # print(p1.text)
        test_result(p1.status_code, 200)

    def test_get_todo(self):
        p3 = requests.get("http://127.0.0.1:5000/todo/api/todos/3")
        # print(p3.text)
        test_result(p3.status_code, 200)

    def test_post_todo(self):
        payload = {'task': "new testss",'user':"admin"}
        cookie = {"uid": "admin","token": "eyJ1c2VybmFtZSI6ICJzZWFuMTAiLCAic2FsdCI6ICIwLjgzMjM3MjU1MTA1NDUwMTciLCAiZXhwaXJlcyI6IDE1MTYwMDcxMTMuMTIyOTkzfehiOt53_QzWW_jJwhh1rZs="}
        print(payload)
        print(json.dumps(payload))
        p2 = requests.post("http://127.0.0.1:5000/todo/api/todos/2", data=json.dumps(payload), cookies=cookie, headers=self.json_headers)
        # print(p2.text)
        test_result(p2.status_code, 201)

    def test_delete_todo(self):
        p4 = requests.delete("http://127.0.0.1:5000/todo/api/todos/10")
        # print(p4.text)
        test_result(p4.status_code,201)

#
    def test_put_todo(self):
        payload = {'task': "new hello"}
        p5 = requests.put("http://127.0.0.1:5000/todo/api/todos/8", data=json.dumps(payload), headers=self.json_headers)
        # print(p5.text)
        test_result(p5.status_code, 202)



# headers = {'Content-Type': 'application/json'}

# test login api
# headers['Authorization'] = "admin:admin"

# headers = {'Content-Type': 'application/x-www-form-urlencoded'}


# test resource right check
# auth2 = requests.post("http://127.0.0.1:5000/author/api/resource")





#
#

#






# 测试通过



def test_interface():
    # 初始化测试起始时间
    start_time = datetime.datetime.now()

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(test_API("test_signup"))   # 注册
    suite.addTest(test_API("test_login_success"))   # 登录
    suite.addTest(test_API("test_login_token"))   # 登录 token
    suite.addTest(test_API("test_get_todoList"))
    suite.addTest(test_API("test_get_todo"))
    suite.addTest(test_API("test_post_todo"))
    suite.addTest(test_API("test_delete_todo"))
    suite.addTest(test_API("test_put_todo"))


    # suite.addTest(test_API("test_employees"))  # 员工管理
    # suite.addTest(test_API("test_department"))  # 部门管理
    # suite.addTest(test_API("test_work_sys"))  # 工作日历管理
    # suite.addTest(test_API("test_holiday"))  # 节假日管理
    # suite.addTest(test_API("test_queryAp"))  # 智能终端管理
    # suite.addTest(test_API("test_edit_info"))  # 企业信息管理 & 个人信息
    # suite.addTest(test_API("test_data"))  # 每日数据报表 & 月度数据报表

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # 测试执行时间计算
    end_time = datetime.datetime.now()
    total_use_case = u"执行用例总数:" + str(num_success + num_fail) + \
                     u"\t通过数:" + str(num_success) + \
                     u"\t不通过数:" + str(num_fail)
    total_time = u"\t总共耗时：" + str((end_time-start_time).seconds) + u"秒"
    print_out(total_use_case + total_time)

if __name__ == "__main__":
    test_interface()