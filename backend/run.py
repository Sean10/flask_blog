from flasky import create_app
from config import config

app = create_app(config)


from flasky.flaskr import flasky, init_db
from flasky.todo import todo
from flasky.client import client
# app.register_blueprint(flasky)
app.register_blueprint(todo, url_prefix='/todo')
# app.register_blueprint(client, url_prefix='/client')


#
# @app.cli.command('initdb')
# def initdb_command():
#     """Creates the database tables."""
#     init_db()
#     print('Initialized the database.')
#
# #@app.teardown_maincontext
# def close_db(error):
#     """Closes the database again at the end of the request."""
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()

app.run(debug=True)

