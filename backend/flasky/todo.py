from flask import Blueprint, jsonify, request, send_file, make_response,current_app
from flask_restful import reqparse, abort, Api, Resource
# from flasky.utils import allow_cross_domain
from flask_cors import CORS
# from flask_uploads import images
from flasky import files
import os
from flasky.models import User, Role, db


todo = Blueprint('todo', __name__)
CORS(todo)
api = Api(todo)

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

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("task", type=str, required=True, help="No tasks here", location='json')

    def get(self, todo_id):
        print(request);
        if abort_if_todo_doesnt_exist(todo_id):
            for task in TODOS:
                if task['id'] == int(todo_id):
                    return jsonify(task),200
        # return 404

    def delete(self, todo_id):
        # print(type(request))
        print(request.data)
        id = int(todo_id)
        if abort_if_todo_doesnt_exist(todo_id):
            for task in TODOS:
                if id == task['id']:
                    TODOS.remove(task)
                    return jsonify(TODOS), 204
    #
    def put(self, todo_id):
        # args = parser.parse_args()
        task_temp = request.json['task']
        todo_id = int(todo_id)
        if abort_if_todo_doesnt_exist(todo_id):
            for task in TODOS:
                if todo_id == task['id']:
                    task['task'] = task_temp
                    return jsonify(task)

    def post(self, todo_id):
        # args = parser.parse_args()
        print(request.json)
        todo = {
            'id': TODOS[-1]['id']+1,
            'task': request.json['task']
        }
        TODOS.append(todo)
        print(TODOS[-1])
        return TODOS[-1], 201

    # def options(self, todo_id):
    #     return 200
# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("task", type=str, required=True, help="No tasks here", location='json')


    def get(self):
        rst = make_response(jsonify(TODOS))
        return rst,200


# class getTasks(Resource):
#     def get(self):
#         return jsonify({"tasks": tasks})


# class addTask(Resource):
#     def post(self):
#         print(request)
#         if request.json['title'] == "":
#             abort(400)
#         print(request.json['title'])
#         task = {
#             'id': tasks[-1]['id'] + 1,
#             'title': request.json['title'],
#             'description': request.json.get('description', ""),
#             'done': False
#         }
#         tasks.append(task)
#         print(tasks)
#         return jsonify({'tasks': tasks})
#
#
# class deleteTask(Resource):
#     def delete(self):
#         task_id = request.json['id']
#         for task in tasks:
#             if task_id == task['id']:
#                 tasks.remove(task)
#                 return jsonify({'tasks': tasks}), 201


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

# api.add_resource(test, "/api")
# api.add_resource(getTasks, "/api/tasks")
# api.add_resource(addTask, "/api/addTask")
# api.add_resource(deleteTask, "/api/deleteTask")
api.add_resource(TodoList, '/api/todos/')
api.add_resource(Todo, '/api/todos/<todo_id>')
# api.add_resource(upload, '/api/upload')