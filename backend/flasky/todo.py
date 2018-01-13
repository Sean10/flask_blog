from flask import Blueprint, jsonify, request, send_file, make_response, current_app,abort
# from flask_restful import reqparse, abort, Api, Resource
# from flasky.utils import allow_cross_domain
from flask_cors import CORS
from marshmallow import Schema, fields, pprint
# from flask_uploads import images
from . import files, auth
import os

# from flasky.models import User, Role, db


todo = Blueprint('todo', __name__)
CORS(todo)
# api = Api(todo)
# parser = reqparse.RequestParser()
# parser.add_argument('task', type=str)

TODOS = [
    {'id': 1,
     'task': u'build an API'
     },
    {'id': 2,
     'task': u'?????'
     },
    {
        'id': 3,
        'task': u'profit!'
    }
]


def abort_if_todo_doesnt_exist(todo_id):
    temp_id = int(todo_id)

    print(type(temp_id))
    for task in TODOS:
        # print(type(task['id']), type(todo_id))
        if task['id'] == temp_id:
            print("succeed")
            return True
    abort(404, message="Todo {} doesn't exist".format(todo_id))
    return False

@todo.route('/api/todos/<todo_id>', methods=['Get'])
def getTodo(todo_id):
    print(request);
    abort_if_todo_doesnt_exist(todo_id)
    for task in TODOS:
        if task['id'] == int(todo_id):
            return jsonify(task), 200

@todo.route('/api/todos/<todo_id>', methods=['PUT'])
def putTodo(todo_id):
    task_temp = request.json['task']
    todo_id = int(todo_id)
    abort_if_todo_doesnt_exist(todo_id)
    for task in TODOS:
        if todo_id == task['id']:
            task['task'] = task_temp
            return jsonify(task), 202

@todo.route('/api/todos/<todo_id>', methods=['DELETE'])
def deleteTodo(todo_id):
    print(request.data)
    id = int(todo_id)
    abort_if_todo_doesnt_exist(todo_id)
    for task in TODOS:
        if id == task['id']:
            TODOS.remove(task)
            return jsonify(TODOS), 204

@todo.route('/api/todos/<todo_id>', methods=['POST'])
def postTodo(todo_id):
    print(request.json)
    args = request.json['task']
    todo = {
        'id': TODOS[-1]['id'] + 1,
        'task': args
    }
    TODOS.append(todo)
    print(TODOS[-1])
    return jsonify(TODOS[-1]), 201

@todo.route('/api/todos', methods=['GET'])
def getTodoList():
    return jsonify(TODOS), 200

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

