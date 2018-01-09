from flask import Blueprint, jsonify, request, send_file, make_response,current_app
from flask_restful import reqparse, abort, Api, Resource
# from flasky.utils import allow_cross_domain
from flask_cors import CORS
# from flask_uploads import images
from flasky import files
import os


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

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        # abort_if_todo_doesnt_exist(todo_id)
        # del TODOS[todo_id]
        # return '', 204

        print(request.json)
        id = request.json['id']
        for task in TODOS:
            if id == task['id']:
                TODOS.remove(task)
                return jsonify(TODOS), 201

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

    def post(self, todo_id):
        # args = parser.parse_args()
        # print(request.json['params'])
        # print(TODOS[-1])
        # todo_id = int(TODOS[-1].lstrip('todo')) + 1
        # print(todo_id)
        # todo_id = 'todo%i' % todo_id
        # data = request.json['params']['task']
        # print(data)
        todo = {
            'id': todo_id,
            'task': request.json['params']['task']
        }
        TODOS.append(todo)
        return TODOS[-1]

    # def options(self, todo_id):
    #     print(request.json)
    #     pass;

# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        rst = make_response(jsonify(TODOS))
        return rst


class getTasks(Resource):
    def get(self):
        return jsonify({"tasks": tasks})


class addTask(Resource):
    def post(self):
        print(request)
        if request.json['title'] == "":
            abort(400)
        print(request.json['title'])
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        print(tasks)
        return jsonify({'tasks': tasks})


class deleteTask(Resource):
    def delete(self):
        task_id = request.json['id']
        for task in tasks:
            if task_id == task['id']:
                tasks.remove(task)
                return jsonify({'tasks': tasks}), 201


@todo.errorhandler(404)
def handle_api_not_found(error):
    # response 的 json 内容为自定义错误代码和错误信息
    response = jsonify({'error': "not found"})

    # response 返回 error 发生时定义的标准错误代码
    response.status_code = error.status_code

    return response

class test(Resource):
    def get(self):
        return send_file("templates/tasks.html")
## Actually setup the Api resource routing here

class upload(Resource):
    def get(self):
        fileList = os.listdir(current_app.config['UPLOADED_FILES_DEST'])
        return jsonify(fileList)

    def post(self):
        print(request.headers)
        print(request.files)
        filename = files.save(request.files['file'])
        print(filename)
        return filename
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

api.add_resource(test, "/api")
api.add_resource(getTasks, "/api/tasks")
api.add_resource(addTask, "/api/addTask")
api.add_resource(deleteTask, "/api/deleteTask")
api.add_resource(TodoList, '/')
api.add_resource(Todo, '/<todo_id>')
api.add_resource(upload, '/api/upload')