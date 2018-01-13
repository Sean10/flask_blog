from flasky import create_app
from config import config


app = create_app(config)

# db.create_all()

from flasky.flaskr import flasky, init_db
from flasky.todo import todo
from flasky.client import client
from flasky import db
# app.register_blueprint(flasky)
app.register_blueprint(todo, url_prefix='/todo')
# app.register_blueprint(client, url_prefix='/client')

db.create_all()

app.run(debug=True)

