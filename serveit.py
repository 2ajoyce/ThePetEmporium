"""A tornado server to serve ThePetEmporium"""

#Importing tornado to colaborate with flask
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from packit import login

http_server = HTTPServer(WSGIContainer(login))
http_server.listen(5000)
IOLoop.instance().start()
