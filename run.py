"""A tornado server to serve ThePetEmporium"""

#Importing tornado to colaborate with flask
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import App
from app import controller
from app import db_models

db_models.init_db()
http_server = HTTPServer(WSGIContainer(App))
http_server.listen(5000)
IOLoop.instance().start()
