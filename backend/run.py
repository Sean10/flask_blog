from flasky import create_app
from config import config


app = create_app(config)

# db.create_all()

from flasky.flaskr import flasky, init_db
from flasky.todo import todo
from flasky.client import client
from flasky import db
from flasky.models import TodoList,UserPW
# app.register_blueprint(flasky)
app.register_blueprint(todo, url_prefix='/todo')
# app.register_blueprint(client, url_prefix='/client')

db.create_all()

todo1 = TodoList(id=1, task=u"build an API", user='admin')
todo2 = TodoList(id=2, task=u'?????', user='admin')
todo3 = TodoList(id=3, task=u'profit!', user='guest')

# db.session.add(UserPW(id=1, username=u"admin", password=u"admin"))
# db.session.add(UserPW(id=2, username=u"guest", password=u"guest"))
#
#
# db.session.add(todo1)
# db.session.add(todo2)
# db.session.add(todo3)
# db.session.commit()

app.run(debug=True)

