# 测试文档

## 测试环境
* virtualenvwrapper
* python3.6

## 测试方法
* 单元测试后端接口

## 测试工具
* unittest 模块
* Request库

## 测试例
suite.addTest(test_API("test_signup"))   # 注册
suite.addTest(test_API("test_login_success"))   # 登录
suite.addTest(test_API("test_login_token"))   # 登录 token
suite.addTest(test_API("test_get_todoList"))
suite.addTest(test_API("test_get_todo"))
suite.addTest(test_API("test_post_todo"))
suite.addTest(test_API("test_delete_todo"))
suite.addTest(test_API("test_put_todo"))

## 测试结果
```
.测试结果：不通过
错误信息： 期望返回值:201 实际返回值:400

Test has done!
succeed
succeed
测试结果：通过

Test has done!
..succeed
测试结果：通过

Test has done!
测试结果：通过

Test has done!
.测试结果：通过

Test has done!
{'task': 'new testss', 'user': 'admin'}
{"task": "new testss", "user": "admin"}
.测试结果：通过

Test has done!
..测试结果：不通过
错误信息： 期望返回值:201 实际返回值:500

Test has done!
测试结果：通过

Test has done!
执行用例总数:8	通过数:6	不通过数:2	总共耗时：1秒
.
----------------------------------------------------------------------
Ran 8 tests in 1.788s

OK
```
