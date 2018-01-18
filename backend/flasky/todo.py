

from flask import Blueprint, jsonify, request, send_file, make_response, current_app,abort
# from flask_restful import reqparse, abort, Api, Resource
# from flasky.utils import allow_cross_domain
from marshmallow import Schema, fields, pprint
# from flask_uploads import images
from . import files, auth, db
from .models import TodoList
import os

# from flasky.models import User, Role, db


todo = Blueprint('todo', __name__)
# CORS(todo)


class marTodo(object):
    def __init__(self, id, task, user):
        self.id = id
        self.task = task
        self.user = user

class marTodoSchema(Schema):
    id = fields.Int()
    task = fields.Str()
    user = fields.Str()

schema = marTodoSchema()




# TODOS = [
#     {'id': 1,
#      'task': u'build an API'
#      },
#     {'id': 2,
#      'task': u'?????'
#      },
#     {
#         'id': 3,
#         'task': u'profit!'
#     }
# ]




def abort_if_todo_doesnt_exist(todo_id):
    todo_id = int(todo_id)

    TODOS = TodoList.query.filter_by(id=todo_id).first()
    if TODOS != '':
        return TODOS
    abort(404, message="Todo {} doesn't exist".format(todo_id))
    return False

@todo.route('/api/todos/<todo_id>', methods=['Get'])
def getTodo(todo_id):
    """
    获取指定Todo
    :param todo_id:
    :return:
    """
    print(request);
    TODOS = abort_if_todo_doesnt_exist(todo_id)
    if TODOS != False:
        result = schema.dump(TODOS)
        return jsonify(result.data), 200

@todo.route('/api/todos/<todo_id>', methods=['PUT'])
def putTodo(todo_id):
    """
    更新指定Todo
    :param todo_id:
    :return:
    """
    task_temp = request.json['task']
    todo_id = int(todo_id)
    TODOS = abort_if_todo_doesnt_exist(todo_id)
    TODOS.task = task_temp
    db.session.commit()
    print(TODOS)

    TODOS = TodoList.query.filter_by(id=todo_id).first()
    result = schema.dump(TODOS)
    pprint(result.data)
    return jsonify(result), 202

@todo.route('/api/todos/<todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    """
    删除指定Todo
    :param todo_id:
    :return:
    """
    # TODOS = TodoList.query.filter_by(id=todo_id)
    print(request.data)
    TODOS = abort_if_todo_doesnt_exist(todo_id)
    if TODOS == False:
        return jsonify({"error":"no such id"}),404

    db.session.delete(TODOS)
    db.session.commit()
    TODOS = TodoList.query.all()
    result = schema.dump(TODOS, many=True)
    return jsonify(result.data), 201

@todo.route('/api/todos/<todo_id>', methods=['POST'])
def postTodo(todo_id):
    """
    添加新的Todo
    :param todo_id:
    :return:
    """
    print(request.headers)
    print(request.json)
    data = request.form['task']
    re_user = request.cookies.get('uid')
    db.session.add(TodoList(task=data,user=re_user))
    db.session.commit()
    TODO = TodoList.query.order_by(TodoList.id.desc()).first()
    result = schema.dump(TODO)
    return jsonify(result.data), 201

@auth.login_required
@todo.route('/api/todos', methods=['GET'])
def getTodoList():
    """
    获取完整Todolist
    :return:
    """
    re_uid = request.cookies.get('uid')
    TODOS = TodoList.query.filter_by(user=re_uid)
    # print(type(TODOS))
    result = schema.dump(TODOS, many=True)
    # print(result.data)
    return jsonify(result.data), 200

@todo.errorhandler(404)
def handle_api_not_found(error):
    # response 的 json 内容为自定义错误代码和错误信息
    response = jsonify({'error': "not found"})
    # response 返回 error 发生时定义的标准错误代码
    response.status_code = error.status_code

    return response


#
# class test(Resource):
#     def get(self):
#         return send_file("templates/tasks.html")
## Actually setup the Api resource routing here
#
# class upload(Resource):
#     def get(self):
#         fileList = os.listdir(current_app.config['UPLOADED_FILES_DEST'])
#         return jsonify(fileList)
#
#     def post(self):
#         print(request.headers)
#         print(request.files)
#         filename = files.save(request.files['file'])
#         print(filename)
#         return filename
# try:
#     if 'recipe_image' in request.files:
#         filename = files.save(request.files['recipe_image'])
#         self.image_filename = filename
#         self.image_url = files.url(filename)
#     else:
#         json_data = request.get_json()
#         self.recipe_title = json_data['title']
#         self.recipe_description = json_data['description']
#         if 'recipe_type' in json_data:
#             self.recipe_type = json_data['recipe_type']
#         if 'rating' in json_data:
#             self.rating = json_data['rating']
#         if 'ingredients' in json_data:
#             self.ingredients = json_data['ingredients']
#         if 'recipe_steps' in json_data:
#             self.recipe_steps = json_data['recipe_steps']
#         if 'inspiration' in json_data:
#             self.inspiration = json_data['inspiration']
# except KeyError as e:
#     raise ValidationError('Invalid recipe: missing ' + e.args[0])
# return jsonify(self)

