# 设计文档

## 主要功能

可以实现多账户登录，TodoList 增删改查功能

## 主要结构
主要遵循前后端分离思想，Vue.js+Flask技术栈完成

.
├── README.md
├── backend				后端flask工程目录
│   ├── LICENSE
│   ├── README.md
│   ├── config.py		初始化config配置文件
│   ├── data
│   ├── flasky			主要功能模块
│   │   ├── __init__.py	包
│   │   ├── client.py   oauth第三方模拟
│   │   ├── flaskr.py
│   │   ├── login.py	登录功能
│   │   ├── models.py	数据库模型功能
│   │   ├── todo.py		主要TodoList功能
│   │   └── utils.py	组件功能
│   ├── requirements.txt 依赖管理包
│   ├── run.py			 程序运行入口
│   └── test			 单元测试代码
│       └── test_api.py
├── dist				前端打包目录
│   ├── index.html
│   └── static
└── frontend			前端Vue.js工程目录
    ├── README.md
    ├── build/			Webpack自动构建
    ├── config/
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── src				前端源代码文件
    │   ├── App.vue		主app应用
    │   ├── assets		图片等二进制资源
    │   │   ├── logo.png
    │   │   └── profile.jpg
    │   ├── components	功能组件
    │   │   ├── BaseInputText.vue	基本输入组件
    │   │   ├── HelloWorld.vue		调试功能尝试模块
    │   │   ├── TodoList.vue		主要TodoList模块
    │   │   ├── TodoListItem.vue	主要TodoListItem组件
    │   │   ├── footer.vue			页脚组件
    │   │   ├── topbar.vue			导航栏组件
    │   │   └── upload.vue			上传功能组件
    │   ├── main.js
    │   ├── router
    │   │   └── index.js			路由管理
    │   └── view
    │       ├── about.vue
    │       ├── login.vue			登录页面
    │       ├── signup.vue			注册页面
    │       ├── upload_view.vue		上传页面
    │       └── userInfo.vue		用户信息页面
    ├── static
    └── test
